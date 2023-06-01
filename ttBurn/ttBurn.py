import logging
import eth_account
from abi.abi import getABI
from web3 import Web3
from web3.middleware import geth_poa_middleware
from config.config import BlockchainConf
import datetime
import time


def burnTT(conn):
    amount = countTT(conn)
    if amount is None:
        logging.info("amount is 0")
        return
    w3 = Web3(Web3.HTTPProvider(BlockchainConf['RPC']))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    burnHsh = burn(w3, amount)
    if burnHsh is None:
        return
    print(burnHsh)
    updateDestroyState(conn, burnHsh)


def countTT(conn):
    try:
        yesterday_start_time, yesterday_end_time = yesterdayTimestamp()
        with conn.cursor() as cursor:
            sql = "select sum(destroy_count) as amount from mining_destroy where status=2 and add_time>={} and  add_time<={} ".format(
                yesterday_start_time, yesterday_end_time)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]

    except Exception as e:
        logging.error("countTT error：\n", e)
        return None


def updateDestroyState(conn, destroy_hash):
    try:
        yesterday_start_time, yesterday_end_time = yesterdayTimestamp()
        with conn.cursor() as cursor:
            sql = "update mining_destroy set status=1,destroy_hash='{}' where status=2 and add_time>={} and  add_time<={} ".format(
                destroy_hash, yesterday_start_time, yesterday_end_time)
            cursor.execute(sql)
            conn.commit()
    except Exception as e:
        logging.error("updateDestroyState error：\n", e)
        return None


def burn(w3, amount):
    try:
        ttAddress = w3.toChecksumAddress(BlockchainConf['TdexContractAddress'])
        burnAccount = w3.toChecksumAddress(BlockchainConf['burnAccount'])
        burnAccountKey = BlockchainConf['burnAccountKey']
        ttBurnAddress = w3.toChecksumAddress(BlockchainConf['TdexBurnContractAddress'])

        ttContract = w3.eth.contract(address=ttAddress, abi=getABI("tt"))
        ttBurnContract = w3.eth.contract(address=ttBurnAddress, abi=getABI("ttBurn"))
        token_balance = w3.fromWei(ttContract.functions.balanceOf(burnAccount).call(), 'wei')
        # check balance
        if token_balance < amount:
            logging.error("burn error: insufficient balance")
            return None
        # approve
        nonce = w3.eth.get_transaction_count(burnAccount)
        baseFeePerGas = w3.eth.getBlock("pending").baseFeePerGas  # 即时的base，只用于预估的，最后不一定是这个值，所以一般计算max时会乘以一个系数2。
        baseFeePerGas = int("0x" + str(baseFeePerGas), 16)
        maxPriorityFeePerGas = w3.toWei(2, "gwei")
        maxFeePerGas = baseFeePerGas * 2 + maxPriorityFeePerGas
        # tx = {
        #     'from': myAddress,
        #     'nonce': nonce,
        #     'gas': 100000,
        #     'gasPrice': w3.toWei('50', 'gwei'), # 或者下面的方式
        #     'chainId': 80001
        # }  # transfer tx
        # txn = ttContract.functions.transfer(ttBurnAddress, w3.toWei(amount, 'ether')).buildTransaction(tx)  # transfer
        txn = ttContract.functions.approve(ttBurnAddress, w3.toWei(str(amount), 'wei')).buildTransaction({
            'from': burnAccount,
            'maxFeePerGas': maxFeePerGas,
            'maxPriorityFeePerGas': maxPriorityFeePerGas,
            'nonce': nonce
        })
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=burnAccountKey)
        w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # allowance = ttContract.functions.allowance(myAddress, ttBurnAddress).call()  # 查看 allowance
        # print(123)
        # return None
        time.sleep(5)
        # burn
        nonce = w3.eth.get_transaction_count(burnAccount)
        txn_dict = ttBurnContract.functions.burn(w3.toWei(str(amount), 'wei')).buildTransaction({
            'from': burnAccount,
            'maxFeePerGas': maxFeePerGas,
            'maxPriorityFeePerGas': maxPriorityFeePerGas,
            'nonce': nonce
        })
        signed_txn = w3.eth.account.sign_transaction(txn_dict, private_key=burnAccountKey)
        tx_hash_bytes = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        destroy_hash = parseHex(tx_hash_bytes)
        return destroy_hash
    except Exception as e:
        logging.error("burn error:", e)
        return None


def parseHex(bytes_hex):
    hexStr = ''.join([hex(x)[2:].zfill(2) for x in bytes_hex])
    return "0x" + hexStr.lstrip("0")


def yesterdayTimestamp():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    return yesterday_start_time, yesterday_end_time

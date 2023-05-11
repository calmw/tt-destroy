import logging
import time
from web3 import Web3
from blockstore.blockstore import get_poll_height, save_poll_height
from config.config import BlockchainConf

w3 = Web3(Web3.HTTPProvider(BlockchainConf["RPC"]))


def poll_block(conn):
    try:
        latest_block = w3.eth.blockNumber
        chain_id = w3.eth.chain_id
        start_height = get_poll_height()
        end_height = start_height + BlockchainConf["step"]
        if (end_height - latest_block) > BlockchainConf["step"] / 5:
            logging.info("跳过")
            return
        contract_address = w3.toChecksumAddress(BlockchainConf["contractAddress"])
        filters = {
            'fromBlock': start_height,
            'toBlock': end_height,
            'address': contract_address,
            'topics': ['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef']
        }
        logs = w3.eth.get_logs(filters)
        for log in logs:
            from_address_bytes = log.topics[1]
            to_address_bytes = log.topics[2]
            to_address = '0x' + ''.join([hex(x)[2:].zfill(2) for x in to_address_bytes])
            tx_hash_bytes = log.transactionHash
            tx_hash = '0x' + ''.join([hex(x)[2:].zfill(2) for x in tx_hash_bytes])
            if to_address == "0x0000000000000000000000000000000000000000000000000000000000000000":
                # 入库
                destroy_num = int(log.data, 16)
                block_num = log.blockNumber
                destroy_address = contract_address
                to_address = "0x0000000000000000000000000000000000000000"
                from_address = parse_address(from_address_bytes)
                save_destroy_info(conn, chain_id, destroy_num, block_num, destroy_address,
                                  from_address, to_address, tx_hash)
            else:
                logging.info("非销毁的Transfer事件")
        save_poll_height(end_height)

    except Exception as e:
        logging.error("poll_block error：\n", e)


def parse_address(bytes_address):
    address_temp = ''.join([hex(x)[2:].zfill(2) for x in bytes_address])
    address_temp = "0x" + address_temp.lstrip("0")
    address_temp = w3.toChecksumAddress(address_temp)
    return w3.toChecksumAddress(address_temp)


def save_destroy_info(conn, chain_id, destroy_num, block_num, destroy_address, from_address, to_address, tx_hash):
    try:
        with conn.cursor() as cursor:
            sql = "select block_height from mining_trade_fee_destroy where block_height={} order by add_time desc limit 1".format(
                block_num)
            cursor.execute(sql)
            block_height = cursor.fetchone()
            if block_height is None:
                sql = "insert into mining_trade_fee_destroy (contract_address,destroy_count,block_height,add_time,chain_id,from_address,to_address,tx_hash) values('{}', {}, {}, {},{},'{}','{}','{}')".format(
                    destroy_address,
                    destroy_num,
                    block_num,
                    int(time.time()),
                    chain_id,
                    from_address,
                    to_address,
                    tx_hash
                )
                cursor.execute(sql)
            conn.commit()
            logging.info("入库成功")
    except Exception as e:
        logging.error("insert_db error：\n", e)
        return None

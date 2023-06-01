import logging
from blockchain.blockchain import poll_block
from db import mysql
from ttBurn.ttBurn import burnTT


def destroyTt():
    conn = mysql.mysql_db()
    if conn is None:
        exit(1)
    try:
        poll_block(conn)
    except Exception as e:
        logging.error("destroyTt error：\n", e)


def burnTt():
    conn = mysql.mysql_db()
    if conn is None:
        exit(1)
    try:
        burnTT(conn)
    except Exception as e:
        logging.error("burnTt error：\n", e)

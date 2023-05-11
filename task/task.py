import logging
from core.blockchain import poll_block
from db import mysql


def destroy_tt():
    conn = mysql.mysql_db()
    if conn is None:
        exit(1)

    try:
        poll_block(conn)
    except Exception as e:
        logging.error("destroy_tt error：\n", e)

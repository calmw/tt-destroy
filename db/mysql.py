import pymysql
import logging
import config.config


# mysql
def mysql_db():
    try:
        conn = pymysql.connect(
            host=config.config.dbConf.get('host'),
            port=config.config.dbConf.get('port'),
            database=config.config.dbConf.get('database'),
            charset=config.config.dbConf.get('charset'),
            user=config.config.dbConf.get('user'),
            passwd=config.config.dbConf.get('passwd'),
        )
        return conn
    except Exception as e:
        logging.error("数据库连接失败：\n", e)
        return None

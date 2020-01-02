import configparser
import pymysql

config = configparser.ConfigParser()
config.read('config.ini')


class DB():
    def __init__(self, host=config['mysql']['mysql_url'], port=3306, db=config['mysql']['mysql_db'],
                 user=config['mysql']['mysql_user'], passwd=config['mysql']['mysql_password'], charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset,
                                    autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()

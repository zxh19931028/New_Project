# coding=utf-8

import mysql.connector


mysql_configs = {
    '172.16.0.20': {
        'host': '172.16.0.20',
        'user': 'zhangxiaogang',
        'password': 'gangxiaozhang',
        'port': 3306,
        'database': 'court_notice',
        'charset': 'utf8'
              },
                 }


class MySQL(object):

    fetch_batch_size = 1000

    def __init__(self, host, db=None, auto_commit=True):
        if db:
            mysql_configs['database'] = db
        self.connection = mysql.connector.connect(**mysql_configs[host])
        self.connection.autocommit = auto_commit
        self.cursor = self.connection.cursor()

    def execute_query(self, sql, params=()):
        self.connection.ping(True)
        self.cursor.execute(sql, params)
        while True:
            _res = self.cursor.fetchmany(self.fetch_batch_size)
            if _res:
                for _row in _res:
                    yield _row
            else:
                break

    def execute_and_fetch_all(self, sql, params=()):
        self.connection.ping(True)
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def execute_update(self, sql, params=()):
        self.connection.ping(True)
        self.cursor.execute(sql, params)

    def execute_many_update(self, sql, params):
        self.connection.ping(True)
        self.cursor.executemany(sql, params)


if __name__ == '__main__':
    mysql20 = MySQL('172.16.0.20')
    mysql20.execute_and_fetch_all("select * from ktgg.tsgkw where case_id='1011508'")



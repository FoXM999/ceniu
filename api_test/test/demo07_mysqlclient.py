# Author:zqbin
# @Time:2023/10/1 18:28
# @Author:14988
# @Site:
# @File:demo07_mysqlclient.py
# @Software:PyCharm
import pymysql

from lib.config import CONFIG


class MySQLClient:

    def __init__(self,host=None,port=None,user=None,password=None,db=None):
        self.database = {
            'host': CONFIG.get('database', 'host') if host is None else host,
            'db': CONFIG.get('database', 'db') if db is None else db,
            'port': CONFIG.get('database', 'port') if port is None else port,
            'user': CONFIG.get('database', 'user') if port is None else user,
            'password': CONFIG.get('database', 'password') if port is None else password
        }

    def select(self, sql):
        with pymysql.connect(**self.database) as conn:
            with conn.cursor() as cur:
                ret = cur.execute(sql)
                conn.commit()
                return ret

    def execute(self, sqlList):
        with pymysql.connect(**self.database) as conn:
            with conn.cursor() as cur:
                retlist = []
                try:
                    for sql in sqlList:
                        retlist.append(cur.execute(sql))
                except Exception as e:
                    print(e)
                    conn.rollback()
                else:
                    conn.commit()
                    return retlist

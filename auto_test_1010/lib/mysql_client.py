# Author:zqbin
# @Time:2023/9/26 17:43
# @Author:14988
# @Site:
# @File:mysql_client.py
# @Software:PyCharm
"""
对pymysql模块使用的二次封装
提供2个接口;
select(sql):执行查询语句，返回查询结果集记录的条数
execute(sqls):参数是一个列表，执行列表中所有的SQL语句，支持事务的功能
"""
import pymysql
from lib.config import CONFIG
from lib.logger import Logger


class MySQLClient:
    def __init__(self, host=None, port=None, db=None, user=None, password=None):
        self.dbInfo = {
            "host": CONFIG.get("database", "host") if host is None else host,
            "port": CONFIG.getint("database", "port") if port is None else port,
            "db": CONFIG.get("database", "db") if db is None else db,
            "user": CONFIG.get("database", "user") if user is None else user,
            "password": CONFIG.get("database", "password") if password is None else password
        }
        self.__logger = Logger()

    def select(self, sql):
        """
        执行select语句的接口
        :param sql: str 要执行的SQL语句
        :return: 查询结果集的记录的数量
        """
        with pymysql.connect(**self.dbInfo) as connection:
            with connection.cursor() as cursor:
                self.__logger.info(f"执行sql:{sql}")
                return cursor.execute(sql)

    def execute(self, sqlList):
        """
        执行插入，修改，删除语句的接口,支持事务
        :param sqlList: iterable[str] 由SQL语句组成的可迭代对象
        :return: None
        """
        with pymysql.connect(**self.dbInfo) as connection:
            with connection.cursor() as cursor:
                retList = []
                try:
                    for sql in sqlList:
                        self.__logger.info(f"执行sql:{sql}")
                        ret = cursor.execute(sql)
                        retList.append(ret)
                except Exception as e:
                    self.__logger.info(f"执行{sql}异常：{e}")
                    connection.rollback()  # 回滚
                else:
                    connection.commit()
                    return retList


if __name__ == '__main__':
    pass
# Author:zqbin
# @Time:2023/9/26 14:07
# @Author:14988
# @Site:
# @File:test_register.py
# @Software:PyCharm
import unittest
from lib.mysql_client import MySQLClient
from lib.logger import Logger
from lib.http_client import HTTPClient
from jsonpath import jsonpath


class TestRegister01(unittest.TestCase):
    __logger = Logger()
    __httpclient = HTTPClient()

    @classmethod
    def setUp(cls) -> None:
        cls.__logger.info("开始执行测试用例--注册接口")
        client = MySQLClient()
        sql1 = 'delete from auth_user where username="test926_901"'
        sql2 = 'delete from user_profile where name="test926_901"'
        client.execute([sql1, sql2])

    @classmethod
    def tearDown(cls) -> None:
        client = MySQLClient()
        sql1 = 'delete from auth_user where username="test926_901"'
        sql2 = 'delete from user_profile where name="test926_901"'
        client.execute([sql1, sql2])
        cls.__logger.info("结束执行测试用例--注册接口")

    def test_method(self):
        method = "post"
        data = {
            "name": "test926_901",
            "password1": "123456",
            "password2": "123456"
        }
        r = self.__httpclient.request('/register/', method=method, json=data)

        expectValue = 200
        currentValue = r.status_code
        self.assertEqual(expectValue, currentValue)

        expectValue = '200'
        # currentValue = r.json()['code']
        currentValue = jsonpath(r.json(), '$..code')[0]
        # TestRegister01.__logger.info(f'currentValue={currentValue}')
        self.assertEqual(expectValue, currentValue)

        expectValue = 1
        client = MySQLClient()
        sql1 = 'select * from auth_user where username="test926_901"'
        sql2 = 'select * from user_profile where name="test926_901"'
        retList = client.execute([sql1, sql2])
        currentValue = retList[0]
        self.assertEqual(expectValue, currentValue)
        currentValue = retList[1]
        self.assertEqual(expectValue, currentValue)

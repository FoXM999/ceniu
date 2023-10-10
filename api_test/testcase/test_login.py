# Author:zqbin
# @Time:2023/9/26 15:00
# @Author:14988
# @Site:
# @File:test_login.py
# @Software:PyCharm
import unittest
import test_register
from lib.mysql_client import MySQLClient
from lib.logger import Logger
from lib.http_client import HTTPClient


class TestRegister01(unittest.TestCase):
    __logger = Logger()
    __httpclient = HTTPClient()

    @classmethod
    def setUp(cls) -> None:
        cls.__logger.info("开始执行测试用例--登录接口")
        t = test_register.TestRegister01()
        t.test_method()

    @classmethod
    def tearDown(cls) -> None:
        client = MySQLClient()
        sql1 = 'delete from auth_user where username="test926_901"'
        sql2 = 'delete from user_profile where name="test926_901"'
        client.execute([sql1, sql2])
        cls.__logger.info("结束执行测试用例--登录接口")

    def test_method(self):
        method = "post"
        data = {
            "name": "test926_901",
            "password": "123456",
        }
        r = self.__httpclient.request('/login/', method=method,json=data)

        expectValue = 200
        currentValue = r.status_code
        self.assertEqual(expectValue, currentValue)

        expectValue = '200'
        currentValue = r.json()['code']
        self.assertEqual(expectValue, currentValue)

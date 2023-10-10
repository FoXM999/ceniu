# Author:zqbin
# @Time:2023/9/26 15:00
# @Author:14988
# @Site:
# @File:mytestcase2.py
# @Software:PyCharm
import unittest
import requests


class TestRegister01(unittest.TestCase):
    def test_method(self):
        baseUrl = "http://39.108.127.130:8008"
        path = "/login/"
        method = "post"
        data = {
            "name": "test926_901",
            "password": "123456",
        }
        r = requests.request(method=method, url=baseUrl + path, json=data)
        expectValue = '200'
        currentValue = r.json()['code']
        self.assertEqual(expectValue, currentValue)
# Author:zqbin
# @Time:2023/10/1 17:36
# @Author:14988
# @Site:
# @File:test_test.py
# @Software:PyCharm
import unittest


class TestTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')

    def test_demo1(self):
        print('test')
        self.assertEqual(1, 1)

    def test_demo2(self):
        print('test2')
        self.assertEqual(2, 1)

    def tearDown(self) -> None:
        print('tearDown')

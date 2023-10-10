# Author:zqbin
# @Time:2023/9/26 14:51
# @Author:14988
# @Site:
# @File:08_fixture.py
# @Software:PyCharm
import unittest


# 进入当前模块的时候会调用1次该函数
def setUpModule():
    print("setUpModule")


# 退出当前模块前会调用1次该函数
def tearDownModule():
    print("tearDownModule")


class TestDemo(unittest.TestCase):
    # 在执行该类的所有测试方法之前只执行一次该方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    # 在执行该类的所有测试方法之后只执行一次该方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    # 在该类当中的所有的测试方法执行前都会执行一次该方法
    def setUp(self) -> None:
        print("setUp")

    # 在该类当中的所有的测试方法执行后都会执行一次该方法
    def tearDown(self) -> None:
        print("tearDown")

    def test_method_01(self):
        print("test_method_01")

    def test_method_02(self):
        print("test_method_02")
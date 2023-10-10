# Author:zqbin
# @Time:2023/9/26 14:41
# @Author:14988
# @Site:
# @File:runner.py
# @Software:PyCharm
import unittest
from mytestcase import TestRegister01

suite = unittest.TestSuite()
suite.addTest(TestRegister01('test_method'))
runner = unittest.TextTestRunner()
runner.run(suite)
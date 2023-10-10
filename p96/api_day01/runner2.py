# Author:zqbin
# @Time:2023/9/26 14:46
# @Author:14988
# @Site:
# @File:runner2.py
# @Software:PyCharm
import unittest

suite = unittest.defaultTestLoader.discover("unitest_demo", '*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
# Author:zqbin
# @Time:2023/9/26 15:01
# @Author:14988
# @Site:
# @File:09_report.py
# @Software:PyCharm
import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./unitest_demo", '*.py')

with open("report.html", "wb") as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title="测试报告",
        description="描述信息"
    )
    runner.run(suite)
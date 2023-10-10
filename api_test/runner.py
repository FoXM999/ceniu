# Author:zqbin
# @Time:2023/9/26 15:09
# @Author:14988
# @Site:
# @File:runner.py.py
# @Software:PyCharm

"""
测试框架的入口文件
通过执行该文件，执行框架当中的所有的测试用例
并且生成测试报告，保存到report目录
为了测试报告不被覆盖，（没次执行都有对应的测试报告）
测试报告的名称规则为: report_2023_09_26_15_10_22.html
"""
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
import time
import os

# suite = unittest.defaultTestLoader.discover('./testcase', '*.py')
# filename = time.strftime('report_%Y_%m_%d_%H_%M_%S')
# if not os.path.exists('./report'):
#     os.makedirs('./report')
# with open("./report/" + filename + '.html', "wb") as f:
#     runner = HTMLTestRunner(
#         stream=f,
#         verbosity=2,
#         title=filename,
#         description="描述信息"
#     )
#     runner.run(suite)

# 获取当前文件的绝对路径
filePath = os.path.abspath(__file__)

# 获取项目的根目录的绝对路径
rootDir = os.path.dirname(filePath)

# 获取测试用例存放的目录的绝对路径
caseDir = os.path.join(rootDir, "testcase")

# 获取测试报告存放的路径
reportDir = os.path.join(rootDir, "report")

# 确定测试报告的名称
reportName = time.strftime("report_%Y_%m_%d_%H_%M_%S.html")

# 确定测试报告文件的绝对路径
reportPath = os.path.join(reportDir, reportName)

# 加载测试用例，得到测试套件
suite = unittest.defaultTestLoader.discover(caseDir)

# 打开测试报告文件
with open(reportPath, "wb") as f:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title=reportName,
        description="WMS系统接口测试报告"
    )
    # 执行测试
    runner.run(suite)
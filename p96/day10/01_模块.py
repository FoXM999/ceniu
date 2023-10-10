# Author:zqbin
# @Time:2023/9/20 10:02
# @Author:14988
# @Site:
# @File:01_模块.py
# @Software:PyCharm
import re

import module
import module.m01
import requests
import time
from decimal import Decimal
import os.path as path
import logging

print(module.strTest1)
print(module.m01.strTest2)

# sleep(2)
# print(time())

print(dir())

d1 = Decimal('1.01')
d2 = Decimal('1.02')
print(d1 + d2)

print(__file__)
print(path.basename(__file__))
print(path.dirname(__file__))

logging.error('测试')

# year = input('请输入年：')
# month = input('请输入月：')
# day = input('请输入日：')
# t = '-'.join([year, month, day])
# t = time.strptime(t, '%Y-%m-%d')
# print(t)
# print(t.tm_yday)


m = re.search(r'(\d+)\.(\d+)', 'a24.123 12.23')
print('group',m.group())
print('groups',m.groups())



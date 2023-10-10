# Author:zqbin
# @Time:2023/9/20 16:40
# @Author:14988
# @Site:
# @File:04_datetime.py
# @Software:PyCharm

from datetime import datetime
import time

print(datetime.today())
print(datetime.now())
print(datetime.fromtimestamp(time.time()))
a = datetime.now()
print(a.year)
print(a.ctime())
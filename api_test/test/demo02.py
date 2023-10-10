# Author:zqbin
# @Time:2023/9/26 19:28
# @Author:14988
# @Site:
# @File:demo02.py
# @Software:PyCharm
from lib.mysql_client import MySQLClient

# client = MySQLClient()
# sql1 = 'delete from auth_user where username="test926_901"'
# sql2 = 'delete from user_profile where name="test926_901"'
# ret = client.execute([sql1, sql2])
# print(ret)

client = MySQLClient()
sql1 = 'select * from auth_user where username="test926_901"'
sql2 = 'select * from user_profile where name="test926_901"'
retList = client.execute([sql1, sql2])
print(retList)
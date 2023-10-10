# Author:zqbin
# @Time:2023/9/26 16:33
# @Author:14988
# @Site:
# @File:demo03_upload_wait.py
# @Software:PyCharm
import pymysql

with pymysql.connect(
    host='localhost',
    port=33060,
    db='student',
    user='root',
    password='123456'
) as connection:
    with connection.cursor() as cursor:
        sql = "select * from students;"
        ret = cursor.execute(sql)
        print('ret=', ret)
        print(cursor.fetchone())
        print(cursor.fetchmany(3))
        print(cursor.fetchall())

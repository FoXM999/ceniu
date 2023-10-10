# Author:zqbin
# @Time:2023/9/26 16:21
# @Author:14988
# @Site:
# @File:demo02_upload.py
# @Software:PyCharm
import pymysql

connection = pymysql.connect(
    host='localhost',
    port=33060,
    db='student',
    user='root',
    password='123456'
)
cursor = connection.cursor()
# sql = "insert into students values('015', '后羿', '男', '北京', 30, '2班', NULL);"
sql = "update students set name='关羽' where studentNo=15;"
# sql = "delete from students where studentNo=15;"
ret = cursor.execute(sql)
connection.commit()
cursor.close()
connection.close()

# Author:zqbin
# @Time:2023/9/26 17:22
# @Author:14988
# @Site:
# @File:delete_user.py
# @Software:PyCharm
import pymysql

with pymysql.connect(
        host="39.108.127.130",
        port=3306,
        db="wms",
        user="root",
        password="Ceniu2023!"
) as conn:
    with conn.cursor() as cursor:
        sql1 = 'delete from auth_user where username="test926_901"'
        sql2 = 'delete from user_profile where name="test926_901"'
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
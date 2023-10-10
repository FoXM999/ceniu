# Author:zqbin
# @Time:2023/9/26 16:17
# @Author:14988
# @Site:
# @File:demo01.py
# @Software:PyCharm
# 1. 导入模块
import pymysql

# 2. 创建数据库连接
connection = pymysql.connect(
    host="localhost",
    port=33060,
    db="student",
    user="root",
    password="123456"
)
# 3. 创建游标
cursor = connection.cursor()
# 4. 准备好要执行的SQL语句
sql = "INSERT INTO students values('015', '后羿', '男', '北京', 30, '2班', NULL);"
# 5. 执行SQL语句
ret = cursor.execute(sql)   # 返回受影响的记录条数
print(ret)
# 6. 增删改操作需要提交
connection.commit()
# 7. 关闭游标
cursor.close()
# 8. 关闭数据库连接
connection.close()


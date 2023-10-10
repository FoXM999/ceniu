# Author:zqbin
# @Time:2023/9/15 15:17
# @Author:14988
# @Site:
# @File:mytestcase.py
# @Software:PyCharm

# f = open('./file/test.txt',encoding='utf-8')
# print(f.read(10))
# f.close()
#
# with open('./file/test.txt',encoding='utf-8') as f:
#     print(f.read(10))

# with open('./file/test.txt',mode='a+',encoding='UTF-8') as f:
#     f.write('hello world\n')
#     f.seek(0)
#     print(f.read())

# f = open('./file/test.txt',mode='r+',encoding='UTF-8')
# f.write('hello world\n')
# f.seek(0)
# print(f.read())
# f.close()

with open('./file/test.txt',mode='r',encoding='utf-8') as f:
    s = f.readline()
    while s:
        print(s.rstrip())
        s = f.readline()

print('学生信息管理系统'.ljust(100))
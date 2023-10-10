# Author:zqbin
# @Time:2023/9/8 14:47
# @Author:14988
# @Site:
# @File:mytestcase.py
# @Software:PyCharm


name = 'zs'
age = 18
height = 1.87
print('姓名：%s，年龄：%-05d，身高：%.2f' % (name, age, height))

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

i = 100
while i < 1000:
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i)
    i += 1

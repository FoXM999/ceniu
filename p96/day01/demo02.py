# Author:zqbin
# @Time:2023/9/8 10:14
# @Author:14988
# @Site:
# @File:demo02_upload.py
# @Software:PyCharm


x, y, z = 100, 200, 300 + 3.3
print(x, y, z)

x += 50
print(x)
print(220 % 3)

str = 'hello,world!'
print('wor' not in str)

d = {'name': 'zs', 'age': 18, 'address': 'gx'}
print('na' in d)

s2 = 'hello,world'
s3 = str

print(str is s2)
print(str is s3)

# x = int(input('请输入4位数：'))
# a = x // 1000
# b = x // 100 % 10
# c = x // 10 % 10
# d = x % 10
# print(a, b, c, d)

n = -13
print(n << 3)

# a = float(input('请输入第1个数：'))
# b = float(input('请输入第2个数：'))
# print(a if a > b else b)

num1 = 60  # 0011 1100
num2 = 13  # 0000 1101

num1 ^= num2
num2 ^= num1
num1 ^= num2
print(num1, num2)

num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))
print("大的那个数是:", num1 if num1 > num2 else num2)

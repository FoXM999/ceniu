# Author:zqbin
# @Time:2023/9/6 14:37
# @Author:14988
# @Site:
# @File:demo01.py
# @Software:PyCharm


print("hello world", 666, 'iloveu')
num01 = 257
print(num01)
num02 = 257
print(id(num01))
print(id(num02))
print(type(num01),type(num01)==int)

print(bin(10),oct(10),hex(10))

print(0.1+0.2)
c = 3+4j
print(c,type(c))

b1 = b'abc'
print(b1,type(b1))

# t = tuple(1,2,3)

t = frozenset({1,2,3})
print(t)
# t.
print(t)

t2 = {1,2,3}
print(t2)
t2.add(4)
print(t2)

print(bool(1))
print(bool(0.0))
print(bool('1'))
print(bool({}))
print(bool(()))
print(bool([]))

# a =input('请输入：')
# print(f'a={a}')
#
# while True:
#     if a=='1':
#         exit()
#     else:
#         a = input('请输入：')
#         print(f'a={a}')

a = input('请输入a:')
b = input('请输入b:')
print(f'交换前：a={a}，b={b}')
# t = a
# a = b
# b = t
a,b = b,a
print(f'交换后：a={a}，b={b}')

f2 = 3.123456e-2
print(f2, type(f2))


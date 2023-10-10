# Author:zqbin
# @Time:2023/9/11 10:10
# @Author:14988
# @Site:
# @File:09.py
# @Software:PyCharm

"""
这是一个demo文档
"""
import math
import string

s1 = '''this is a test text'''

# print(s1)
# print(__doc__)

# print(s1[0])
# print(s1[1])
# print(s1[2])

# print(s1[::2])

# print('I\'am Tom')
# print(r'I\'am Tom')
# print('I\'\nam \tTom')
# print(s1[0:4])
# print(s1[0:])
# print(s1[::-2])
#
# print(s1.find('is'))
#
# print(s1.replace('s', 'sss'))
# print(s1.replace('s', 'sss', 1))

# s2 = s1.split(' ')
# print(s2)
# print(len(s1))
# print(s1[-1])
# print('$$'.join(s2))

s = 'Python'
# print(s[-2:1:-1])
# print(s[:3:-1])
# print(s[::-1])
#
s = 'PythonPythonPython'
count = s.count('y')
start = 0
i = 0
while i<count:
    s2 = s.index('y', start)
    print(s2)
    start = s2 + 1
    i += 1


for i,char in enumerate(s):
    if char == 'y':
        print(i)

print(max(s))
print(min(s))

r = range(4)
print(r)

for i in range(4,1,-1):
    print(i)
print(s[4:0:-1])

print(s.replace('P','p'))

# s = input('请输入字符串：')
# zm = 0
# sz = 0
# kg = 0
# other = 0
# for i in s:
#     if i in string.ascii_letters:
#         zm += 1
#         print(i)
#     elif i.isdigit():
#         sz += 1
#     elif i.isspace():
#         kg += 1
#     else:
#         other += 1
# print(zm,sz,kg,other)

print(s.split())
ss = '   hello   '
print(ss)
print(ss.strip())

ss = 'he name is Tom'
print(ss.startswith('he'))
print(ss.startswith('eh'))
print(ss.endswith('Tom'))
print(ss.endswith('To'))

ss = ss.encode()
print(ss,type(ss))
ss = ss.decode()
print(ss,type(ss))

# print(ss.removeprefix('he'))
print(ss.lstrip('he '))
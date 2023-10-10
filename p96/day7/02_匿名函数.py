# Author:zqbin
# @Time:2023/9/15 11:09
# @Author:14988
# @Site:
# @File:02_匿名函数.py
# @Software:PyCharm

f1 = lambda x,y:x if x > y else y
print(f1(10,20))

f2 = lambda :100
print(f2())

l1 = [1, 3, 9, 2, 0, -9, 4]

print(sorted('hello'))
print(sorted(l1))

l = ['1班','2班','3班','11班','12班']

print(sorted(l))

l1.sort(key=lambda x:x.get('age'))
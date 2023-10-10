# Author:zqbin
# @Time:2023/9/13 10:24
# @Author:14988
# @Site:
# @File:01.py
# @Software:PyCharm

s1 = frozenset()
s2 = set()
print(s1,type(s1))
print(s2,type(s2))

s3 = {i**3 for i in range(2,11) if i%2 == 0}
print(s3,type(s3))

lst = list(s3)
print(lst,type(lst))
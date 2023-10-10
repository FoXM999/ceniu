# Author:zqbin
# @Time:2023/9/16 16:55
# @Author:14988
# @Site:
# @File:07_高阶函数.py
# @Software:PyCharm

import functools

lst1 = list(map(lambda x: x ** 3, range(1, 11)))
print(lst1)

lst2 = list(map(lambda x: 2 * x, [1, 2, 3, 4, 5]))
print(lst2)

lst3 = [i for i in range(1, 21)]
print(list(filter(lambda x: x % 3 == 0, lst3)))

lst4 = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x + y, lst4))
print(functools.reduce(lambda x, y: x + y, lst4, 10))

print(abs(-5.6))
print(abs(5.6))

print(all(lst4))
print(all(lst4 + [0]))

print(any(lst4))
print(any(lst4 + [0]))

s1 = ord('A')
print(s1)
print(chr(s1))

m,s = divmod(100,21)
print(m,s)

print(pow(2,3))
print(pow(2,3,7))

print(list(reversed(lst4)))

f = 16.2387
f2 = 16.5387
print(round(f))
print(round(f,2))
print(round(f2))
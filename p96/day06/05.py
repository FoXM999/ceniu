# Author:zqbin
# @Time:2023/9/14 11:50
# @Author:14988
# @Site:
# @File:mytestcase.py
# @Software:PyCharm


def f(a, b):
    m = max(a, b)
    n = min(a, b)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

print(f(30,48))
# 18 30
# 12 18
# 12 6
# 6 6
#
# 18 30
# 12 18
# 6 12
def f2(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(f2(30,45))
# 15 30

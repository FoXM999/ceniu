# Author:zqbin
# @Time:2023/9/14 14:34
# @Author:14988
# @Site:
# @File:06.py
# @Software:PyCharm


def my_sum(a:str,b:str) -> int:
    return a+b

print(my_sum(1,2))
print(my_sum(1.4,2.5))

def f1(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(f1(4))

def  f2(n):
    if n == 1:
        return 1
    return n * f2(n-1)


print(f2(4))


def f3(s):
    if s == '':
        return ''
    if len(s) == 1:
        return s[0]
    return s[-1] + f3(s[:len(s)-1])


print(f3('hello'))

def f4(n):
    if n == 1 or n == 2:
        return 2
    return f4(n-1) + f4(n-2)

print(f4(4))
# Author:zqbin
# @Time:2023/9/14 11:25
# @Author:14988
# @Site:
# @File:04.py
# @Software:PyCharm


def my_sum(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for i in kwargs.values():
        result += i
    return result


print(my_sum())                                 # 0
print(my_sum(1))                                # 1
print(my_sum(a=1))                              # 1
print(my_sum(1, 2, 3, 4))                       # 10
print(my_sum(a=10, b=2, c=3, d=4))              # 19
print(my_sum(1, 2, 3, 4, a=10, b=2, c=3, d=4))  # 29
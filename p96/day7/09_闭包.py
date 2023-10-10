# Author:zqbin
# @Time:2023/9/19 15:22
# @Author:14988
# @Site:
# @File:09_闭包.py
# @Software:PyCharm

def f1():
    count = 0

    def f2():
        nonlocal count
        count += 1
        print(count)
    return f2


f = f1()
f()
f()

f2 = f1()
f2()
f2()
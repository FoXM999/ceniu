# Author:zqbin
# @Time:2023/9/14 16:26
# @Author:14988
# @Site:
# @File:08_汉诺塔.py
# @Software:PyCharm


def f(n, start="A", helper="B", target="C"):
    if n == 1:
        print("%s --> %s" % (start, target))
        return
    else:
        f(n-1, start, target, helper)
        print("%s --> %s" % (start, target))
        f(n-1, helper, start, target)


f(4)
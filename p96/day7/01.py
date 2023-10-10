# Author:zqbin
# @Time:2023/9/15 10:38
# @Author:14988
# @Site:
# @File:01.py
# @Software:PyCharm

a = 10
b = 20

def f():
    a = 100
    print(a,b)

    def f2():
        global b
        nonlocal a
        a = 1000
        c = 3000
        b = 2000
        print(a,b)
        print(globals())
        print(locals())

    f2()
    print(a,b)

f()
print(a,b)

print(globals())
print(locals())
# Author:zqbin
# @Time:2023/9/14 10:17
# @Author:14988
# @Site:
# @File:01.py
# @Software:PyCharm


def my_length(seq):
    length = 0
    for i in seq:
        length += 1
    print(length)


my_length([1, 2, 3, 4, 5])

def test1(a,b,c):
    print(a,b,c)

test1(4,b=2,c=3)

print(' yield '.center(50,'='))
def my_f():
    yield 1
    yield 2
    yield 3


f = my_f()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
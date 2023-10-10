# Author:zqbin
# @Time:2023/9/19 14:31
# @Author:14988
# @Site:
# @File:03_生成器.py
# @Software:PyCharm

def my_range(n):
    index = 0
    while index < n:
        yield index
        index += 1


ret = my_range(5)


# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))

class StepIsZero(Exception):
    def __init__(self, msg):
        self.msg = msg


def my_range2(start, end, step=1):
    if step == 0:
        raise StepIsZero('步长不能为0')

    while (step > 0 and start < end) or \
            (step < 0 and start > end):
        yield start
        start += step


for i in my_range2(1, 11):
    print(i)

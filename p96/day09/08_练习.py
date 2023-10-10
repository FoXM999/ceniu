# Author:zqbin
# @Time:2023/9/19 20:42
# @Author:14988
# @Site:
# @File:08_练习.py
# @Software:PyCharm

class StepIsZero(Exception):
    def __init__(self, msg):
        self.msg = msg


class MyRangeIterator:
    def __init__(self, start, end, step):
        if step == 0:
            raise StepIsZero('步长不能为0')
        self.index = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.end > self.index) or \
                (self.step < 0 and self.end < self.index):
            ret = self.index
            self.index += self.step
            return ret
        else:
            raise StopIteration


# for i in MyRangeIterator(10,-1,-2):
#     print(i)

class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return MyRangeIterator(self.start, self.end, self.step)


# for i in MyRange(10,-1,0):
#     print(i)

def my_range(start, end, step):
    if step == 0:
        raise StepIsZero('步长不能为0')
    while (step > 0 and start < end) or (step < 0 and start > end):
        yield start
        start += step


# print(ret)
# print(next(ret))
# try:
#     ret = my_range(10, -1, -2)
#     while True:
#         print(next(ret))
# except StopIteration:
#     pass

class Myrange2:
    def __init__(self, start, end, step):
        if step == 0:
            raise StepIsZero('步长不能为0')
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        # return my_range(self.start, self.end, self.step)
        return (i for i in range(self.start, self.end, self.step))


# for i in Myrange2(0, 11, 2):
#     print(i)

import time
import functools


# def get_time(f):
#     @functools.wraps(f)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         ret = f(*args, **kwargs)
#         end = time.time()
#         print('代码执行耗时：%.3f' % (end - start))
#         return ret
#
#     return wrapper
#
#
# @get_time
# def func(a, b, c):
#     time.sleep(2)
#     return a + b + c
#
#
# print(func(3, 5, c=2))


# def get_time(arg):
#     def mid(f):
#         @functools.wraps(f)
#         def wrapper(*args, **kwargs):
#             if arg:
#                 print('开始时间：' + time.strftime('%Y-%m-%d %H:%M:%S'))
#             else:
#                 print('开始时间：' + time.strftime('%Y-%m-%d %I:%M:%S %p'))
#             start = time.time()
#             ret = f(*args, **kwargs)
#             end = time.time()
#             if arg:
#                 print('结束时间：' + time.strftime('%Y-%m-%d %H:%M:%S'))
#             else:
#                 print('结束时间：' + time.strftime('%Y-%m-%d %I:%M:%S %p'))
#             print('代码执行耗时：%.3f' % (end - start))
#             return ret
#
#         return wrapper
#     return mid
#
#
# @get_time(False)
# def func(a, b, c):
#     time.sleep(2)
#     return a + b + c
#
#
# print(func(3, 5, c=2))


class GetTime:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.f(*args, **kwargs)
        end = time.time()
        print('代码执行耗时：%.3fs' % (end - start))
        return ret


@GetTime
def func(a, b, c):
    time.sleep(2)
    return a + b + c


print(func(3, 5, c=2))

# Author:zqbin
# @Time:2023/9/19 11:24
# @Author:14988
# @Site:
# @File:02_迭代器.py
# @Software:PyCharm

s = str('hello')
a = iter(s)
b = s.__iter__()
# print(a)
# print(b)

# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
#
# try:
#     while 1:
#         print(next(a))
# except:
#     pass


class StepIsZero(Exception):
    def __init__(self, msg):
        self.msg = msg


class MyRangeIterator:
    def __init__(self, start, end, step):
        self.index = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.index < self.end) or \
                (self.step < 0 and self.index > self.end):
            ret = self.index
            self.index += self.step
            return ret
        else:
            raise StopIteration


# myRangeIt = MyRangeIterator(0,11,1)
# for item in myRangeIt:
#     print(item)

def my_range(start, end, step=1):
    if step == 0:
        raise StepIsZero('步长不能为0')

    while (step > 0 and start < end) or \
            (step < 0 and start > end):
        yield start
        start += step

class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        # return MyRangeIterator(self.start, self.end, self.step)
        return my_range(self.start, self.end, self.step)


for i in MyRange(10, -1, -2):
    print(i)

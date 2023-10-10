# Author:zqbin
# @Time:2023/9/19 16:27
# @Author:14988
# @Site:
# @File:06_带参数的装饰器.py
# @Software:PyCharm

import time
import functools


def get_time(arg):
    def mid(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if arg:
                print('开始时间：' + time.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                print('开始时间：' + time.strftime('%Y-%m-%d %I:%M:%S %p'))
            start = time.time()
            ret = f(*args, **kwargs)
            end = time.time()
            if arg:
                print('结束时间：' + time.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                print('结束时间：' + time.strftime('%Y-%m-%d %I:%M:%S %p'))
            print('代码执行耗时：%.3fs' % (end - start))
            return ret

        return wrapper

    return mid


@get_time(False)
def func(a, b):
    time.sleep(3)
    return a + b


print(func(1, 2))

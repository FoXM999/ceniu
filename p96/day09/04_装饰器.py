# Author:zqbin
# @Time:2023/9/19 15:13
# @Author:14988
# @Site:
# @File:04_装饰器.py
# @Software:PyCharm

def super_man(func):
    def wrapper():
        func()
        print('会飞')

    return wrapper


# @super_man
def man():
    print('会爬')
    print('会走')
    print('会跑')


man()

import time
import decimal


def get_time(f):
    def wrapper():
        start = time.time()
        ret = f()
        end = time.time()
        print(f'代码执行耗时：{end - start}')
        return ret

    return wrapper


@get_time
def func(a, b):
    time.sleep(3)
    # print(3+2)
    return a + b


print(func(1, 2))

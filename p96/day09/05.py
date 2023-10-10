# 案例2：  通过装饰器统计函数执行的耗时
import time
import functools


def get_time(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        print(f'代码执行耗时：{end - start}')
        return ret

    return wrapper


@get_time
def func(a, b):
    time.sleep(3)
    return a + b


print(func(1, 2))


@get_time
def func2(a, b, c, d):
    """返回多个参数的值"""
    time.sleep(2)
    return a + b + c + d


print(func2(1, 2, 3, d=4))

print(func2.__name__)
print(func2.__doc__)
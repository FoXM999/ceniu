# Author:zqbin
# @Time:2023/9/14 11:19
# @Author:14988
# @Site:
# @File:03.py
# @Software:PyCharm

def func(a, b, c, *args, **kwargs):
    '''
    :param a:
    :param b:
    :param c:
    :param args:
    :param kwargs:
    :return:
    '''
    print(a, b, c)
    print(args)
    print(kwargs)


func(1, 2, c=3, d=4)

func(*(1,2,3))
func(**{'a':1,'b':2,'c':3,'d':4})

print(func.__doc__)
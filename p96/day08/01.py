# Author:zqbin
# @Time:2023/9/18 10:35
# @Author:14988
# @Site:
# @File:01.py
# @Software:PyCharm

class Hero(object):
    def __init__(self,name,atk):
        self.name = name
        self.atk = atk

    def info(self):
        print(self)

    def __new__(cls, *args, **kwargs):
        print('cls',cls)
        return object.__new__(cls)

    def __str__(self):
        return '{' + f'name={self.name}, atk={self.atk}' + '}'

    # def __del__(self):
    #     print('对象销毁了')

    def move(self):
        print('%s 开始移动' % self.name)


h1 = Hero('关羽',1000)
h1.info()
print(h1.__repr__())

h1.move()
Hero.move(h1)




# Author:zqbin
# @Time:2023/9/18 14:34
# @Author:14988
# @Site:
# @File:04_继承.py
# @Software:PyCharm

class Father:
    def __init__(self, name, age):
        print('Father')
        self.name = name
        self.age = age

    def sayHello(self):
        print(f'hello,my name is {self.name},age is {self.age}')

    def work(self):
        print('工作ing')


class Mather:
    def __init__(self, name, age):
        print('Mather')
        self.name = name
        self.age = age

    def work(self):
        print('打扫ing')


class Son(Father, Mather):
    def __init__(self, name, age):
        super().__init__(name, age)
        print('Son')
        self.name = name
        self.age = age

    def setInfo(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print('学习ing')

    def father_work(self):
        # Father.work(self)
        super().work()

    def mather_work(self):
        # Mather.work(self)
        super().work()


s1 = Son('小明', 18)
s1.work()
# print(s1.name)
s1.sayHello()
s1.work()
s1.setInfo('小红', 16)
s1.sayHello()

s1.father_work()
s1.mather_work()

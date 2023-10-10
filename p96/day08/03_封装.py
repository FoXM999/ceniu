# Author:zqbin
# @Time:2023/9/18 14:21
# @Author:14988
# @Site:
# @File:03_封装.py
# @Software:PyCharm


class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age = age

    def __hello(self):
        print('hello')

    def hello(self):
        self.__hello()


s1 = Student('张三',18)
print(s1.name)
# print(s1.__age)
print(s1.getAge())
s1.setAge(30)
print(s1.getAge())

# print(s1.__hello())
s1.hello()


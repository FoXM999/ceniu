# Author:zqbin
# @Time:2023/9/18 15:58
# @Author:14988
# @Site:
# @File:05_类属性_类方法.py
# @Software:PyCharm

## 类属性

# 实例属性： 属于实例对象的， 在init魔术方法当中进行初始化
# 类属性： 属于类对象的， 直接定义在类下面的变量


class People(object):
    nationality = "China"  # 类属性
    __test = "123"

    def __init__(self):
        self.name = "张三"
        self.__age = 20

    def method(self):
        print(self.nationality)
        print(People.nationality)
        print(self.__test)
        print(People.__test)


p = People()

# 访问类属性，可以使用 类对象.属性名称   实例对象.属性名称
print(People.nationality)
print(p.nationality)

# 修改实例属性，只能使用       类对象.属性名称 = 属性值
People.nationality = "USA"
print(People.nationality)
print(p.nationality)

# 如果使用 实例对象.属性名称=属性值，不是修改类属性，而是新增一个同名的实例属性
p.nationality = "China"
print(People.nationality)  # USA
print(p.nationality)  # China

# 类属性也有访问权限的控制
# print(People.__test) # AttributeError: type object 'People' has no attribute '__test'

p.method()

## 方法

### 实例方法： 属于实例对象，第一个参数时  self，代表实例对象自生

### 类方法： 属于类对象 ，第一个参数是 cls，代表类对象自身

# 方法上面添加了 @ classmethod

### 静态方法： 不属于实例对象，也不属于类对象，纯粹的知识一个写在类当中的函数 ，没有额外的参数


# 方法上面添加 @ staticmethod


class Demo(object):

    def test_method(self):
        print(self)

    @classmethod
    def method_02(cls):
        print(cls)

    @staticmethod
    def func():
        print("xxx")


# 实例对象和类对象都可以调用类方法
d = Demo()
d.method_02()
Demo.method_02()

# 实例对象和类对象都可以调用静态方法
d.func()
Demo.func()

#  实例对象和类对象都可以调用实例方法
d.test_method()
Demo.test_method(d)
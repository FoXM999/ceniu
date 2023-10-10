# Author:zqbin
# @Time:2023/9/18 11:30
# @Author:14988
# @Site:
# @File:02.py
# @Software:PyCharm

# ## 课堂练习
# 定义一个分数类: FractionalNumber
# 实例化的时候可以传入2个参数，或者1个参数
# 如果传入2个参数，分别代表 分子 和 分母
# 如果传入1个参数，代表分子， 此时 分母默认为1
# 暂时不考虑分母为0的异常情况

class FractionalNumber(object):

    def __init__(self, mol, deno=1):
        # 初始化3个实例属性： 分子， 分母  和 符号
        if mol / deno >= 0:
            self.sign = True
        else:
            self.sign = False

        self.mol = abs(mol)
        self.deno = abs(deno)

    def jian(self, x, y):
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x

    def __str__(self):
        if self.mol == 0:
            return '0'
        if self.deno == 1:
            return str(int(self.mol/self.deno))

        self.gys = self.jian(self.mol, self.deno)
        mol = int(self.mol / self.gys)
        deno = int(self.deno / self.gys)
        if self.sign:
            return '%s/%s' % (mol, deno)
        else:
            return '-%s/%s' % (mol, deno)


print(FractionalNumber(3, 2))  # 3/2
print(FractionalNumber(-3, 2))  # -3/2
print(FractionalNumber(3, -2))  # -3/2
print(FractionalNumber(-3, -2))  # 3/2
print(FractionalNumber(9, 6))  # 3/2
print(FractionalNumber(3))  # 3
print(FractionalNumber(0, 2))  # 0

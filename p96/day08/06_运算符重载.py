# Author:zqbin
# @Time:2023/9/18 16:15
# @Author:14988
# @Site:
# @File:06_运算符重载.py
# @Software:PyCharm

class e(Exception):
    def __init__(self, msg):
        self.msg = msg

class FractionalNumber(object):

    def __init__(self, mol, deno=1):

        if deno == 0:
            raise e('分数的分母不能为0')

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
            return str(int(self.mol / self.deno))

        if self.mol == self.deno:
            if self.sign:
                return '1'
            else:
                return '-1'

        self.gys = self.jian(self.mol, self.deno)
        mol = int(self.mol / self.gys)
        deno = int(self.deno / self.gys)
        if self.sign:
            return '%s/%s' % (mol, deno)
        else:
            return '-%s/%s' % (mol, deno)

    def __mul__(self, other):
        if self.sign == other.sign:
            return FractionalNumber(self.mol * other.mol, self.deno * other.deno)
        else:
            return FractionalNumber(-self.mol * other.mol, self.deno * other.deno)

    def __truediv__(self, other):
        if self.sign == other.sign:
            return FractionalNumber(self.mol * other.deno, self.deno * other.mol)
        else:
            return FractionalNumber(-self.mol * other.deno, self.deno * other.mol)

    def __add__(self, other):
        if self.sign == other.sign:
            mol = self.mol * other.deno + self.deno * other.mol
            deno = self.deno * other.deno

            if self.sign:
                return FractionalNumber(mol, deno)
            else:
                return FractionalNumber(-mol, deno)
        else:
            if self.sign:
                if self.mol / self.deno > other.mol / other.deno:
                    return FractionalNumber(self.mol * other.deno - self.deno * other.mol, self.deno * other.deno)
                else:
                    return FractionalNumber(self.deno * other.mol - self.mol * other.deno, -self.deno * other.deno)
            else:
                if self.mol / self.deno > other.mol / other.deno:
                    return FractionalNumber(self.mol * other.deno - self.deno * other.mol, -self.deno * other.deno)
                else:
                    return FractionalNumber(self.deno * other.mol - self.mol * other.deno, self.deno * other.deno)

    def __sub__(self, other):
        other.sign = not other.sign
        return FractionalNumber.__add__(self, other)

    def __lt__(self, other):
        result = str(FractionalNumber.__sub__(self, other))
        if result[0] == '-':
            return True
        return False

    def __le__(self, other):
        result = str(FractionalNumber.__sub__(self, other))
        if result[0] == '-' or result[0] == '0':
            return True
        return False

    def __gt__(self, other):
        return not FractionalNumber.__le__(self, other)

    def __ge__(self, other):
        return not FractionalNumber.__lt__(self, other)

    def __eq__(self, other):
        result = str(FractionalNumber.__sub__(self, other))
        if result[0] == '0':
            return True
        return False

    def __ne__(self, other):
        return not FractionalNumber.__eq__(self, other)


# print(FractionalNumber(3, 2))  # 3/2
# print(FractionalNumber(-3, 2))  # -3/2
# print(FractionalNumber(3, -2))  # -3/2
# print(FractionalNumber(-3, -2))  # 3/2
# print(FractionalNumber(9, 6))  # 3/2
# print(FractionalNumber(3))  # 3
# print(FractionalNumber(0, 2))  # 0
#
# print(FractionalNumber(3,3))
#
# print('='*100)
# f1 = FractionalNumber(-7, 3)
# f2 = FractionalNumber(3, 4)
# print(f1 * f2)
#
# print('='*100)
# f1 = FractionalNumber(0, 3)
# f2 = FractionalNumber(1, -3)
# print(f1 / f2)
#
# print('='*100)
# f1 = FractionalNumber(0, 4)
# f2 = FractionalNumber(1, 4)
# print(f1 + f2)
#
# print('='*100)
# f1 = FractionalNumber(0, 4)
# f2 = FractionalNumber(1, 4)
# print(f1 - f2)

# print('='*100)
# f1 = FractionalNumber(-2, 4)
# f2 = FractionalNumber(-3, 4)
# print(f1 < f2)

# print('='*100)
# f1 = FractionalNumber(-2, 4)
# f2 = FractionalNumber(-3, 4)
# print(f1 <= f2)

# print('='*100)
# f1 = FractionalNumber(-2, 4)
# f2 = FractionalNumber(-1, 4)
# print(f1 > f2)

# print('='*100)
# f1 = FractionalNumber(2, 4)
# f2 = FractionalNumber(-1, 4)
# print(f1 == f2)

print('=' * 100)
f1 = FractionalNumber(-2, 4)
f2 = FractionalNumber(-1, 0)
print(f1 != f2)

# Author:zqbin
# @Time:2023/9/8 14:14
# @Author:14988
# @Site:
# @File:04.py
# @Software:PyCharm
import random

# a = random.randint(0,2)
a = int(input('请输入0-2'))
b = random.randint(0,2)

if a == 0:
    aa = '剪刀'
elif a == 1:
    aa = '石头'
else:
    aa = '布'
if b == 0:
    bb = '剪刀'
elif b == 1:
    bb = '石头'
else:
    bb = '布'
print(f'玩家出的是：{aa}，电脑出的是：{bb}')

if a == b:
    print('平局')
elif (a == 2 and b == 1) \
        or (a == 1 and b == 0) \
        or (a == 0 and b == 2):
    print('玩家获胜')
else:
    print('电脑获胜')
# Author:zqbin
# @Time:2023/9/12 10:31
# @Author:14988
# @Site:
# @File:02.py
# @Software:PyCharm


# Author:zqbin
# @Time:2023/9/11 15:08
# @Author:14988
# @Site:
# @File:11.py
# @Software:PyCharm

import random

awin = 0
bwin = 0
info = ('剪刀', '石头', '布')
while True:
    print('=' * 50)
    a = input('（0-剪刀,1-石头,2-布）请输入：')
    if a not in ('1', '2', '3'):
        print('请输入正确的数字')
        continue
    a = int(a)
    b = random.randint(0, 2)

    print(f'玩家出的是：{info[a]}，电脑出的是：{info[b]}')

    if a == b:
        print('平局')
    elif (a == 2 and b == 1) \
            or (a == 1 and b == 0) \
            or (a == 0 and b == 2):
        awin += 1
        print(f'玩家获胜！玩家赢了{awin}局，电脑赢了{bwin}局')
    else:
        bwin += 1
        print(f'电脑获胜！玩家赢了{awin}局，电脑赢了{bwin}局')

    if awin == 7 or bwin == 7:
        print('游戏结束')
        break

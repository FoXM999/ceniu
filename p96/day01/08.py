# Author:zqbin
# @Time:2023/9/8 16:44
# @Author:14988
# @Site:
# @File:08.py
# @Software:PyCharm

# - 输入某年某月某日（分3次输入），打印这一天是这一年的第几天。
year = int(input('请输入年：'))
month = int(input('请输入月：'))
day = int(input('请输入日：'))

run = False
count = 0
monthday = [31,28,31,30,31,30,31,31,30,31,30,31]

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    run = True
if run:
    monthday[1] = 29
i = 0
while i < month - 1:
    count += monthday[i]
    i += 1
print(f'{year}-{month}-{day} 为{year}年的第{count + day}天')


# - 输入3个数x,y,z，请把这三个数由小到大输出。
a = int(input('请输入第1个数：'))
b = int(input('请输入第2个数：'))
c = int(input('请输入第3个数：'))
lt = [a, b, c]
lt.sort()
print(lt)

# - 有1，2，3，4四个数字，能够组成多少个互不相同且无重复数字的三位数？都是多少
lt = []
count = 0
for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if j == k or i == k:
                continue
            lt.append(i*100 + j*10 + k)
            count += 1
print(lt)
print(count)

# - 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第3个月后又生一对兔子，假如兔子都不死，问第n个月的兔子总数为多少，n从键盘输入
month = int(input('请输入：'))
if month == 1 or month == 2:
    print(f'第{month}个月的兔子总数为：1')
i = 3
a = 1
b = 1
while i <= month:
    t = a
    a = b
    b = t + b
    i += 1
print(f'第{month}个月的兔子总数为：{b}')

# - 一个数如果恰好等于它的因子之和，这个数就是“完数”。例如6=1+2+3，打印1000以内的所有完数
i = 2
while i <= 1000:
    j = 1
    count = 0
    while j < i:
        if i % j == 0:
            count += j
        j += 1
    if count == i:
        print(i)
    i += 1

# - 一个球从100米高度自由落下，每次落地后反弹原高度的一半；再落下，求它再第10次落地时，共经历了多少米？第10次反弹多高？
i = 1
count = 0
height = 100
while i <= 10:
    count += height
    height /= 2
    i += 1
print(f'第{i-1}次落地时共经历了：{count}，第10次反弹 {height} 米')

# - 求1+2!+3!+...+20!的和
i = 1
count = 0
while i <= 20:
    j = 1
    count2 = 1
    while j <= i:
        count2 *= j
        j += 1
    count += count2
    i += 1
print(count)

# - 将课堂练习剪刀石头布，改为谁先赢7局，游戏结束。
import random

awin = 0
bwin = 0
while True:
    print('=' * 50)
    a = int(input('（0-剪刀,1-石头,2-布）请输入：'))
    b = random.randint(0, 2)

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
        awin += 1
        print(f'玩家获胜！玩家赢了{awin}局，电脑赢了{bwin}局')
    else:
        bwin += 1
        print(f'电脑获胜！玩家赢了{awin}局，电脑赢了{bwin}局')

    if awin == 7 or bwin == 7:
        print('游戏结束')
        break

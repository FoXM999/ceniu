# Author:zqbin
# @Time:2023/9/11 14:18
# @Author:14988
# @Site:
# @File:10.py
# @Software:PyCharm

for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    # print(a,b,c)
    if (a ** 3 + b ** 3 + c ** 3) == i:
        print(i)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d x %d = %-4d' % (j, i, i * j), end='')
    print()

isSuShu = True
for i in range(2, 11):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

result = 0
for i in range(1, 21):
    tmp = 1
    for j in range(1, i + 1):
        tmp *= j
    result += tmp
    tmp = 1
print(result)

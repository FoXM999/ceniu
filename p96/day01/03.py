# Author:zqbin
# @Time:2023/9/8 11:59
# @Author:14988
# @Site:
# @File:03.py
# @Software:PyCharm


score = 1
while (score):
    score = input('请输入分数：')
    if score == 'exit':
        print('程序结束运行')
        break
    score = int(score)
    if score > 100 or score < 0:
        print('请输入正确的分数！')
        continue
    if 90 <= score <= 100:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('E')

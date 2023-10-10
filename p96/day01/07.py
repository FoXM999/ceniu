# Author:zqbin
# @Time:2023/9/8 16:20
# @Author:14988
# @Site:
# @File:07.py
# @Software:PyCharm

# i = 2
# count = 0
# while i <= 100:
#     if i == 2:
#         print('2')
#         i += 1
#         count += 1
#         continue
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         print(i)
#         count += 1
#     i += 1
#
# print(f'count={count}')

# for i in range(2, 11):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

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

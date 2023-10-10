# Author:zqbin
# @Time:2023/9/8 15:34
# @Author:14988
# @Site:
# @File:06.py
# @Software:PyCharm

# i = 1
# j = 1
# while i < 5:
#     while j <= i:
#         print('*',end='')
#         j += 1
#     print()
#     i += 1
#     j = 1

# for i in range(1,5):
#     for j in range(1,5):
#         if j <= i:
#             print('*',end='')
#     print()

# i = 1
# j = 1
# while i < 10:
#     while j <= i:
#         # print(f'{i} x {j} = {j*i}', end='')
#         print('%d x %d = %-5d' % (j, i, j * i), end='')
#         j += 1
#     i += 1
#     j = 1
#     print()

for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print('%d x %d = %-5d' % (j, i, j * i), end='')
    print()
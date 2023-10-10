# Author:zqbin
# @Time:2023/9/12 15:15
# @Author:14988
# @Site:
# @File:07.py
# @Software:PyCharm

lst = [1, 3, 9, 2, 0, -9, 4]
# lst = [-9, 0, 1, 2, 4, 9, 3]
count = 0
for i in range(len(lst) - 1):
    flag = True
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            # t = lst[j]
            # lst[j] = lst[j + 1]
            # lst[j + 1] = t
            lst[j], lst[j+1] = lst[j+1],lst[j]
            flag = False
        count += 1
    if flag:
        break

print(lst)
print(count)

# Author:zqbin
# @Time:2023/9/13 16:13
# @Author:14988
# @Site:
# @File:06.py
# @Software:PyCharm

l1 = [1, 3, 9, 2, 0, -9, 4]

for i in range(len(l1)-1):
    xb = i
    for j in range(i, len(l1)):
        if l1[j] < l1[xb]:
            xb = j
    l1[i], l1[xb] = l1[xb], l1[i]

print(l1)

# Author:zqbin
# @Time:2023/9/13 16:46
# @Author:14988
# @Site:
# @File:07.py
# @Software:PyCharm
import copy

l1 = [1,2,[1,2]]
l2 = l1.copy()
l3 = l1
# print(l2)
# l2.append(3)
# print(l1)
# print(l2)
# print(l3)

l2[2].append(3)
print(l2)
print(l1)

l4 = copy.deepcopy(l1)

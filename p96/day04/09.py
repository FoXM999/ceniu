# Author:zqbin
# @Time:2023/9/12 17:11
# @Author:14988
# @Site:
# @File:09.py
# @Software:PyCharm


# l1 = [1, 2, 3, [1, 2], 2, [1, 2], 3, 4]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print('l2=',l2)

# l3 = [l1[i] for i in range(len(l1)) if l1[i] not in l1[:i]]
# print('l3=', l3)

# print(l1[i+1:])

l1 = [1, 2, 3, [1, 2], 2, [1, 2], 3, 4]

l3 = [l1[i] for i in range(len(l1)) if l1[i] not in l1[:i]]
print('l3=', l3)

l4 = set()
for i in l1:
    l4.add(i)
print(l4)
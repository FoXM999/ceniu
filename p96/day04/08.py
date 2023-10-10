# Author:zqbin
# @Time:2023/9/12 15:48
# @Author:14988
# @Site:
# @File:08.py
# @Software:PyCharm


lst = [i ** 2 for i in range(1, 11)]
print(lst)

lst2 = [i for i in range(1, 11) if i % 2 == 0]
print(lst2)

l5 = [1, 2, 3]
l6 = [3, 1, 4]
l7 = [(i, j) for i in l5 for j in l6 if i != j]
print(l7)

t1 = (1, 2, 3, 4, 5)
t2 = (100, 200, 300)
length = len(t1) if len(t1) < len(t2) else len(t2)
ret = [(t1[i], t2[i]) for i in range(length)]
print(ret)

l1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# l2 = [
#     [1, 5, 9],
#     [2, 6, 10],
#     [3, 7, 11],
#     [4, 8, 12]
# ]
l2 = []
for i in range(len(l1[0])):
    tmp = []
    for item in l1:
        tmp.append(item[i])
    l2.append(tmp)
print('l2=', l2)

l4 = [[item[i] for item in l1] for i in range(len(l1[0]))]
print('l4:', l4)

print([item[0] for item in l1])
print([item[1] for item in l1])
print([item[2] for item in l1])
print([item[3] for item in l1])
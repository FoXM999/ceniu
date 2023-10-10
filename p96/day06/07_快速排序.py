# Author:zqbin
# @Time:2023/9/14 15:49
# @Author:14988
# @Site:
# @File:07_快速排序.py
# @Software:PyCharm

l1 = [1, 3, 9, 2, 0, -9, 4]


# def kp(lst, start, end):
#     if end <= start:
#         return
#     index = start
#     for i in range(start, end):
#         if lst[i] < lst[index]:
#             tmp = lst.pop(i)
#             lst.insert(index, tmp)
#             index += 1
#     kp(lst, 0, index-1)
#     kp(lst, index+1, end)
#
#
# #
# #

# kp(l1, 0, len(l1))
# print(l1)


def quick_sort(lst):
    if len(lst) < 2:
        return lst
    left, right = [], []
    for i in range(1, len(lst)):
        if lst[i] < lst[0]:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return quick_sort(left) + [lst[0]] + quick_sort(right)


print(quick_sort(l1))

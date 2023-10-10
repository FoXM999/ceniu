# Author:zqbin
# @Time:2023/9/15 11:33
# @Author:14988
# @Site:
# @File:03_冒泡排序.py
# @Software:PyCharm
import copy


# lst = [1, 3, 9, 2, 0, -9, 4]
# # lst = [-9, 0, 1, 2, 4, 9, 3]
# count = 0
# for i in range(len(lst) - 1):
#     flag = True
#     for j in range(len(lst) - 1 - i):
#         if lst[j] > lst[j + 1]:
#             # t = lst[j]
#             # lst[j] = lst[j + 1]
#             # lst[j + 1] = t
#             lst[j], lst[j+1] = lst[j+1],lst[j]
#             flag = False
#         count += 1
#     if flag:
#         break
#
# print(lst)
# print(count)


# def bubbling_sorted(iterable, *, key=None, reverse=False):
#     """
#     通过冒泡排序算法，实现对iterable参数进行排序，返回排好序的列表
#     :param iterable: 待排序的可迭代对象
#     :param key: 具有一个参数的函数对象，用于从排序对象中的没个元素中提取用于比较的键，
#                 默认值为None,直接通过元素自身进行比较
#     :param reverser: bool类型值，默认值为Fales，表示从小到大排序，
#                      如果设置为True，表示从大到小排序
#     :return: 排好序的列表
#     """
#     lst = list(iterable)
#     for i in range(1, len(lst) - 1):
#         flag = True
#         for j in range(len(lst) - i):
#             if key is None:
#                 if lst[j] > lst[j + 1]:
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                     flag = False
#             else:
#                 if key(lst[j]) > key(lst[j + 1]):
#                     lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                     flag = False
#         if flag:
#             break
#     if reverse:
#         lst.reverse()
#     return lst
#
#
# students = [
#     {"name": "zhangsan", "age": 18, "class": "2班", "height": 178.5},
#     {"name": "lisi", "age": 19, "class": "1班", "height": 188.5},
#     {"name": "wangwu", "age": 20, "class": "3班", "height": 168.5}
# ]
#
# print(bubbling_sorted(students, key=lambda x: x.get("height"), reverse=True))


def bubbling_sorted(iterable, *, key=None, reverse=False):
    """
    通过冒泡排序算法，实现对iterable参数进行排序，返回排好序的列表
    :param iterable: 待排序的可迭代对象
    :param key: 具有一个参数的函数对象，用于从排序对象中的没个元素中提取用于比较的键，
                默认值为None,直接通过元素自身进行比较
    :param reverse: bool类型值，默认值为False，表示从小到大排序，
                     如果设置为True，表示从大到小排序
    :return: 排好序的列表
    """
    # 1. 将可迭代对象转换成列表
    result = list(iterable)
    # 2. 循环len()-1次
    for i in range(1, len(result)):
        # 3. 循环len()-i次
        for j in range(len(result)-i):
            # 4. 判断key, 如果 key is None, 则拿相邻的两个元素直接比较
            if key is None:
                if result[j] > result[j+1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
            # 5. 如果 key is not None,将相邻的两个元素作为参数来调用key对应的函数对象，对返回结果进行比较
            else:
                if key(result[j]) > key(result[j+1]):
                    result[j], result[j + 1] = result[j + 1], result[j]
    # 6. 判断reverser,如果为True，则倒序
    if reverse:
        result.reverse()
    # 7. 返回排好序的列表
    return result


students = [
    {"name": "zhangsan", "age": 18, "class": "2班", "height": 178.5},
    {"name": "lisi", "age": 19, "class": "1班", "height": 188.5},
    {"name": "wangwu", "age": 20, "class": "3班", "height": 168.5}
]

print(bubbling_sorted(students, key=lambda x: x.get("height"), reverse=True))
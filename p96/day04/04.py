# Author:zqbin
# @Time:2023/9/12 11:57
# @Author:14988
# @Site:
# @File:04.py
# @Software:PyCharm

l1 = [1, 2, 3, 4, 5]

print(l1[0])
l1[0] = 100
print(l1)   # [100, 2, 3, 4, 5]
l1[-1] = 500
print(l1)   # [100, 2, 3, 4, 500]

# 通过切片来修改列表元素的值是，赋值的必须是一个可迭代对象
# l1[1:2] = 200   # TypeError: can only assign an iterable
print(l1[1:2])  # [2]
l1[1:2] = [200]
print(l1)   # [100, 200, 3, 4, 500]

# 当切片步长为1的时候，切片结果的长度，可以和赋值的可迭代对象的长度不一致
l1[2:3] = [300, 350]
print(l1)   # [100, 200, 300, 350, 4, 500]

l1[2:5] = [1000]
print(l1)   # [100, 200, 1000, 500]

l1[2:3] = "abc"     # [100, 200, 'a', 'b', 'c', 500]
print(l1)   # [100, 200, 'a', 'b', 'c', 500]


# 当切片的步长不为1时，切片结果的长度必须和赋值的可迭代对象的长度保持一致
# ValueError: attempt to assign sequence of size 2 to extended slice of size 3
# l1[::2] = (1, 2)
l1[::2] = (1, 2, 3)
print(l1)   # [1, 200, 2, 'b', 3, 500]
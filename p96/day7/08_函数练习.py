# Author:zqbin
# @Time:2023/9/16 17:10
# @Author:14988
# @Site:
# @File:08_函数练习.py
# @Software:PyCharm

# 汉诺塔
# def han(n,start='A',helper='B',target='C'):
#     if n==1:
#         print(f'{start} -> {target}')
#     else:
#         han(n-1,start=start,helper=target,target=helper)
#         print(f'{start} -> {target}')
#         han(n-1,start=helper,helper=start,target=target)
#
# han(2)
# print('='*50)
# han(3)
# print('='*50)
# han(4)

l1 = [1, 3, 9, 2, 0, -9, 4]

# 快速排序
# def quick(lst):
#     if len(lst) < 2:
#         return lst
#     mid = lst[0]
#     left, right = [], []
#     for i in range(1,len(lst)):
#         if lst[i] < mid:
#             left.append(lst[i])
#         else:
#             right.append(lst[i])
#     return quick(left) + [mid] + quick(right)
#
#
# print(quick(l1))

# 插入排序
# def insert_sort(lst:list):
#     new_lst = list(lst)
#     for i in range(1,len(l1)):
#         value = new_lst.pop(i)
#         for j in range(i-1,-1,-1):
#             if new_lst[j] < value:
#                 new_lst.insert(j+1,value)
#                 break
#         else:
#             new_lst.insert(0,value)
#     return new_lst
# print(insert_sort(l1))


# 选择排序
# def chose_sort(lst:list):
#     new_lst = list(lst)
#     for i in range(len(new_lst)-1):
#         index = i
#         for j in range(i+1,len(new_lst)):
#             if new_lst[j] < new_lst[index]:
#                 index = j
#         new_lst[i], new_lst[index] = new_lst[index], new_lst[i]
#     return new_lst
#
# print(chose_sort(l1))


# def f1(a,b,/,c,d):
#     print(a+b+c+d)
#
# def f2(a,b,*,c,d):
#     print(a + b + c + d)
#
# f2(1,2,c=3,d=4)


# 辗转相除法
# def chu(x,y):
#     m = max(x,y)
#     n = min(x,y)
#     r = m % n
#     while r != 0:
#         m = n
#         n = r
#         r = m % n
#     return n
#
# print(chu(30,48))


# 辗转相减法
# def jian(x,y):
#     while x != y:
#         if x > y:
#             x -= y
#         else:
#             y -= x
#     return x
#
# print(jian(30,48))


# 一般方法
# def normal(x,y):
#     for i in range(min(x,y),0,-1):
#         if x % i == 0 and y % i == 0:
#             return i
#
# print(normal(7,3))


l2 = [1, 2, 3, [1, 2], 2, [1, 2], 3, 4, 5]

# l3 = [l2[i] for i in range(len(l2)) if l2[i] not in l2[:i]]
# print(l3)
# l3 = []
# for i in range(len(l2)):
#     if l2.index(l2[i]) == i:
#         l3.append(l2[i])
# print(l3)

# l4 = [l2[i] for i in range(len(l2)) if l2.index(l2[i]) == i]
# print(l4)

t1 = (1,2,3)
print(1 in t1)

lst2 = []
lst2.pop()
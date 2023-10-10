# Author:zqbin
# @Time:2023/9/13 23:08
# @Author:14988
# @Site:
# @File:08.py
# @Software:PyCharm


# l1 = [1, 3, 9, 2, 0, -9, 4]

# for i in range(len(l1)-1):
#     for j in range(0,len(l1)-1):
#         if l1[j] > l1[j+1]:
#             l1[j],l1[j+1] = l1[j+1],l1[j]
# print(l1)

# for i in range(1,len(l1)):
#     temp = l1.pop(i)
#     for j in range(i-1, -1, -1):
#         if temp >= l1[j]:
#             l1.insert(j+1, temp)
#             break
#     else:
#         l1.insert(0, temp)
# print(l1)

# for i in range(len(l1)-1):
#     lstIndex = i
#     for j in range(i,len(l1)):
#         if l1[j] < l1[lstIndex]:
#             lstIndex = j
#     l1[i],l1[lstIndex] = l1[lstIndex],l1[i]
# print(l1)

# s1 = {1,2,3,4,5}
# for item in s1:
#     print(item)
# s1.add(6)
# s1.remove(6)
# s1.discard(6)
# s1.clear()
# s1.pop()
# print(s1)

# l1 = ['name', 'age', 'sex']
# l2 = ['zhangsan', 18, '未知']
# d1 = dict(zip(l1, l2))
# print(d1)
#
# d2 = dict([('fname', 'li'), ('lname', 'hua')])
# print(d2)
#
# d3 = dict([(item1, item2) for index1, item1 in enumerate(l1) for index2, item2 in enumerate(l2) if index1 == index2])
# print(d3)
#
# d4 = {'name': 'zhangsan', 'age': 18, 'sex': '未知'}
# print(d4['name'])
# del d4['name']
# print(d4)
# print(d4.pop('age'))
# print(d4)
# print(d4.pop('age', None))
# print(d4)
#
# print(d4['sex'])
# print(d4.get('age'))
# print(d4.get('sex'))
#
# d4['address'] = '广西'
# print(d4)
# d4['address'] = '南宁'
# print(d4)
#
# d4.update({'address': '广州','hobby':['喝酒','抽烟','烫头']})
# print(d4)
#
# print(d4.popitem())
# print(d4)
#
# for i in d4.items():
#     print(i)

# t1 = tuple([1,2,3])
# print(t1)
# t2 = (1,)
# print(t2)
# t3 = (1,2,3,4,5)
# print(t3[0:3])
#
# for i in enumerate(t3):
#     print(i)

l1 = [1, 2, 3, 4, 5]
l2 = [10, 11, 12]
l1.append(6)
print(l1)
l1.insert(1, 1.5)
print(l1)
l1.extend(l2)
print(l1)

del l1[1]
print(l1)
l1.pop()
print(l1)
print(l1.pop(1))
print(l1)
print(l1.remove(4))
print(l1)
l1.reverse()
print(l1)

l2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
l3 = [[l2[j][i] for j in range(len(l2))] for i in range(len(l2[0]))]
print(l3)
l4 = []
for i in range(len(l2[0])):
    temp = []
    for j in range(len(l2)):
        temp.append(l2[j][i])
    l4.append(temp)
print(l4)

# l2 = list('hello')
# print(l2)

# s = ''.join(l2)
# print(s)
#
# s1 = '''he
# is
# my
# love'''
# print(s1.splitlines())
# s2 = 'he is my love'
# print(s2.partition(' '))


print(bin(10))

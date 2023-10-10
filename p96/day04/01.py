# Author:zqbin
# @Time:2023/9/12 10:09
# @Author:14988
# @Site:
# @File:01.py
# @Software:PyCharm

t1 = (100)
print(t1 ,type(t1))

t2 = (100,)
print(t2 ,type(t2))

t3 = 1,2,3,4,5
print(t3,type(t3))

t4 = tuple([1,2,3])
print(t4)

t5 = tuple('hello')
print(t5)
print(t5)
print(t5)

t6 = (1,2,3)
print(t6 + (4,5,6))
print(t6 * 2)

print(t6[1])
t6 = (4,5,6)
print(t6)

t7 = ('a','b')
print(max(t7))

print(t6.count(4))
print(3 in t6)
print(3 not in t6)
print(t6.index(5))

print('分割线'.center(50,'='))
for i in t6:
    print(i)
for index,item in enumerate(t6):
    print(f'{index}--{item}')




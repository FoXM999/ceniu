# Author:zqbin
# @Time:2023/9/12 11:14
# @Author:14988
# @Site:
# @File:03.py
# @Software:PyCharm


a = ['a','b','c']
print(''.join(a))

print(list('abc'))

a2 = '''tom
age
lili'''
print(a2.splitlines())

a3 = 'a_b_c'
print(a3.split('_'))
print(a3.rpartition('_'))

print('='*50)
lst = [1,2,3,4,5]
lst[1:2] = [200]
print(lst)
lst[2:3] = [300,350]
print(lst)
lst[1:5] = [1000]
print(lst)

# lst[2:3] = 'abc'
# print(lst)
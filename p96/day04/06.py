# Author:zqbin
# @Time:2023/9/12 14:32
# @Author:14988
# @Site:
# @File:06.py
# @Software:PyCharm

lst = [1,2,3,4,5,6]
print(lst)

# del lst
# print(lst)

print(lst.pop())
print(lst)

lst.remove(4)
print(lst)

lst.clear()
print(lst)

s = input('请输入：')
lst = list(s)
while 'a' in lst:
    lst.remove('a')
print(''.join(lst))

s = input('请输入：')
print(s.replace('a', ''))

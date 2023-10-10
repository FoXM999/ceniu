# Author:zqbin
# @Time:2023/9/13 14:17
# @Author:14988
# @Site:
# @File:03.py
# @Software:PyCharm

l1 = ['one','two','three']
l2 = [1,2,3,4]
print(dict(zip(l1,l2)))
d = dict([(l1[i],l2[i]) for i in range(len(l1))])
print(d)
d2 = {item1:item2 for i,item1 in enumerate(l1) for j,item2 in enumerate(l2) if i==j}
print('d2=',d2)


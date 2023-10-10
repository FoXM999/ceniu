# Author:zqbin
# @Time:2023/9/13 15:19
# @Author:14988
# @Site:
# @File:mytestcase.py
# @Software:PyCharm

l1 = [1, 3, 9, 2, 0, -9, 4]

for i in range(1,len(l1)):
    temp = l1.pop(i)
    for j in range(i-1,-1,-1):
        if temp >= l1[j]:
            l1.insert(j+1,temp)
            break
    else:
        l1.insert(0,temp)

print(l1)

# for i in range(1,len(l1)):
#     for j in range(i,-1,-1):
#         print(j)
#     break



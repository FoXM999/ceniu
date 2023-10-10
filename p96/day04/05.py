# Author:zqbin
# @Time:2023/9/12 14:05
# @Author:14988
# @Site:
# @File:mytestcase.py
# @Software:PyCharm

l1 = [1, 2, 3, 4, 5]

l1.append(6)
print(l1)       # [1, 2, 3, 4, 5, 6]

l1.append([7, 8])
print(l1)       # [1, 2, 3, 4, 5, 6, [7, 8]]

# l1.extend(9)    # TypeError: 'int' object is not iterable
l1.extend([9, 10])
print(l1)       # [1, 2, 3, 4, 5, 6, [7, 8], 9, 10]

l1.append("ab")
print(l1)    # [1, 2, 3, 4, 5, 6, [7, 8], 9, 10, 'ab']
l1.extend("ab")
print(l1)    # [1, 2, 3, 4, 5, 6, [7, 8], 9, 10, 'ab', 'a', 'b']

l1.insert(0, 0.0)
print(l1)    # [0.0, 1, 2, 3, 4, 5, 6, [7, 8], 9, 10, 'ab', 'a', 'b']

l1.insert(len(l1), 90)  # l1.append(90)
print(l1)    # [0.0, 1, 2, 3, 4, 5, 6, [7, 8], 9, 10, 'ab', 'a', 'b', 90]

l1.insert(7, 6.5)
print(l1)    # [0.0, 1, 2, 3, 4, 5, 6, 6.5, [7, 8], 9, 10, 'ab', 'a', 'b', 90]
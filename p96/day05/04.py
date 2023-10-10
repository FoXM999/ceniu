# Author:zqbin
# @Time:2023/9/13 14:40
# @Author:14988
# @Site:
# @File:04.py
# @Software:PyCharm


d1 = {"name": "Tom", "age": 30, "height": 175.5}
print(d1, type(d1))

print(d1["age"])
print(d1.get("age"))

# print(d1["id"])  # KeyError: 'id'
print(d1.get("id"))  # None

d1["age"] = 28
print(d1)
d1["id"] = 1
print(d1)

d1.update(dict([('height',180), ('sex','男')]))
print(d1)

del d1['name']
print(d1)

print(d1.pop('age'))
print(d1)

print(d1.pop('age',None))
print(d1)

print(d1.popitem())
print(d1)

# d1.clear()
# print(d1)

print(list(d1.values()))
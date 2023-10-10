# Author:zqbin
# @Time:2023/9/14 10:52
# @Author:14988
# @Site:
# @File:02.py
# @Software:PyCharm

def my_bin(num):
    # if num == 0:
    #     return 0
    temp = []
    while True:
        temp.append(str(num % 2))
        num //= 2
        if num == 0:
            break
    return ''.join(temp[::-1])


print(my_bin(0))

print(bin(0))

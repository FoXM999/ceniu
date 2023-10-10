# Author:zqbin
# @Time:2023/9/19 10:07
# @Author:14988
# @Site:
# @File:01_异常.py
# @Software:PyCharm
import traceback

try:
    print('start')
    # print(4/0)
    # raise ValueError('手动抛出异常')
    num1,num2 = 1, 2
    assert num1==num2,'实际结果:'+str(num1)+' != 预期结果:'+str(num2)
    print('end')
except ZeroDivisionError as e:
    print(e)
    traceback.print_exc()

print('运行结束')
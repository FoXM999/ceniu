# Author:zqbin
# @Time:2023/10/10 14:34
# @Author:14988
# @Site:
# @File:runner.py
# @Software:PyCharm
import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./result -c -o ./report')
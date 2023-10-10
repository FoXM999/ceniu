# Author:zqbin
# @Time:2023/10/10 10:27
# @Author:14988
# @Site:
# @File:demo01_test.py
# @Software:PyCharm
import pytest


class TestClass:
    @pytest.mark.smoke
    def test_method01(self):
        print('test_method01')
        assert 1 == 2, '1!=2'

    @pytest.mark.regression
    def test_method02(self):
        print('test_method02')
        assert 1 == 2, '1!=2'


@pytest.mark.smoke
@pytest.mark.regression
def test_func():
    print('test_func')
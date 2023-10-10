# Author:zqbin
# @Time:2023/10/10 14:09
# @Author:14988
# @Site:
# @File:demo03_login_test.py
# @Software:PyCharm
import pytest
from selenium import webdriver


@pytest.fixture
def setUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

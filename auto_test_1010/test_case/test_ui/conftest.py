# Author:zqbin
# @Time:2023/10/10 15:21
# @Author:14988
# @Site:
# @File:conftest.py
# @Software:PyCharm
import pytest
from selenium import webdriver


@pytest.fixture
def webdriver_fixture():
    print("\nsetup")
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # teardown
    print("\nteardown")
    driver.close()
    driver.quit()

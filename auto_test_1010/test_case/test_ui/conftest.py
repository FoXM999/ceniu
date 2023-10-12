# Author:zqbin
# @Time:2023/10/10 15:21
# @Author:14988
# @Site:
# @File:conftest.py
# @Software:PyCharm
import time

import allure
import pytest
from selenium import webdriver


driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global driver

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        time.sleep(0.5)
        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

@pytest.fixture
def webdriver_fixture():
    global driver

    print("\nsetup")
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # teardown
    print("\nteardown")
    driver.close()
    driver.quit()

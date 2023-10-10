# Author:zqbin
# @Time:2023/10/10 14:14
# @Author:14988
# @Site:
# @File:demo04_test.py
# @Software:PyCharm
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from jsonpath import jsonpath


def text_is_not_null(locator):
    def method(d):
        return d.find_element(*locator).text

    return method


@pytest.fixture
def fixture_for_login_01():
    # setup ===
    register()
    print("\nsetup")
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def register():
    data = {
        "name": "test926_1010",
        "password1": "123456",
        "password2": "123456"
    }
    requests.request('POST', 'http://39.108.127.130:8008/register/', json=data)


class TestLogin01(object):

    def test_method(self, fixture_for_login_01):
        print("\ntest_method")
        driver = fixture_for_login_01

        driver.get("http://39.108.127.130:8008/")

        driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()

        driver.find_element(By.CSS_SELECTOR, "header button:nth-of-type(4)").click()

        driver.find_element(By.CSS_SELECTOR, "div.q-menu>div>div:nth-of-type(2)").click()
        driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()
        driver.find_element(By.CSS_SELECTOR, "div.q-toolbar>button:nth-of-type(5)").click()
        driver.find_element(By.CSS_SELECTOR, "div[role='tablist']>div>div:last-child").click()
        inputList = driver.find_elements(By.TAG_NAME, "input")
        inputList[0].send_keys("test926_1010")
        inputList[1].send_keys("123456")

        driver.find_element(By.CSS_SELECTOR, "div.q-card span.block").click()

        currentValue = WebDriverWait(driver, 10).until(
            text_is_not_null((By.CSS_SELECTOR, "div.q-notification__message"))
        )
        expectValue = "Success Login"
        assert expectValue == currentValue

# Author:zqbin
# @Time:2023/10/10 14:52
# @Author:14988
# @Site:
# @File:test_login.py
# @Software:PyCharm
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lib.mysql_client import MySQLClient
from lib.http_client import HTTPClient
from lib.config import CONFIG
from lib.extend_ec import text_is_not_null




# @pytest.fixture
# def fixture_for_login_01():
#     mysqlClient = MySQLClient()
#     httpClient = HTTPClient()
#     # setup ===
#     print("\nsetup")
#     # 调用接口实现注册
#     name = "test_10_10_001"
#     password = "123456"
#     path = "/register/"
#     method = "post"
#     data = {
#         "name": name,
#         "password1": password,
#         "password2": password
#     }
#     r = httpClient.request(path=path, method=method, json=data)
#     print(r.text)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     yield driver, name, password
#
#     # teardown
#     print("\nteardown")
#     sqlList = [
#         f"DELETE FROM auth_user WHERE username = '{name}';",
#         f"DELETE FROM user_profile WHERE name = '{name}';"
#     ]
#     mysqlClient.execute(sqlList=sqlList)

class TestLogin01(object):

    def test_method(self, fixture_for_login_01, webdriver_fixture):
        print("\ntest_method")
        driver = webdriver_fixture
        name, password = fixture_for_login_01

        driver.get("http://39.108.127.130:8008/")

        driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()

        driver.find_element(By.CSS_SELECTOR, "header button:nth-of-type(4)").click()

        driver.find_element(By.CSS_SELECTOR, "div.q-menu>div>div:nth-of-type(2)").click()
        driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()
        driver.find_element(By.CSS_SELECTOR, "div.q-toolbar>button:nth-of-type(5)").click()
        driver.find_element(By.CSS_SELECTOR, "div[role='tablist']>div>div:last-child").click()
        inputList = driver.find_elements(By.TAG_NAME, "input")
        inputList[0].send_keys(name)
        inputList[1].send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "div.q-card span.block").click()

        currentValue = WebDriverWait(driver, 10).until(
            text_is_not_null((By.CSS_SELECTOR, "div.q-notification__message"))
        )
        expectValue = "Success Login"
        assert expectValue == currentValue
# Author:zqbin
# @Time:2023/10/10 10:35
# @Author:14988
# @Site:
# @File:demo02_test.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestWMS:
    # def test_login(self):
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #
    #     driver.get("http://39.108.127.130:8008/")
    #     driver.find_element(By.CSS_SELECTOR, "div.q-card>div:first-child>button").click()
    #
    #     driver.find_element(By.CSS_SELECTOR, "header button:nth-of-type(4)").click()
    #
    #     driver.find_element(By.CSS_SELECTOR, "div.q-menu>div>div:nth-of-type(2)").click()
    #     driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()
    #     driver.find_element(By.CSS_SELECTOR, "div.q-toolbar>button:nth-of-type(5)").click()
    #     driver.find_element(By.CSS_SELECTOR, "div[role='tablist']>div>div:last-child").click()
    #
    #     inputList = driver.find_elements(By.CSS_SELECTOR, "input[aria-label]")
    #     inputList[0].send_keys("zqb3")
    #     inputList[1].send_keys("123456")
    #
    #     driver.find_element(By.CSS_SELECTOR, "div.q-card span.block").click()
    #
    #     currentValue = WebDriverWait(driver, 10).until(
    #         ec.presence_of_element_located((By.CSS_SELECTOR, "div.q-notification__message"))
    #     ).text
    #     print(currentValue)
    #
    #     assert 'Success Login' == currentValue, "登录失败"

    def test_02_01(self):
        print('test_02_01')

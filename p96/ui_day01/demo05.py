# Author:zqbin
# @Time:2023/10/8 11:13
# @Author:14988
# @Site:
# @File:demo05.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://39.108.127.130:8008/')
driver.maximize_window()

# input()
driver.find_element(by=By.CSS_SELECTOR, value='.q-card button').click()
driver.find_element(by=By.CSS_SELECTOR, value='.q-header button .block').click()
driver.find_element(by=By.CSS_SELECTOR, value='.q-card .q-bar .q-tab:last-child').click()
driver.find_element(by=By.CSS_SELECTOR, value='.q-card .q-pt-md label input').send_keys('zqb3')
driver.find_element(by=By.CSS_SELECTOR, value='.q-card .q-pt-md label:last-child input').send_keys('123456')
driver.find_element(by=By.CSS_SELECTOR, value='.q-card__actions button').click()

time.sleep(3)

driver.close()
driver.quit()
# Author:zqbin
# @Time:2023/10/8 11:04
# @Author:14988
# @Site:
# @File:demo04.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

# input()
driver.find_element(by=By.CSS_SELECTOR, value='#kw').send_keys('美食')
driver.find_element(by=By.CSS_SELECTOR, value='#su').click()
time.sleep(3)

driver.close()
driver.quit()

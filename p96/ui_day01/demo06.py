# Author:zqbin
# @Time:2023/10/8 11:48
# @Author:14988
# @Site:
# @File:demo06.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

# input()
e = driver.find_element(by=By.CSS_SELECTOR, value='#su')
print(e.get_attribute('value'))
input()
driver.find_element(by=By.LINK_TEXT, value='网盘').click()

time.sleep(3)

driver.close()
driver.quit()
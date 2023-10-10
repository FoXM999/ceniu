# Author:zqbin
# @Time:2023/10/8 15:54
# @Author:14988
# @Site:
# @File:demo10.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://www.baidu.com')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, '网盘').click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH, "//span[text()=' 去登录 ']").click()

input()

time.sleep(5)
driver.close()
driver.quit()
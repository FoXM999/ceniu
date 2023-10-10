# Author:zqbin
# @Time:2023/10/8 16:37
# @Author:14988
# @Site:
# @File:demo12.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://sahitest.com/demo/clicks.htm")
driver.maximize_window()

action = ActionChains(driver)

element = driver.find_element(By.CSS_SELECTOR, "input[value='dbl click me']")
action.double_click(element).perform()

element = driver.find_element(By.CSS_SELECTOR, "input[value='right click me']")
action.context_click(element).perform()

input()
driver.close()
driver.quit()
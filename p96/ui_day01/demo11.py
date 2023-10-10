# Author:zqbin
# @Time:2023/10/8 16:15
# @Author:14988
# @Site:
# @File:demo11.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://www.baidu.com')
driver.maximize_window()

action = ActionChains(driver)
element = driver.find_element(By.CSS_SELECTOR, ".title-content-title")

print('textElement.text=', element.text)
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('美食')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#kw').clear()

searchButton = driver.find_element(value="su")
print(searchButton.size)
print(searchButton.location)
print(searchButton.rect)

input()

time.sleep(5)
driver.close()
driver.quit()

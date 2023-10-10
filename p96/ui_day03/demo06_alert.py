# Author:zqbin
# @Time:2023/10/9 15:38
# @Author:14988
# @Site:
# @File:demo06_alert.py
# @Software:PyCharm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# 设置全局的隐式等待时间
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
driver.maximize_window()

action = ActionChains(driver)
element = driver.find_element(by=By.XPATH, value="//span[text()='设置']")
action.move_to_element(element).perform()

element = driver.find_element(by=By.XPATH, value="//div[@id='s-user-setting-menu']//span[text()='搜索设置']")
action.move_to_element(element).perform()
action.click().perform()

element = driver.find_element(by=By.XPATH, value="//div[@class='pftab']//input[@value='50']")
action.move_to_element(element).perform()
action.click().perform()
element = driver.find_element(by=By.XPATH, value="//div[@class='pftab']//div[@id='se-setting-7']/a[2]")
action.move_to_element(element).perform()
action.click().perform()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()


time.sleep(5)
driver.close()
driver.quit()
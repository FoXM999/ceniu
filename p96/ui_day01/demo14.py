# Author:zqbin
# @Time:2023/10/8 16:45
# @Author:14988
# @Site:
# @File:demo14.py
# @Software:PyCharm
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/dragDropMooTools.htm")

element = driver.find_element(By.CSS_SELECTOR, '#dragger')
targetList = driver.find_elements(By.CSS_SELECTOR, '.item')

action = ActionChains(driver)

for i in range(4):
    # action.move_to_element(element).click_and_hold().move_to_element(targetList[i]).release().perform()
    action.click_and_hold(element).release(targetList[i]).perform()
    sleep(2)

input()

driver.close()
driver.quit()
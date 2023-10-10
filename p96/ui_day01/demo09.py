# Author:zqbin
# @Time:2023/10/8 14:55
# @Author:14988
# @Site:
# @File:demo09.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://sahitest.com/demo/clicks.htm")
driver.maximize_window()

action = ActionChains(driver)

# 1.Clear按钮
ButtonClear = driver.find_element(By.CSS_SELECTOR, "input[value='Clear']")

# input[value='dbl click me']
Button_dbl_click_me = driver.find_element(By.CSS_SELECTOR, "input[value^='dbl']")

# input[value='click me']
Button_click_me = driver.find_element(By.CSS_SELECTOR, "input[value^='click']")

# input[value='right click me']
Button_right_click_me = driver.find_element(By.CSS_SELECTOR, "input[value^='right']")

# 输出框
result = driver.find_element(By.CSS_SELECTOR, "[name='t2']")

# 点清空
# clickClear = action.move_to_element(ButtonClear).perform()
# ButtonClear.click()

# 点 click me
# action.move_to_element(Button_click_me).perform()
# action.click().perform()
action.move_to_element(Button_click_me).click().perform()
print(result.get_attribute("value"))
# 点Clear
time.sleep(3)
# action.move_to_element(ButtonClear).perform()
# ButtonClear.click()
action.click(ButtonClear).perform()

# 点两次dbl_click_me
time.sleep(3)
action.double_click(Button_dbl_click_me).perform()
print(result.get_attribute("value"))

# 点Clear
time.sleep(3)
ButtonClear.click()

# 右键点right_click_me
time.sleep(3)
action.context_click(Button_right_click_me).perform()
print(result.get_attribute("value"))

time.sleep(3)

driver.close()
driver.quit()
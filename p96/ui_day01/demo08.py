# Author:zqbin
# @Time:2023/10/8 14:51
# @Author:14988
# @Site:
# @File:demo08.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
# 鼠标操作需要导入ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# https://sahitest.com/demo/mouseover.htm
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/mouseover.htm")

# 实例化ActionChains需要传入一个webdriver对象
actions = ActionChains(driver)
sleep(5)

buttons = driver.find_elements(By.NAME, "b1")
results = driver.find_element(By.NAME, "t1")

# 1. 移动鼠标到writebutton, 显示Mouse moved
# move_to_element()   将鼠标移动到一个webelement上
actions.move_to_element(buttons[0])
actions.perform()  # 将动作链中的所有动作提交之后才会生效
print(results.get_attribute("value"))
sleep(5)

# 1. 移动鼠标到blankbutton
actions.move_by_offset(0, buttons[1].location["y"] - buttons[0].location["y"]).perform()
print(results.get_attribute("value"))
sleep(5)

actions.move_to_element_with_offset(buttons[1], 0, (buttons[1].location["y"] - buttons[0].location["y"]) * -1).perform()

sleep(5)
driver.close()
driver.quit()
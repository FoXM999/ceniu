# Author:zqbin
# @Time:2023/10/8 16:42
# @Author:14988
# @Site:
# @File:demo13.py
# @Software:PyCharm
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/dragDropMooTools.htm")

dragDiv = driver.find_element(value="dragger")
targetDivs = driver.find_elements(By.CLASS_NAME, "item")
print(len(targetDivs))

sleep(5)
actions = ActionChains(driver)
actions.drag_and_drop(dragDiv, targetDivs[0]).perform()

# sleep(5)
# actions.move_to_element(dragDiv).click_and_hold().move_to_element(targetDivs[1]).release().perform()
# sleep(5)
# actions.click_and_hold(dragDiv).release(targetDivs[2]).perform()
# sleep(5)
# actions.drag_and_drop_by_offset(
#     dragDiv,
#     targetDivs[3].location["x"] - dragDiv.location["x"],
#     targetDivs[3].location["y"] - dragDiv.location["y"]
# ).perform()
# sleep(5)
input()
driver.close()
driver.quit()
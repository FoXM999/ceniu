# Author:zqbin
# @Time:2023/10/9 15:25
# @Author:14988
# @Site:
# @File:demo05.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.126.com")

loginFrame = driver.find_element(By.CSS_SELECTOR, "iframe[id^='x-URS-iframe']")
driver.switch_to.frame(loginFrame)

driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("zhengqingbin2023")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("zqb19971023ZQB")
# driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT, "帮助").click()

handler = driver.window_handles
driver.switch_to.window(handler[1])

driver.find_element(By.CSS_SELECTOR, "form[class='search'] input[type='text']").send_keys('密码')
driver.find_element(By.CSS_SELECTOR, "form[class='search'] input[type='submit']").click()

driver.switch_to.window(handler[0])
driver.switch_to.frame(loginFrame)
driver.find_element(By.CSS_SELECTOR, "a#dologin").click()

input()

driver.close()
driver.quit()

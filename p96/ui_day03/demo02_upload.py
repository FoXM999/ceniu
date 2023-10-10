# Author:zqbin
# @Time:2023/10/9 14:12
# @Author:14988
# @Site:
# @File:demo02_upload.py
# @Software:PyCharm
import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.126.com")

loginFrame = driver.find_element(By.CSS_SELECTOR, "iframe[id^='x-URS-iframe']")
driver.switch_to.frame(loginFrame)

driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("zhengqingbin2023")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("zqb19971023ZQB")
driver.find_element(By.CSS_SELECTOR, "a#dologin").click()

driver.find_element(By.XPATH, "//span[text()='写 信']").click()
driver.find_element(By.CSS_SELECTOR, ".nui-editableAddr-ipt").send_keys('qinrui1008@126.com')
driver.find_element(By.CSS_SELECTOR, ".nui-ipt-input[maxlength='256']").send_keys('TEST')
file_path = os.path.join("C:\\Users\\14988\\Desktop", '测试文件上传.docx')
driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)

textFrame = driver.find_element(By.CSS_SELECTOR, ".APP-editor-iframe")
driver.switch_to.frame(textFrame)
driver.find_element(By.CSS_SELECTOR, "p").send_keys('test')

driver.switch_to.default_content()
driver.find_element(By.XPATH, "//span[text()='发送']").click()

input()

driver.close()
driver.quit()
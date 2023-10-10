# Author:zqbin
# @Time:2023/10/7 14:30
# @Author:14988
# @Site:
# @File:demo02_upload.py
# @Software:PyCharm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

driver.maximize_window()

driver.find_element(by=By.XPATH, value='//form/span[1]/input').send_keys('美食')
time.sleep(3)

driver.find_element(value='su').click()
time.sleep(3)

driver.close()
driver.quit()
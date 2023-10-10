# Author:zqbin
# @Time:2023/10/8 20:56
# @Author:14988
# @Site:
# @File:demo15.py
# @Software:PyCharm
from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.baidu.com")

# driver.close()
# driver.quit()
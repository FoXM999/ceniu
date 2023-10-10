# Author:zqbin
# @Time:2023/10/7 12:39
# @Author:14988
# @Site:
# @File:demo01.py
# @Software:PyCharm
# 1. 导入selenium模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 2. 实例化webdriver对象-把chrome浏览器打开
# 根据测试时候使用的浏览器不同，需要实例化不同的webdriver对象
driver = webdriver.Chrome()
# 将浏览器窗口最大化
driver.maximize_window()

# 3. 打开网站
driver.get("https://www.baidu.com")

# 4. 业务操作（输入一些文本内容，点击一些页面元素，......）
# 	5. 定位或者获取页面元素
#   find_element方法如果定位到元素，返回定位到的元素，即一个webelement对象
keyWordInput = driver.find_element(by=By.ID, value="kw")
# 	6. 对元素进行操作
#    webelement对象的send_keys方法，向webelement对象输入文本内容
keyWordInput.send_keys("test")
sleep(3)
# 链式写法
#    webelement对象的click方法，点击定位到的webelement
driver.find_element(value="su").click()


sleep(3)
# 7. 关闭浏览器
driver.close()
# 8. 退出webdriver对象
driver.quit()
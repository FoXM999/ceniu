# Author:zqbin
# @Time:2023/10/9 15:52
# @Author:14988
# @Site:
# @File:demo07_js.py
# @Software:PyCharm
import time
from selenium import webdriver
from selenium.common import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.set_page_load_timeout(5)
# 设置全局的隐式等待时间
# driver.implicitly_wait(10)
try:
    driver.get('https://element.eleme.cn/#/zh-CN/component/date-picker')
except TimeoutException:
    jsCode = 'window.stop()'
    driver.execute_script(jsCode)

driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='默认']/..//input").send_keys('2023-10-08')
driver.find_element(By.XPATH, "//span[text()='带快捷选项']").click()

js = '''document.querySelector("input[placeholder='选择一个或多个日期']").removeAttribute("readonly")'''
driver.execute_script(js)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='选择一个或多个日期']").send_keys('2023-10-01, 2023-10-03')
# time.sleep(3)
WebDriverWait(driver, 10, 1, ignored_exceptions=(ElementNotInteractableException,)).until(
    lambda d: not d.find_element(By.XPATH, "//div[@x-placement]//span[contains(text(),'确定')]").click()
)
# driver.find_element(By.XPATH, "//div[@x-placement]//span[contains(text(),'确定')]").click()
input()

driver.close()
driver.quit()

# Author:zqbin
# @Time:2023/10/7 15:42
# @Author:14988
# @Site:
# @File:demo03_login.py
# @Software:PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('http://39.108.127.130:8008/')
driver.maximize_window()

# 登录
driver.find_element(by=By.XPATH, value="//div[@class='q-card']//i[text()='close']").click()
driver.find_element(by=By.XPATH, value="//header//span[text()='Login']").click()
driver.find_element(by=By.XPATH, value="//div[@class='q-card']//div[@role='tab'][2]").click()
driver.find_element(by=By.XPATH, value="//div[@class='q-card']//input[@aria-label='Admin']").send_keys('zqb3')
driver.find_element(by=By.XPATH, value="//div[@class='q-card']//input[@aria-label='Password']").send_keys('123456')
driver.find_element(by=By.XPATH, value="//div[@class='q-card']//span[text()='Login']").click()

# input()
# 改为中文
wait = WebDriverWait(driver, 10)
element = driver.find_element(by=By.XPATH, value="//i[text()='translate']")
driver.execute_script("arguments[0].click()", element)
wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//div[@class='q-menu q-position-engine scroll']//div[text()='中文简体']"))
).click()

# 创建到货通知书
driver.find_element(by=By.XPATH,
                    value="//div[@class='q-drawer-container']//div[@class='q-list']//div[text()='收货管理']").click()
wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//div[@class='main-table']//div[contains(@class,'q-table__top')]//span[text()='新增']"))
).click()
# time.sleep(1)
element = wait.until(
    ec.presence_of_element_located((By.CSS_SELECTOR, ".q-bar div:first-child"))
)
asn = element.get_attribute('innerText')
# driver.find_element(By.CSS_SELECTOR, '.q-bar div:first-child').text
print('asn=', asn)
input()

driver.find_element(by=By.XPATH,
                    value="//div[@class='shadow-24 q-card']//div[text()='供应商名称']/preceding-sibling::div/input").send_keys(
    'Supplier Name-1')
wait.until(
    ec.presence_of_element_located((By.XPATH, "//div[@role='listbox']//div[text()='Supplier Name-1']"))
).click()

element = driver.find_element(by=By.XPATH,
                              value="//div[@class='shadow-24 q-card']//label[2]//div[text()='商品编码']/preceding-sibling::div/input")

driver.find_element(by=By.XPATH,
                              value="//div[@class='shadow-24 q-card']//label[2]//div[text()='商品编码']/preceding-sibling::div/input").send_keys(
    'A')


def wait_goods_code(d):
    element.click()
    time.sleep(1)
    return d.find_element(By.XPATH, "//div[@class='q-item__label']")


wait.until(wait_goods_code).click()

driver.find_element(by=By.XPATH,
                    value="//div[@class='shadow-24 q-card']//label[2]//div[text()='总数量']/preceding-sibling::input").send_keys(
    20)
driver.find_element(by=By.XPATH, value="//div[@class='shadow-24 q-card']//span[text()='确认']").click()

# 确认到货
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "q-td text-left")))
while element.text != asn:
    element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "q-td text-left")))
    time.sleep(0.5)
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".main-table .q-tr button:nth-child(2)")))
driver.execute_script("arguments[0].click()", element)
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".q-card div:last-child button:last-child")))
driver.execute_script("arguments[0].click()", element)
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".main-table .q-tr button:nth-child(3)")))
driver.execute_script("arguments[0].click()", element)
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".q-card div:last-child button:last-child")))
driver.execute_script("arguments[0].click()", element)
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".main-table .q-tr button:nth-child(4)")))
driver.execute_script("arguments[0].click()", element)

element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "q-card label:last-child input")))
driver.execute_script("arguments[0].click()", element)
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".q-card div:last-child button:last-child")))
driver.execute_script("arguments[0].click()", element)

wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='q-pa-md']//div[text()='已分拣']"))).click()
# driver.find_element(by=By.XPATH, value="//div[@class='q-pa-md']//div[text()='已分拣']").click()
# time.sleep(2)
driver.find_element(by=By.XPATH, value="//div[@class='main-table']//tr//span[@class='q-focus-helper']/..").click()
driver.find_element(by=By.XPATH,
                    value="//div[@class='shadow-24 q-card']//div[text()='库位名称']/preceding-sibling::div/input").send_keys(
    'B0')
driver.find_element(by=By.XPATH, value="//div[@role='listbox']//div[text()='B010101']").click()
driver.find_element(by=By.XPATH,
                    value="//div[@class='shadow-24 q-card']//div[text()='总数量']/preceding-sibling::input").send_keys(
    20)
driver.find_element(by=By.XPATH, value="//div[@class='shadow-24 q-card']//span[text()='确认']").click()

time.sleep(5)

input()

driver.close()
driver.quit()

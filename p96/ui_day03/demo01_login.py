# Author:zqbin
# @Time:2023/10/9 11:40
# @Author:14988
# @Site:
# @File:demo01_login.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


def select_goods_code(d, index, code):
    goodsCodeInputs = d.find_elements(By.XPATH, "//div[text()='商品编码']/preceding-sibling::div/input")
    arrows = d.find_elements(By.XPATH, "//div[text()='商品编码']/parent::div/following-sibling::div//i")

    goodsCodeInputs[index].send_keys("a")

    def wait_goods_code(index, code, sleepTime=1):
        def method(d):
            arrows[index].click()
            sleep(sleepTime)
            return d.find_element(By.XPATH, f"//div[text()='{code}']")

        return method

    WebDriverWait(driver, 10).until(wait_goods_code(index, code)).click()


def select_goods_qty(d, index, qty):
    inputs = d.find_elements(By.XPATH, "//div[text()='总数量']/preceding-sibling::input")
    inputs[index].send_keys(qty)


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://39.108.127.130:8008/")
driver.find_element(By.CSS_SELECTOR, "div.q-card>div:first-child>button").click()

driver.find_element(By.CSS_SELECTOR, "header button:nth-of-type(4)").click()

driver.find_element(By.CSS_SELECTOR, "div.q-menu>div>div:nth-of-type(2)").click()
driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()
driver.find_element(By.CSS_SELECTOR, "div.q-toolbar>button:nth-of-type(5)").click()
driver.find_element(By.CSS_SELECTOR, "div[role='tablist']>div>div:last-child").click()

inputList = driver.find_elements(By.CSS_SELECTOR, "input[aria-label]")
inputList[0].send_keys("zqb3")
inputList[1].send_keys("123456")

driver.find_element(By.CSS_SELECTOR, "div.q-card span.block").click()
textValue = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.q-notification__message"))
).text
print('textValue=', textValue)
# currentValue = driver.find_element(By.CSS_SELECTOR, "div.q-notification__message").text
input()

# driver.find_element(By.XPATH, "//i[text()='speaker_notes']").click()
WebDriverWait(driver, 10, ignored_exceptions=(ElementClickInterceptedException,)).until(
    lambda x: True if x.find_element(By.XPATH,
                                     "//i[text()='speaker_notes']").click() else True
)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='新增']"))
).click()

# driver.find_element(By.CSS_SELECTOR, "div.q-card>div:nth-child(2)>label:first-child>div").click()
WebDriverWait(driver, 10, ignored_exceptions=(ElementNotInteractableException,)).until(
    lambda x: True if x.find_element(By.CSS_SELECTOR,
                                     "div.q-card>div:nth-child(2)>label:first-child>div").click() else True
)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Supplier Name-1']"))
).click()
# driver.find_element(By.XPATH, "//div[text()='阿里']").click()

select_goods_code(driver, 0, "A000039")
select_goods_qty(driver, 0, 20)

WebDriverWait(driver, 10, ignored_exceptions=(ElementNotInteractableException,)).until(
    lambda x: not x.find_element(By.XPATH, "//span[text()='确认']").click()
)

WebDriverWait(driver, 10, ignored_exceptions=(ElementClickInterceptedException, StaleElementReferenceException)).until(
    lambda x: not x.find_element(By.CSS_SELECTOR, "tbody>tr:first-child img[src*='preloadstock']").click()
)

WebDriverWait(driver, 10, ignored_exceptions=(ElementNotInteractableException, ElementClickInterceptedException)).until(
    lambda x: not x.find_element(By.XPATH, "//span[text()='确认']").click()
)

WebDriverWait(driver, 10, ignored_exceptions=(ElementClickInterceptedException, StaleElementReferenceException)).until(
    lambda x: not x.find_element(By.CSS_SELECTOR, "tbody>tr:first-child img[src*='presortstock']").click()
)

WebDriverWait(driver, 10, ignored_exceptions=(ElementNotInteractableException, ElementClickInterceptedException)).until(
    lambda x: not x.find_element(By.XPATH, "//span[text()='确认']").click()
)

WebDriverWait(driver, 10, ignored_exceptions=(ElementClickInterceptedException, StaleElementReferenceException)).until(
    lambda x: not x.find_element(By.CSS_SELECTOR,
                                 "tbody>tr:first-child img[src='statics/inbound/sortstock.png']").click()
)
WebDriverWait(driver, 10).until(
    lambda x: not x.find_element(By.XPATH, "//div[text()='实际到货数量']/preceding-sibling::input").send_keys(20)
)
driver.find_element(By.XPATH, "//span[text()='确认']").click()


# 已分拣
def select_store_code(d, index, code):
    goodsCodeInputs = d.find_elements(By.CSS_SELECTOR, ".q-card input")
    arrows = d.find_elements(By.CSS_SELECTOR, ".q-card .q-field__before i")

    goodsCodeInputs[index].send_keys("b")

    def wait_goods_code(index, code, sleepTime=1):
        def method(d):
            arrows[index].click()
            sleep(sleepTime)
            return d.find_element(By.XPATH, f"//div[text()='{code}']")

        return method

    WebDriverWait(driver, 10).until(wait_goods_code(index, code)).click()


driver.find_element(By.XPATH, "//div[text()='已分拣']").click()
WebDriverWait(driver, 10).until(
    lambda x: not x.find_element(By.XPATH, "//i[text()='move_to_inbox']").click()
)
select_store_code(driver, 0, 'B010101')
driver.find_element(By.XPATH, "//div[text()='总数量']/preceding-sibling::input").send_keys(20)
driver.find_element(By.XPATH, "//span[text()='确认']").click()

input()
sleep(5)
driver.close()
driver.quit()

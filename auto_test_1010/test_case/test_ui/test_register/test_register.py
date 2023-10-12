# Author:zqbin
# @Time:2023/10/10 16:01
# @Author:14988
# @Site:
# @File:test_register.py
# @Software:PyCharm
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lib.extend_ec import text_is_not_null
from lib.config import CONFIG

@allure.epic("WebUI测试用例")
@allure.feature("用户模块")
@allure.story("注册")
# @allure.severity(allure.severity.)
class TestRegisterDDT(object):

    def test_method(self, webdriver_fixture, fixture_for_register_ddt):
        driver = webdriver_fixture
        data = fixture_for_register_ddt
        driver.get(CONFIG["server"]["baseUrl"])

        driver.find_element(By.CSS_SELECTOR, "div.q-card i[role='img']").click()
        driver.find_element(By.CSS_SELECTOR, "header button:nth-of-type(4)").click()
        driver.find_element(By.CSS_SELECTOR, "div.q-menu>div>div:nth-of-type(2)").click()

        inputList = driver.find_elements(By.CSS_SELECTOR, "input[aria-label]")
        inputList[0].send_keys(data["name"])
        inputList[1].send_keys(data["password1"])
        inputList[2].send_keys(data["password2"])
        driver.find_element(By.XPATH, "//div[@class='q-card']//span[text()='注册']").click()

        currentValue = WebDriverWait(driver, 10).until(
            text_is_not_null((By.CSS_SELECTOR, "div.q-notification__message"))
        )
        expectValue = data["msg"]
        assert expectValue == currentValue
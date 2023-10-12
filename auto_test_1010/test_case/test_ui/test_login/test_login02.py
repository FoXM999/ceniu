# Author:zqbin
# @Time:2023/10/11 16:22
# @Author:14988
# @Site:
# @File:test_login02.py
# @Software:PyCharm
import allure
from page.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import CONFIG
from lib.extend_ec import text_is_not_null


@allure.epic("WebUI测试用例")
@allure.feature("用户管理")
@allure.story("登录")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin01(object):
    @allure.title("正常登录")
    def test_method(self, fixture_for_login_01, webdriver_fixture):
        name, password = fixture_for_login_01
        driver = webdriver_fixture
        mainPage = MainPage(driver=driver, url=CONFIG["server"]["baseUrl"])
        mainPage.login(name, password)
        currentValue = mainPage.find_element(mainPage.divNotification).text(is_not_none=True)
        expectValue = "Success Login"
        assert expectValue == currentValue, f"预期结果: {expectValue} != 实际结果: {currentValue}"
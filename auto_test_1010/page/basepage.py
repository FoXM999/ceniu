# Author:zqbin
# @Time:2023/10/11 16:15
# @Author:14988
# @Site:
# @File:basepage.py
# @Software:PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException


class Element(object):

    def __init__(self, _driver, _element, _locator):
        self._driver = _driver
        self.element = _element
        self._locator = _locator

    def send_keys(self, content, is_clear=False):
        if is_clear:
            self.element.clear()
        self.element.send_keys(content)

    def click(self):

        def _click_abel(_ele):
            def method(x):
                return not _ele.click()

            return method

        exceptions = [
            StaleElementReferenceException,
            ElementClickInterceptedException
        ]
        WebDriverWait(driver=self._driver, timeout=10, ignored_exceptions=exceptions).until(
            _click_abel(self.element)
        )

    def text(self, is_not_none=False):
        if is_not_none:
            def text_is_not_none(_ele):
                def method(d):
                    return _ele.element.text

                return method

            return WebDriverWait(self._driver, 10).until(text_is_not_none(self))
        else:
            return self.element.text


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        _element = WebDriverWait(driver=self.driver,
                                 timeout=10).until(
            EC.presence_of_element_located(locator=locator)
        )
        return Element(self.driver, _element, locator)

    def find_elements(self, locator):
        _list = WebDriverWait(driver=self.driver,
                              timeout=10).until(
            EC.presence_of_all_elements_located(locator=locator)
        )
        return [Element(self.driver, item, locator) for item in _list]
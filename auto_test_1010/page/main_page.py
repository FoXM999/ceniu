# Author:zqbin
# @Time:2023/10/11 16:21
# @Author:14988
# @Site:
# @File:main_page.py
# @Software:PyCharm
from page.basepage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, driver, url=None):
        super().__init__(driver)
        self.url = url
        if self.url is not None:
            self.driver.get(self.url)

        self.iCloseRegister = (By.CSS_SELECTOR, "div.q-card i[role='img']")
        self.buttonChangeLanguage = (By.CSS_SELECTOR, "header button:nth-of-type(4)")
        self.divChinese = (By.CSS_SELECTOR, "div.q-menu>div>div:nth-of-type(2)")
        self.divLogin = (By.CSS_SELECTOR, "div.q-toolbar>button:nth-of-type(5)")
        self.divAdminLogin = (By.CSS_SELECTOR, "div[role='tablist']>div>div:last-child")
        self.userAndPasswdInputList = (By.TAG_NAME, "input")
        self.submitLogin = (By.CSS_SELECTOR, "div.q-card span.block")
        self.divNotification = (By.CSS_SELECTOR, "div.q-notification__message")

    def login(self, name, password):
        self.find_element(self.iCloseRegister).click()
        self.find_element(self.buttonChangeLanguage).click()
        self.find_element(self.divChinese).click()
        self.find_element(self.iCloseRegister).click()
        self.find_element(self.divLogin).click()
        self.find_element(self.divAdminLogin).click()
        self.find_elements(self.userAndPasswdInputList)[0].send_keys(name)
        self.find_elements(self.userAndPasswdInputList)[1].send_keys(password)
        self.find_element(self.submitLogin).click()

    def select_language_by_index(self, index):
        pass

    def select_language_by_name(self, name):
        pass
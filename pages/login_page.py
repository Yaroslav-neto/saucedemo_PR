import re

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPageLocators:
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"
    INVENTORY_CONTAINER = ".inventory_list"


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._username = page.locator(LoginPageLocators.USERNAME_INPUT)
        self._password = page.locator(LoginPageLocators.PASSWORD_INPUT)
        self._login_btn = page.locator(LoginPageLocators.LOGIN_BUTTON)
        self._error_msg = page.locator(LoginPageLocators.ERROR_MESSAGE)
        self._inventory_list = page.locator(LoginPageLocators.INVENTORY_CONTAINER)

    @allure.step("Авторизация")
    def login(self, username, password):
        self._username.fill(username)
        self._password.fill(password)
        self._login_btn.click()

    @allure.step("Проверка текста ошибки: {text}")
    def check_error_message(self, text):
        expect(self._error_msg).to_contain_text(text)

    @allure.step("Проверка успешного перехода в каталог")
    def should_be_at_inventory_page(self):
        self.should_have_url(re.compile(r".*/inventory.html"))
        self.is_visible(self._inventory_list)

    def navigate(self):
        self.open("/")

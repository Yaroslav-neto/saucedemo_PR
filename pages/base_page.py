from re import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу {url}")
    def open(self, url: str):
        self.page.goto(url)

    @allure.step("Проверить, что URL страницы — {url}")
    def should_have_url(self, url: str | Pattern[str]):
        expect(self.page).to_have_url(url)

    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator):
        expect(locator).to_be_visible()

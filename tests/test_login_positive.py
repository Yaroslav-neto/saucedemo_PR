import allure
import pytest

from data.test_data import Users


@allure.feature("Авторизация")
@allure.story("Позитивные сценарии")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, login_page):
        login_page.navigate()

    @allure.title("Успешный логин")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_success_login(self, login_page):
        login_page.login(Users.STANDARD_USER, Users.PASSWORD)
        login_page.should_be_at_inventory_page()

    @allure.title("Логин с задержкой (Performance Glitch)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_performance_glitch_user(self, login_page):
        login_page.login(Users.GLITCH_USER, Users.PASSWORD)
        login_page.should_be_at_inventory_page()

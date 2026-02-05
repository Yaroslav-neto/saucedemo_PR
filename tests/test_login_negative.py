import allure
import pytest

from data.test_data import Users, ErrorMessages, FakeData


@allure.feature("Авторизация")
@allure.story("Негативные сценарии")
@allure.severity(allure.severity_level.CRITICAL)
class TestFailLogin:

    @pytest.fixture(autouse=True)
    def setup(self, login_page):
        login_page.navigate()

    @allure.title("Проверка ошибок авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка различных вариантов ввода невалидных данных")
    @pytest.mark.parametrize("username, password, expected_error", [
        (Users.STANDARD_USER, FakeData.PASSWORD, ErrorMessages.WRONG_CREDENTIALS),
        (Users.LOCKED_USER, Users.PASSWORD, ErrorMessages.LOCKED_OUT),
        ("", "", ErrorMessages.USER_REQUIRED)
    ], ids=["fake_password", "locked_out_user", "empty_fields"])
    def test_login_errors(self, login_page, username, password, expected_error):
        login_page.login(username, password)
        login_page.check_error_message(expected_error)

import allure
import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

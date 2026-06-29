import pytest
from playwright.sync_api import Playwright, Page

pytest_plugins = (
    "fixtures.pages",
    # "fixtures.browsers"  # Раскомментировать, если нужны фикстуры для браузера
)


@pytest.fixture(scope="function")
def page(browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


# @pytest.fixture(scope="session")
# def initialize_browser_state(playwright: Playwright):
#     """
#     Фикстура для сохранения состояния браузера после регистрации.
#     Используется ОДИН раз за сессию.
#     """
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
#
#     email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#     email_input.fill('user.name@gmail.com')
#
#     username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#     username_input.fill('username')
#
#     password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#     password_input.fill('password')
#
#     registration_button = page.get_by_test_id('registration-pages-registration-button')
#     registration_button.click()
#
#     context.storage_state(path="tests/browser-state.json")
#     context.close()
#     browser.close()
#     return "tests/browser-state.json"


# @pytest.fixture(scope="function")
# def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
#     """
#     Фикстура для страницы с сохраненным состоянием.
#     Создает НОВУЮ страницу для КАЖДОГО теста.
#     """
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state="tests/browser-state.json")
#     page = context.new_page()
#
#     yield page
#
#     context.close()
#     browser.close()
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    brouser = playwright.chromium.launch(headless=False)
    page = brouser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill('password')

    login_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    login_button.click()

    dashboard_v = page.locator('//div//h6[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_v).to_be_visible()
    expect(dashboard_v).to_have_text('Dashboard')


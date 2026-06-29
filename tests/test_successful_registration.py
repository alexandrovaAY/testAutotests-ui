import pytest

from fixtures.pages import dashboard_page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form( email = 'sss@sss.ru', username = 'sss', password = 'sss')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()

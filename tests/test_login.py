import pytest

from pages.login_page import LoginPage
from playwright.sync_api import Page, expect
from helpers.config import LoginCredentials

def test_login(open_browser: Page):

    login_page = LoginPage(open_browser)

    login_page.click_login_link()
    login_page.input_email_address(LoginCredentials.email)
    login_page.input_password(LoginCredentials.password)
    login_page.click_login_button()


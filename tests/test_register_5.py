from playwright.sync_api import Page, expect
import pytest
from pages.register_page import RegisterPage
from helpers.random_email import generate_random_email


#@pytest.mark.skip
def test_register_new_user_account(open_browser: Page):
    register_page = RegisterPage(open_browser)
    random_email = generate_random_email()
    register_page.navigate_to_register_page()
    register_page.fill_registration_form("male", "David", "Ross", random_email, "abc@123", "abc@123")
    register_page.submit_registration()

from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from helpers.random_email import generate_random_email


def test_register_new_user_account(page: Page):
    register_page = RegisterPage(page)
    random_email = generate_random_email()
    register_page.navigate_to_register_page()
    register_page.fill_registration_form("male", "David", "Ross", random_email, "abc@123", "abc@123")
    register_page.submit_registration()

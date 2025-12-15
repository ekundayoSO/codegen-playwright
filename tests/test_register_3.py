from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from helpers.random_email import generate_random_email
import pytest


@pytest.mark.parametrize(
    "gender, first_name, last_name, email, password, confirm_password",
    [
        ("female", "Jane", "Roose", generate_random_email(), "abc123", "abc123"),
        ("male", "David", "Ross", generate_random_email(), "abc@123", "abc@123"),
        ("male", "Habiba", "Rid", generate_random_email(), "abc@123", "abc@123"),
    ],
)
def test_register_new_user_account(
    page: Page, gender, first_name, last_name, email, password, confirm_password
):
    register_page = RegisterPage(page)
    register_page.navigate_to_register_page()
    register_page.fill_registration_form(
        gender=gender,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        confirm_password=confirm_password,
    )
    register_page.submit_registration()

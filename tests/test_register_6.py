from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from helpers.random_email import generate_random_email
import pytest

data = [
    ("female", "Jane", "Roose", "abc123", "abc123"),
    ("male", "David", "Ross", "abc@123", "abc@123"),
    ("male", "Habiba", "Rid", "abc@123", "abc@123"),
    ("female", "Gold", "Felix", "abc@123", "abc@123"),
    ("female", "Lizzy", "Benson", "abc@123", "abc@123"),

]

@pytest.mark.parametrize(
    "gender, first_name, last_name, password, confirm_password", data
)
def test_register_new_user_account(
    page: Page, gender, first_name, last_name, password, confirm_password
):
    register_page = RegisterPage(page)
    register_page.navigate_to_register_page()
    register_page.fill_registration_form(
        gender=gender,
        first_name=first_name,
        last_name=last_name,
        email=generate_random_email(),
        password=password,
        confirm_password=confirm_password,
    )
    register_page.submit_registration()

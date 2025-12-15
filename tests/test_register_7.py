import json

from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from helpers.random_email import generate_random_email
import pytest

with open("testdata/data.json") as f:
    register_data = json.load(f)


@pytest.mark.parametrize(
    "gender, first_name, last_name, password, confirm_password",
    [(
            data["gender"],
            data["first_name"],
            data["last_name"],
            data["password"],
            data["confirm_password"]) for data in register_data
    ])
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

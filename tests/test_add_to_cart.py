import json
import time

import pytest
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from conftest import open_browser
from helpers.config import LoginCredentials


def read_json(file_path):
    file = open(file_path, "r")
    return json.load(file)

def test_add_products_to_cart(open_browser: Page):

    login_page = LoginPage(open_browser)

    # Login to the web app
    login_page.click_login_link()
    login_page.input_email_address(LoginCredentials.email)
    login_page.input_password(LoginCredentials.password)
    login_page.click_login_button()

    # Add product to cart
    products = read_json("testdata/products.json")
    cart_page = CartPage(open_browser)
    cart_page.add_products_to_cart(products)

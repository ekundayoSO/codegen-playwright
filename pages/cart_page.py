import time

from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.search_field = page.locator("#small-searchterms")
        self.search_button = page.get_by_role("button", name="Search")
        self.add_to_cart_btn = page.locator('input[value="Add to cart"]')

    def add_products_to_cart(self, products):
        for item in products:
            self.search_field.fill(item)
            self.search_field.press("Enter")
            self.add_to_cart_btn.first.click()
            self.page.wait_for_selector("p.content", state="visible")








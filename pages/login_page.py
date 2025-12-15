

from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.login_link = page.get_by_role("link", name = "Log in")
        self.email_field = page.get_by_role("textbox", name = "Email:")
        self.password_field = page.get_by_role("textbox", name = "Password:")
        self.login_btn = page.get_by_role("button", name = "Log in")

        # Actions method
    def click_login_link(self):
        self.login_link.click()

    def input_email_address(self, email):
        self.email_field.fill(email)

    def input_password(self, passwd):
        self.password_field.fill(passwd)

    def click_login_button(self):
        self.login_btn.click()


from playwright.sync_api import Page


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page

        # Store locators only (do NOT click/fill here)
        self.register_link = page.get_by_role("link", name="Register")
        #self.male_radio = page.get_by_role("radio", name="Male", exact=True)
        #self.female_radio = page.get_by_role("radio", name="Female")
        self.gender_radio_button = page.locator("div.gender")
        self.firstname_input = page.get_by_role("textbox", name="First name:")
        self.lastname_input = page.get_by_role("textbox", name="Last name:")
        self.email_input = page.get_by_role("textbox", name="Email:")
        self.password_input = page.get_by_role("textbox", name="Password:", exact=True)
        self.confirm_password_input = page.get_by_role(
            "textbox", name="Confirm password:"
        )

        self.register_button = page.get_by_role("button", name="Register")

    # Methods to interact with the page
    def navigate_to_register_page(self):
        self.page.goto("https://demowebshop.tricentis.com/register")

    def click_register_link(self):
        self.register_link.click()

    def fill_registration_form(
        self,
        gender: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        confirm_password: str,
    ):
        if gender.lower() == "male":
            self.gender_radio_button.locator("input[value='M']").check()
        elif gender.lower() == "female":
            self.gender_radio_button.locator("input[value='F']").check()
        else:
            raise ValueError("Gender must be 'male' or 'female'")

        self.firstname_input.fill(first_name)
        self.lastname_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)

    def submit_registration(self):
        self.register_button.click()




import re
from playwright.sync_api import Playwright, sync_playwright, expect
from helpers.random_email import generate_random_email


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demowebshop.tricentis.com/")

    randon_email = generate_random_email()

    page.get_by_role("link", name="Register").click()
    page.get_by_role("radio", name="Male", exact=True).check()
    page.get_by_role("textbox", name="First name:").fill("Donald")
    page.get_by_role("textbox", name="Last name:").fill("Steven")
    page.get_by_role("textbox", name="Email:").fill(randon_email)
    page.get_by_role("textbox", name="Password:", exact=True).fill("steven123")
    page.get_by_role("textbox", name="Confirm password:").fill("steven123")
    page.get_by_role("button", name="Register").click()

    expect(page.locator("body")).to_contain_text("Your registration completed")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

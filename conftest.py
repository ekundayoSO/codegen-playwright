from playwright.sync_api import Page
import pytest

@pytest.fixture
def open_browser(page: Page):
    page.goto("https://demowebshop.tricentis.com/register")
    return page

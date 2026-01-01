import pytest
from playwright.sync_api import sync_playwright, expect

from globals import URL
from ui_automation.pages.welcome_page import WelcomePage


@pytest.fixture()
def setup_demoblaze():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        welcome_page = WelcomePage(page)


        yield page, welcome_page
        page.close()
        browser.close()
        print("### Test end ###")


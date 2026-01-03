import pytest
from playwright.sync_api import sync_playwright

from globals import URL_UI, IS_HEADLESS, BROWSER
from pages.confirm_page import ConfirmPage
from pages.purchase_page import PurchasePage
from pages.reserve_page import ReservePage
from pages.welcome_page import WelcomePage


@pytest.fixture()
def setup_demoblaze():
    print("### Test start ###")

    with sync_playwright() as playwright:
        if (BROWSER == 0): browser = playwright.chromium.launch(headless=IS_HEADLESS)
        if (BROWSER == 1): browser = playwright.firefox.launch(headless=IS_HEADLESS)

        page = browser.new_page()
        page.goto(URL_UI)
        welcome_page = WelcomePage(page)
        reserve_page = ReservePage(page)
        purchase_page = PurchasePage(page)
        confirm_page = ConfirmPage(page)

        yield page, welcome_page, reserve_page, purchase_page, confirm_page
        page.close()
        browser.close()
        print("### Test end ###")

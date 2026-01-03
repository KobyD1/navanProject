import unittest
import webbrowser

import pytest
from globals import DEPARTURE_CITY, DESTINATION_CITY, USER, EXP_CURRENCY


class TestBookingFlowsUI():

    @pytest.mark.known_issue(reason="Known issue:amount at confirm page is allways 555.0")
    def test_ui_e2e_lower_price_select(self, setup_demoblaze):
        page, welcome_page, reserve_page, purchase_page, confirm_page = setup_demoblaze
        welcome_page.select_departure_and_destination(DEPARTURE_CITY, DESTINATION_CITY)
        prices = reserve_page.get_flights_prices()
        exp_price = reserve_page.select_flight_by_price(prices, True)
        purchase_page.set_user_details(USER)
        id, amount = confirm_page.get_user_details()
        assert len(id) > 0, "Empty ID  found into confirmation page"
        assert amount == exp_price, "Price at confirmation page is not as define at reserve in case of lower price "

    @pytest.mark.known_issue(reason="Known issue:amount at confirm page is allways 555.0")
    def test_ui_e2e_higher_price_select(self, setup_demoblaze):
        page, welcome_page, reserve_page, purchase_page, confirm_page = setup_demoblaze
        welcome_page.select_departure_and_destination(DEPARTURE_CITY, DESTINATION_CITY)
        prices = reserve_page.get_flights_prices()
        exp_price = reserve_page.select_flight_by_price(prices, False)
        purchase_page.set_user_details(USER)
        id, amount = confirm_page.get_user_details()
        assert len(id) > 0, "Empty ID found into confirmation page"
        assert amount == exp_price, "Price at confirmation page is not as define at reserve in case of highr price "

    def test_ui_e2e_is_currency_appears(self, setup_demoblaze):
        page, welcome_page, reserve_page, purchase_page, confirm_page = setup_demoblaze
        welcome_page.select_departure_and_destination(DEPARTURE_CITY, DESTINATION_CITY)
        prices = reserve_page.get_flights_prices()
        reserve_page.select_flight_by_price(prices, False)
        purchase_page.set_user_details(USER)
        is_currency = confirm_page.get_currency_from_confirm(EXP_CURRENCY)
        assert is_currency, "there is no currency in confirmation page"

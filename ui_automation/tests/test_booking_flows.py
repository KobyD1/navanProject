import unittest
import webbrowser


class TestBookingFlows():


    def test_e2e_lower_price_select(self,setup_demoblaze):
        page , welcome_page  = setup_demoblaze
        welcome_page.select_departure_and_destination("Boston","Paris")


    def test_demo(self):
        print ("demo")








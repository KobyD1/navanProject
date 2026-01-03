from utils.ui_utils import uiUtils


class WelcomePage(uiUtils):
    def __init__(self, page):
        self.page = page

    def select_departure_and_destination(self, departure_value, destination_value):
        departure = self.page.locator("[name='fromPort']")
        departure.select_option(departure_value)
        destination = self.page.locator("[name='toPort']")
        destination.select_option(destination_value)
        self.page.get_by_text("Find Flights").click()
        print(F"test select from {destination_value} to {destination_value} completed")

from utils.ui_utils import uiUtils


class PurchasePage(uiUtils):
    def __init__(self, page):
        self.page = page

    def set_user_details(self, user):
        name = self.page.locator("[id='inputName']")
        BasePage.clear_and_type_element(self, name, user["name"])

        address = self.page.locator("[id='address']")
        BasePage.clear_and_type_element(self, address, user["address"])

        city = self.page.locator("[id='city']")
        BasePage.clear_and_type_element(self, city, user["city"])

        state = self.page.locator("[id='state']")
        BasePage.clear_and_type_element(self, state, user["state"])

        zip = self.page.locator("[id='zipCode']")
        BasePage.clear_and_type_element(self, zip, user["zip"])

        self.page.select_option("[id='cardType']", index=user["card_type"])

        card_number = self.page.locator("[id='creditCardNumber']")
        BasePage.clear_and_type_element(self, card_number, str(user["card_number"]))

        month = self.page.locator("[id='creditCardMonth']")
        BasePage.clear_and_type_element(self, month, str(user["month"]))

        year = self.page.locator("[id='creditCardYear']")
        BasePage.clear_and_type_element(self, year, str(user["year"]))

        card_name = self.page.locator("[id='nameOnCard']")
        BasePage.clear_and_type_element(self, card_name, user["card_name"])

        self.page.get_by_text("Purchase Flight").click()

        print("credit card completed successfully")

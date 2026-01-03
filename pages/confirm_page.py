from utils.ui_utils import uiUtils


class ConfirmPage(uiUtils):
    def __init__(self, page):
        self.page = page

    def get_user_details(self):
        rows = self.page.query_selector_all("tr")
        id = rows[1].query_selector_all("td")[1].inner_text()
        amount = rows[3].query_selector_all("td")[1].inner_text()
        amount = amount.replace(" USD", "")
        amount_as_float = float(amount)
        return id, amount_as_float

    def get_currency_from_confirm(self, currency="USD"):
        rows = self.page.query_selector_all("tr")
        amount = rows[3].query_selector_all("td")[1].inner_text()
        return currency in amount

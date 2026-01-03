from utils.ui_utils import uiUtils


class ReservePage(uiUtils):
    def __init__(self, page):
        self.page = page

    def get_flights_prices(self):
        rows = self.page.query_selector_all("tr")
        prices = []
        length = len(rows)
        for i in range(1, length):
            price_text = rows[i].query_selector_all("td")[5].inner_text()
            price_as_float = (price_text.replace("$", ""))
            prices.append(price_as_float)

        return prices

    def select_flight_by_price(self, prices, is_lowest):
        if is_lowest:
            price_to_select = min(prices)
        else:
            price_to_select = max(prices)

        index = prices.index(price_to_select)
        rows = self.page.locator("tbody tr")
        rows.nth(index).locator("td").nth(0).click()
        print(f"Selecting flight by price success at row {index} ,is_lowest={is_lowest}")
        return price_to_select

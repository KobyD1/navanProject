BROWSER = 0  # 0 - chromium , 1- Firefox
IS_HEADLESS = False  # prepare for docker

URL_UI = "https://blazedemo.com/"
BASE_URL_API = "https://reqres.in/"
USERS_API = "/api/users"
DEPARTURE_CITY = "Boston"
DESTINATION_CITY = "London"
EXP_CURRENCY = "USD"

USER = {

    "name": "John Doe",
    "address": "POB 306",
    "city": "London",
    "state": "UK",
    "zip": "9410",
    "card_type": 1,
    "card_number": 123456,
    "month": 10,
    "year": 2010,
    "card_name": "john Doe"

}

MANAGER_PAYLOAD = {
    "name": "Alice",
    "job": "Manager"
}

INTERN_PAYLOAD = {
    "name": "Bob",
    "job": "Intern"
}

HEADERS = {
    'Content-Type': 'application/json'
}

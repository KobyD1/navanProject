import json

import pytest
import requests
from globals import BASE_URL_API, HEADERS, USERS_API, MANAGER_PAYLOAD, INTERN_PAYLOAD
from utils.api_utils import apiUtils


def test_api_create_manager_status_code():
    response = requests.post(BASE_URL_API + USERS_API, headers=HEADERS, data=MANAGER_PAYLOAD)
    assert response.status_code == 201, "status cose for create manager is not 201"


def test_api_create_intern_status_code():
    response = requests.post(BASE_URL_API + USERS_API, headers=HEADERS, data=INTERN_PAYLOAD)
    assert response.status_code == 201, "status cose for create intern is not 201"


def test_api_policy_select():
    response = requests.post(BASE_URL_API + USERS_API, headers=HEADERS, data=json.dumps(INTERN_PAYLOAD))
    apiUtils.select_policy_by_response(response)
    response = requests.post(BASE_URL_API + USERS_API, headers=HEADERS, data=json.dumps(MANAGER_PAYLOAD))
    apiUtils.select_policy_by_response(response)


def test_api_negative_missing_job():
    payload_missing_job = {
        "name": "Bob",
        "job": ""
    }
    response = requests.post(BASE_URL_API + USERS_API, headers=HEADERS, data=json.dumps(payload_missing_job))
    assert response.status_code == 400, "status cose for create user without job is not 400"
    error = response.json()["error"]
    assert error == "Missing data in required field : 'job'", "there is no data (Manager, Intern...) in required field : 'job'"


# @pytest.mark.skip(reason="Example  for passed ,test VS implemented API server")
def test_api_post_vs_implemented_api():
    url_base = 'https://petstore.swagger.io/v2/'
    headers = {'Content-Type': 'application/json'}
    user = {
        "id": 3333,
        "username": "user1",
        "firstName": "John",
        "lastName": "David",
        "email": "abc@gmail.com",
        "password": "123456",
        "phone": "054123456",
        "userStatus": 0
    }
    response = requests.post(url_base + 'user', headers=headers, data=json.dumps(user))
    response_code = response.status_code
    assert response_code == 200
    message = response.json()["message"]
    assert message == '3333'

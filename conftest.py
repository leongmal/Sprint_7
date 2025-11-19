import pytest
import requests
from helper import CourierFactory
from urls import Url



@pytest.fixture(scope='function')
def courier():
    created_body = CourierFactory.courier_body_random_name_pass()
    
    create_courier = requests.post(Url.BASE_URL + Url.CREATE_COURIER_PATH, json=created_body)
    auth_body = {"login": created_body["login"],"password": created_body["password"]}

    auth_courier = requests.post(Url.BASE_URL + Url.LOGIN_COURIER_PATH, json=auth_body)
    auth_data = auth_courier.json()
    current_data ={
        "login": created_body["login"],
        "id": auth_data["id"],
        "password": created_body["password"],
        "create_courier" : create_courier,
        }

    yield  current_data

    delete_courier = requests.delete(Url.BASE_URL + Url.DELETE_COURIER_PATH + "/" + str(current_data['id']))


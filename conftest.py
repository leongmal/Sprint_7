import pytest
import requests
# from api.create_courier import CreateCourier
from helper import CourierFactory
from urls import Url



@pytest.fixture(scope='function')
def courier():
    created_body = CourierFactory.courier_body_random_name_pass()
    # Шаг 1: создаём курьера
    create_courier = requests.post(Url.BASE_URL + Url.CREATE_COURIER_PATH, json=created_body)
    # assert create_response.status_code == 201, ( f"Создание курьера failed: {create_response.status_code}")
    # print(create_courier.status_code, f"---создали курьера")

    # Шаг 2: авторизуем, чтобы получить id
    auth_body = {"login": created_body["login"],"password": created_body["password"]}

    auth_courier = requests.post(Url.BASE_URL + Url.LOGIN_COURIER_PATH, json=auth_body)
    # assert auth_response.status_code == 200, (f"Авторизация failed: {auth_response.status_code}")
    # print(auth_courier.status_code, f"---авторизировали курьера")

    auth_data = auth_courier.json()
    # # assert "id" in auth_data, "В ответе нет поля 'id'"
    # print(auth_data["id"], f"---id курьера")
    current_data ={
        # "cod_create" : create_response,
        "login": created_body["login"],
        "id": auth_data["id"],
        "password": created_body["password"],
        "create_courier" : create_courier,
        "auth_courier" : auth_courier
        }

    yield  current_data
    delete_courier = requests.delete(Url.BASE_URL + Url.DELETE_COURIER_PATH + "/" + str(current_data['id']))
    # print(delete_courier.status_code, f"---удалили курьера")
# courier()

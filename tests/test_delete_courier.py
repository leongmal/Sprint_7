import allure
import pytest
import requests
from urls import Url

@allure.feature("Курьер")
class TestCourier:

#     @allure.title("Создание курьера и его удаление после теста")
#     def test_create_and_delete_courier(self, created_courier):
#         # Тест использует фикстуру: курьер создаётся ДО теста, удаляется ПОСЛЕ
#         # assert "id" in created_courier, "В ответе нет 'id' курьера"
#         # assert isinstance(created_courier["id"], int), "'id' должен быть числом"

#     @allure.title("Авторизация созданного курьера")
#     def test_authorize_created_courier(self, created_courier):
#         auth_body = {"login": created_courier["login"], "password": created_courier["password"]}
#         response = requests.post(Url.BASE_URL + Url.LOGIN_COURIER_PATH, json=auth_body)

#         print(response.json()['id'])
#         # assert response.status_code == 200, (
#         #     f"Авторизация не удалась: {response.status_code}, {response.text}"
#         # )
    def test_authorize_created_courier(self, created_courier):
            auth_body = {"login": created_courier["login"], "password": created_courier["password"]}
            response = requests.post(Url.BASE_URL + Url.LOGIN_COURIER_PATH, json=auth_body)

#             print(response.json()['id'])

# test_authorize_created_courier()

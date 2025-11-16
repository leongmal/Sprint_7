import requests
import allure
from urls import Url



@allure.feature("Получение списка заказов")
class TestOrdersList:

    @allure.title("Проверка, что ответ содержит список заказов")
    @allure.description("Запрос к таблице заказов")
    def test_orders_response_is_list(self):
        response = requests.get(Url.BASE_URL+Url.LIST_ORDER_PATH)
        response_json = response.json()

        assert isinstance(response_json["orders"], list)

import requests
import allure
from urls import Url
from helper import OrderFactory



class CreateOrder:
    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(body: dict):
        response = requests.post(Url.BASE_URL + Url.CREATE_ORDER_PATH, headers={"Content-Type": "application/json"}, json=body)
        return response


    @staticmethod
    @allure.step("Создание заказа с указанными цветами")
    def create_order_with_colors(colors: list = None):
        body = OrderFactory.generate_order_body()
        if colors is not None:
            body["color"] = colors
        else:
            body.pop("color", None)
            
        return CreateOrder.create_order(body)

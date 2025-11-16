import requests
from urls import Url
import allure
from helper import CourierFactory



class CreateCourier:
    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(Url.BASE_URL+Url.CREATE_COURIER_PATH, json=body, headers={"Content-Type": "application/json"})


    @staticmethod
    @allure.step("Отправка запроса на создание одинаковых курьеров")
    def not_create_courier_double(body):
        requests.post(Url.BASE_URL+Url.CREATE_COURIER_PATH, json=body, headers={"Content-Type": "application/json"})
        return requests.post(Url.BASE_URL+Url.CREATE_COURIER_PATH, json=body, headers={"Content-Type": "application/json"})



    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера")
    def success_authorization():
        body = CourierFactory.courier_body_random_name_pass()
        CreateCourier.create_courier(body)
        auth_body = {"login": body["login"],
                    "password": body["password"]}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)


    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера без 'login'")
    def authorization_no_login():
        body = CourierFactory.courier_body_random_name_pass()
        CreateCourier.create_courier(body)
        auth_body = {"password": body["password"]}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)


    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера без 'password'")
    def authorization_no_password():
        body = CourierFactory.courier_body_random_name_pass()
        CreateCourier.create_courier(body)
        auth_body = {"login": body["login"]}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)


    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера, неверный логин")
    def authorization_incorrect_login():
        body = CourierFactory.courier_body_random_name_pass()
        CreateCourier.create_courier(body)
        auth_body = {"login": body["login"] +'Y',
                    "password": body["password"]}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)


    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера, неверный пароль")
    def authorization_incorrect_password():
        body = CourierFactory.courier_body_random_name_pass()
        CreateCourier.create_courier(body)
        auth_body = {"login": body["login"] ,
                    "password": body["password"]+'Y'}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)


    @staticmethod
    @allure.step("авторизоваться под несуществующим пользователем")
    def autorozation_no_regisration():
        body = CourierFactory.courier_body_random_name_pass()
        auth_body = {"login": body["login"],
                    "password": body["password"]}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)

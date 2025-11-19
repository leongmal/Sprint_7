import requests
from urls import Url
import allure
from helper import CourierFactory



class CreateCourier:
    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(Url.BASE_URL + Url.CREATE_COURIER_PATH, json=body, headers={"Content-Type": "application/json"})


    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера")
    def success_authorization():
        body = CourierFactory.courier_body_random_name_pass()
        CreateCourier.create_courier(body)
        auth_body = {"login": body["login"],
                    "password": body["password"]}

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)


    @staticmethod
    @allure.step("отправка запроса на создание курьера без 'login'")
    def request_no_login():
        body = CourierFactory.courier_body_random_name_pass()
        body_no_login =CourierFactory.remove_field(body, 'login')
        return  CreateCourier.create_courier(body_no_login)



    @staticmethod
    @allure.step("отправка запроса на создание курьера без 'password'")
    def request_no_password():
        body = CourierFactory.courier_body_random_name_pass()
        body_copy = body.copy()
        body_copy['password'] = " "
        return  body_copy['password']
        

    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера без 'login'")
    def request_auth__no_login():
        body = CourierFactory.courier_body_random_name_pass()
        body_no_login =CourierFactory.remove_field(body, 'login')

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=body_no_login)
    

    @staticmethod
    @allure.step("отправка запроса на авторизацию курьера без 'password'")
    def request_auth__no_password():
        body = CourierFactory.courier_body_random_name_pass()
        body_copy = body.copy()
        body_copy['password'] = ""
        body_no_password = body_copy['password']

        return requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=body_no_password)
        

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

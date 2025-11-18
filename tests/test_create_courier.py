import allure
from api.create_courier import CreateCourier
from helper import CourierFactory
from data import Response



class TestCreateCourer:
    @allure.title("Проверка успешного создания курьера")
    @allure.description("запрос возвращает правильный код ответа '{ok:true}' ")
    def test_create_courier_status(self, courier):
        create_courier_request = courier["create_courier"]

        assert (create_courier_request.status_code == 201
                and create_courier_request.text == Response.CREATE_OK)


    @allure.title("Проверка запрета на создание двух одинаковых курьеров")
    @allure.description("Проверка создания пользователя с логином, который уже есть, возвращается ошибка status=409")
    def test_you_cannot_create_identical_couriers_code(self,courier):
        duplicate_body = {"login": courier["login"],"password": courier["password"]}
        response = CreateCourier.create_courier(duplicate_body)

        assert (response.status_code == 409
                and Response.USERNAME_IS_TAKEN in response.json()["message"])


    @allure.title("Если нет одного из полей, поля 'login', запрос возвращает ошибку")
    @allure.description("Проверка,чтобы создать курьера, обязательностьполя 'login'")
    def test_login_is_required(self):
        response = CreateCourier.authorization_no_login()

        assert (response.status_code == 400 and
                response.json().get('message') == Response.NOT_ENOUNGH_DATA)


    @allure.title("Если нет одного из полей, поля 'password', запрос возвращает ошибку")
    @allure.description("Проверка,чтобы создать курьера, обязательность поля 'password'")
    def test_password_is_required(self):
        body = CourierFactory.courier_body_random_name_pass()
        body_copy = body.copy()
        body_copy['password'] = " "
        response = CreateCourier.create_courier(body_copy['password'])

        assert (response.status_code == 400 and response.json()["code"] == 400)

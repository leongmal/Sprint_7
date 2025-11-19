import allure
from api.create_courier import CreateCourier
from data import Response


class TestAuthorisationCourier:

    @allure.title("Проверка, что курьер может авторизоваться")
    @allure.description("Проверка, успешный запрос возвращает id")
    def test_success_authorisaton_id(self):
        response = CreateCourier.success_authorization()

        assert (response.status_code == 200 and
                 "id" in response.text)


    @allure.title("Если какого-то поля нет, запрос возвращает ошибку")
    @allure.description("Для авторизации нужно передать все обязательные поля. Пустое поле 'login'")
    def test_authorisation_no_login(self):
        response = CreateCourier.request_auth__no_login()

        assert (response.status_code == 400 and
                response.json()['message'] == "Недостаточно данных для входа")


    @allure.title("Если какого-то поля нет, запрос возвращает ошибку")
    @allure.description("Для авторизации нужно передать все обязательные поля. Пустое поле 'password'")
    def test_authorisation_no_password(self):
        response = CreateCourier.request_auth__no_password()

        assert (response.status_code == 400 and response.json()['code'] == 400)

    @allure.title("Проверка авторизации с неверными данными /логин")
    @allure.description("При авторизации система вернёт ошибку, если неправильно указать логин")
    def test_incorrect_login(self):
        response = CreateCourier.authorization_incorrect_login()

        assert (response.status_code == 404  and
                response.json()['message'] == Response.AUTHORIZATION_NEGATIV)

    @allure.title("Проверка авторизации с неверными данными /пароль")
    @allure.description("система вернёт ошибку, если неправильно указать пароль")
    def test_incorrect_password(self):
        response = CreateCourier.authorization_incorrect_password()

        assert (response.status_code == 404  and
                response.json()['message'] == Response.AUTHORIZATION_NEGATIV)

    @allure.title("Проверка авторизации с несуществующими данными")
    @allure.description("Система вернёт ошибку, если авторизоваться с несуществующими данными")
    def test_incorrect_authorization(self):
        response = CreateCourier.autorozation_no_regisration()

        assert (response.status_code == 404  and
                response.json()['message'] == Response.AUTHORIZATION_NEGATIV)

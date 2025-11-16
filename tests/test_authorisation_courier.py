import allure
from api.create_courier import CreateCourier



class TestAuthorisationCourier:
    @allure.title("Проверка, курьер может авторизоваться")
    @allure.description("Проверка успешной авторизации")
    def test_success_authorisaton(self):
        response = CreateCourier.success_authorization()

        assert response.status_code == 200


    @allure.description("Проверка,успешный запрос возвращает id")
    def test_success_authorisaton_id(self):
        response = CreateCourier.success_authorization()

        assert  "id" in response.text


    @allure.title("если какого-то поля нет, запрос возвращает ошибку")
    @allure.description("для авторизации нужно передать все обязательные поля. Пустое поле 'login'")
    def test_authorisation_no_login(self):
        response = CreateCourier.authorization_no_login()

        assert (response.status_code == 400 and
                response.json()['message'] == "Недостаточно данных для входа")


    @allure.title("если какого-то поля нет, запрос возвращает ошибку")
    @allure.description("для авторизации нужно передать все обязательные поля. Пустое поле 'password'")
    def test_authorisation_no_password(self):
        response = CreateCourier.authorization_no_password()

        assert (response.status_code == 400 and
                response.json()['message'] == "Недостаточно данных для входа")


    @allure.description("система вернёт ошибку, если неправильно указать логин")
    def test_incorrect_login(self):
        response = CreateCourier.authorization_incorrect_login()

        assert response.json()['message'] == "Учетная запись не найдена"


    @allure.description("система вернёт ошибку, если неправильно указать пароль")
    def test_incorrect_password(self):
        response = CreateCourier.authorization_incorrect_password()

        assert response.json()['message'] == "Учетная запись не найдена"


    @allure.description("система вернёт ошибку, если авторизоваться под несуществующим пользователем")
    def test_incorrect_authorization(self):
        response = CreateCourier.autorozation_no_regisration()

        assert response.json()['message'] == "Учетная запись не найдена"

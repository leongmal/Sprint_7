import allure
from api.create_courier import CreateCourier
from helper import CourierFactory


class TestCreateCourer:
    @allure.title("Проверка успешного создания курьера")
    @allure.description("запрос возвращает правильный код ответа")
    def test_create_courier_status(self):
        create_courier_request = CreateCourier.create_courier(CourierFactory.courier_body_random_name_pass())

        assert create_courier_request.status_code == 201


    @allure.description("Проверка код ответа, 'Нельзя двух одинаковых курьеров'")
    def test_you_cannot_create_identical_couriers_code(self):
        body = CourierFactory.courier_body_random_name_pass()
        response = CreateCourier.not_create_courier_double(body)

        assert response.status_code == 409


    @allure.title("если одного из полей, поля 'login', запрос возвращает ошибку")
    @allure.description("Проверка,чтобы создать курьера, обязательностьполя 'login'")
    def test_login_is_required(self):
        body = CourierFactory.courier_body_random_name_pass()
        body_no_login =CourierFactory.remove_field(body, 'login')
        response = CreateCourier.create_courier(body_no_login)

        assert (response.status_code == 400 and
                response.json().get('message') == "Недостаточно данных для создания учетной записи")


    @allure.title("если одного из полей, поля 'password', запрос возвращает ошибку")
    @allure.description("Проверка,чтобы создать курьера, обязательность поля 'password'")
    def test_password_is_required(self):
        body = CourierFactory.courier_body_random_name_pass()
        body_no_password =CourierFactory.remove_field(body, 'password')
        response = CreateCourier.create_courier(body_no_password)

        assert (response.status_code == 400 and
                response.json().get('message') == "Недостаточно данных для создания учетной записи")


    @allure.title("если одного из полей, поля 'firstName', запрос возвращает ошибку")
    @allure.description("Проверка,чтобы создать курьера, обязательность поля 'firstName'")
    def test_password_is_required(self):
        body = CourierFactory.courier_body_random_name_pass()
        body_no_firstName =CourierFactory.remove_field(body, 'firstName')
        response = CreateCourier.create_courier(body_no_firstName)

        assert response.status_code == 400


    @allure.description("Проверка успешный запрос возвращает {'ok':true};")
    def test_create_courier_text(self):
        create_courier_request = CreateCourier.create_courier(CourierFactory.courier_body_random_name_pass())

        assert (create_courier_request.text == '{"ok":true}')


    @allure.description("Проверка если создать пользователя с логином, который уже есть, возвращается ошибка.")
    def test_you_cannot_create_identical_text(self):
        body = CourierFactory.courier_body_random_name_pass()
        response = CreateCourier.not_create_courier_double(body)

        assert  response.json().get('message')=="Этот логин уже используется"

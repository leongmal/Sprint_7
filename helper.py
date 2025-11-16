import allure
from faker import Faker



# class CourierFactory:
#     @staticmethod
#     @allure.step("Генерация body для создания курьера")
#     def courier_body_random_name_pass():
#         faker = Faker('ru_RU')
#         body={"login": faker.user_name(),
#               "password": faker.password(),
#               "firstName": faker.first_name()}

#         return body


    # @staticmethod
    # @allure.step("Удаление поля из тела заказа")
    # def remove_field(body: dict, field: str) -> dict:
    #     copied = body.copy()
    #     copied.pop(field, None)
    #     return copied




class OrderFactory:
    @staticmethod
    @allure.step("Генерация body для создания заказа с рандомными данными")
    def generate_order_body() -> dict:
        faker = Faker('ru_RU')
        return {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "address": 'Konoha, 142 apt.',
            "metroStation": 4,
            "phone": faker.phone_number(),
            "rentTime": 5,
            "deliveryDate": "2025-12-06",
            "comment": faker.sentence(),
            "color": []  # по умолчанию без цветов
        }

import pytest
from api.create_courier import CreateCourier
# from helper import CourierFactory
from faker import Faker
from urls import Url
import requests

@pytest.fixture
def created_courier():
    # 1. Создаём курьера
    # body = CourierFactory.courier_body_random_name_pass()
    response = CreateCourier.create_courier(body)
    faker = Faker('ru_RU')
    body={"login": faker.user_name(),
          "password": faker.password(),
          "firstName": faker.first_name()}

    copied = body.copy()
    auth_body = copied.pop("firstName", None)

    response = requests.post(Url.BASE_URL+Url.LOGIN_COURIER_PATH, json=auth_body)
    id = response.json()["id"]

    itog = requests.delete(Url.BASE_URL+Url.DELETE_COURIER +"/"+{id})
    print(itog.status_code)

created_courier()

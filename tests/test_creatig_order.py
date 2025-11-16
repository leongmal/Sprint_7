import pytest
import allure
from api.create_orders import CreateOrder


@allure.feature("Создание заказа")
@allure.story("Проверка параметров цвета при создании заказа")
class TestOrderCreation:

    @pytest.mark.parametrize(
        "colors, expected_color_set",[(["BLACK"], {"BLACK"}),(["GREY"], {"GREY"}),(["BLACK", "GREY"], {"BLACK", "GREY"}),(None, set())],
        ids=["один цвет BLACK","один цвет GREY","два цвета BLACK и GREY","без указания цвета"])
    @allure.title("Создание заказа с цветами: {colors}")
    def test_order_creation_with_colors(self, colors, expected_color_set):

        response = CreateOrder.create_order_with_colors(colors)
        response_json = response.json()

        assert  (response.status_code == 201 and isinstance(response_json["track"], (str, int)))

import allure
import pytest

from helpers import Helpers as help
from data import HttpMethods, Endpoints, ResponseTexts
from conftest import api_client


class TestCreateOrder:

    @allure.title('Тест создания заказов')
    def test_create_order_authorize(self, api_client):
        token = help.authorize(api_client)
        data = {"ingredients": ["61c0c5a71d1f82001bdaaa75","61c0c5a71d1f82001bdaaa6d"]}
        response = api_client.send_request(HttpMethods.post, Endpoints.ORDERS, data, headers={"Authorization": token})
        assert response.status_code == 200
        assert 'name', 'order' in response.text
        assert '"success":true' in response.text

    @pytest.mark.xfail(reason="Фактическое поведение не соответствует ожидаемому в документации")
    @allure.title('Тест создания заказов без регистрации')
    def test_create_order_non_authorize(self, api_client):
        data = {"ingredients": ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6d"]}
        response = api_client.send_request(HttpMethods.post, Endpoints.ORDERS, data)
        assert 'login' in response.url

    @allure.title('Тест создания заказов c ингредиентами/без ингредиентов')
    @pytest.mark.parametrize('ingredients, success', [(["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6d"], 'true'), ([], 'false')])
    def test_create_order_with_without_ingredients(self, api_client, ingredients, success):
        token = help.authorize(api_client)
        data = {"ingredients": ingredients}
        response = api_client.send_request(HttpMethods.post, Endpoints.ORDERS, data, headers={"Authorization": token})
        success = f'"success":{success}'
        if not ingredients:
            formated_response = help.formate_response(response.status_code, response.text)
            assert formated_response == ResponseTexts.order_without_ingredients
        assert success in response.text

    @allure.title('Тест создания заказов c неверным хэшем ингредиентов')
    def test_create_order_with_incorrect_ingredients(self, api_client):
        token = help.authorize(api_client)
        data = {"ingredients": ["lol", "kek"]}
        response = api_client.send_request(HttpMethods.post, Endpoints.ORDERS, data, headers={"Authorization": token})
        assert response.status_code == ResponseTexts.incorrect_hash_code


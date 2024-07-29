import allure
import pytest

from helpers import Helpers as help
from data import HttpMethods, Endpoints, ResponseTexts
from conftest import api_client


class TestGetOrder:

    @allure.title('Тест создания заказов конкретного пользователя c авторизацией')
    def test_get_order_by_authorize(self, api_client):
        order_id, token = help.create_user_and_order(api_client)
        response = api_client.send_request(HttpMethods.get, Endpoints.ORDERS, headers={"Authorization": token})
        assert response.json()['orders'][0]['number'] == order_id
    @allure.title('Тест получения заказов без авторизации')
    def test_get_order_non_authorize(self, api_client):
        help.create_user_and_order(api_client)
        response = api_client.send_request(HttpMethods.get, Endpoints.ORDERS)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.get_order_non_authorize

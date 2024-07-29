import allure

from helpers import Helpers as help
from conftest import api_client
from data import Endpoints, HttpMethods, ResponseTexts


class TestChangeUser:

    @allure.title('Тест изменения авторизованного юзера')
    def test_create_user_authorize(self, api_client):
        token = help.authorize(api_client)
        data = help.generate_user_data()
        response = api_client.send_request(HttpMethods.patch, Endpoints.USER, data, headers={"Authorization": token})
        assert response.json()['user']['name'] == data['name']
        assert response.json()['user']['email'] == data['email']

    @allure.title('Тест изменения неавторизованного юзера')
    def test_create_user_authorize(self, api_client):
        data = help.generate_user_data()
        response = api_client.send_request(HttpMethods.patch, Endpoints.USER, data)
        formatted_response = help.formate_response(response.status_code, response.text)
        assert formatted_response == ResponseTexts.change_user_data_non_authorize

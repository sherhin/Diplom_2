import allure
import pytest

from helpers import Helpers as help
from conftest import api_client
from data import Endpoints, HttpMethods, ResponseTexts


class TestCreateUser:

    @allure.title('Тест создания юзера')
    def test_create_user(self, api_client):
        data = help.generate_user_data()
        response = api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        assert response.status_code == ResponseTexts.user_created_code
        assert 'user' in response.text
        assert 'accessToken', 'refreshToken' in response.text

    @allure.title('Тест создания юзера с данными уже существующего')
    def test_create_user_exists_negative(self, api_client):
        data = help.generate_user_data()
        api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        second_response = api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        formated_response = help.formate_response(second_response.status_code, second_response.text)
        assert formated_response == ResponseTexts.user_exists

    @allure.title('Тест создания юзера без обязательных полей')
    @pytest.mark.parametrize('field', ['name', 'password'])
    def test_create_user_without_req_fields_negative(self, api_client, field):
        data = help.generate_user_data()
        if data.get(field):
            data[field] = None
        response = api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.user_without_required_fields

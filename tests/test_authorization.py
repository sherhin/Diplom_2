import allure

from helpers import Helpers as help
from conftest import api_client
from data import Endpoints, HttpMethods, ResponseTexts


class TestUserAuthorization:

    @allure.title('Тест авторизации юзера')
    def test_login_user(self, api_client):
        data = help.generate_user_data()
        help.create_user(api_client, data)
        response = api_client.send_request(HttpMethods.post, Endpoints.AUTHORIZATION, data)
        assert response.status_code == ResponseTexts.user_authorizated_code

    @allure.title('Тест авторизации юзера с несуществующими данными')
    def test_login_user_not_exists_negative(self, api_client):
        data = {
            'email': 'fakeemail@mail.ru',
            'password': 'fakepassword'
        }
        response = api_client.send_request(HttpMethods.post, Endpoints.AUTHORIZATION, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.user_bad_authorization

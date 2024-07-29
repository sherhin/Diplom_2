from faker import Faker
from conftest import api_client
from data import HttpMethods, Endpoints


class Helpers:

    @staticmethod
    def generate_user_data():
        fake = Faker()
        random_login = fake.user_name()
        random_password = fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        random_email = fake.email()
        data = {
            'email': random_email,
            'password': random_password,
            'name': random_login
        }
        return data


    @staticmethod
    def formate_response(status_code, message):
        format_response = [status_code, message]
        return format_response

    @staticmethod
    def create_user(api_client, data):
        user = api_client.send_request(HttpMethods.post, Endpoints.REGISTER, data)
        return user

    @staticmethod
    def authorize(api_client, user_data=False):
        if not user_data:
            user_data = Helpers.generate_user_data()
        Helpers.create_user(api_client, user_data)
        response = api_client.send_request(HttpMethods.post, Endpoints.AUTHORIZATION, user_data)
        return response.json()['accessToken']

    @staticmethod
    def create_user_and_order(api_client):
        user_data = Helpers.generate_user_data()
        Helpers.create_user(api_client, user_data)
        token = Helpers.authorize(api_client)
        order_data = {"ingredients": ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6d"]}
        order = api_client.send_request(HttpMethods.post, Endpoints.ORDERS, order_data, headers={"Authorization": token})
        order_id = order.json()['order']['number']
        return order_id, token


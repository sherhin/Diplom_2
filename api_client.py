import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, method, endpoint, data=None, headers=None):
        url = self.base_url + endpoint
        response = requests.request(method, url, json=data, headers=headers)
        return response

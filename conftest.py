import pytest

from data import Endpoints
from api_client import ApiClient

@pytest.fixture
def api_client():
    api_client = ApiClient(base_url=Endpoints.BASE)
    return api_client



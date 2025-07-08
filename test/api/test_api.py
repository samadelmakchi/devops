
import requests
import pytest

def test_api_endpoint():
    response = requests.get("http://your-app-host/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
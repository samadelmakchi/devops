import os
import requests
import pytest

@pytest.fixture
def api_url():
    """دریافت آدرس API از متغیر محیطی"""
    return os.getenv("APP_URL")

def test_user_creation_and_retrieval(api_url):
    """تست ایجاد و بازیابی کاربر از طریق API"""
    # ایجاد کاربر
    create_response = requests.post(f"{api_url}/users", json={"name": "Test User", "email": "test@example.com"})
    assert create_response.status_code == 201
    user_id = create_response.json().get("id")

    # بازیابی کاربر
    get_response = requests.get(f"{api_url}/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test User"
    assert get_response.json()["email"] == "test@example.com"

def test_invalid_user_creation(api_url):
    """تست ایجاد کاربر با داده نامعتبر"""
    response = requests.post(f"{api_url}/users", json={"name": "", "email": "invalid"})
    assert response.status_code == 400
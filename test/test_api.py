import requests
import pytest

BASE_URL = "http://api.example.com/users"

@pytest.fixture
def user_data():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_get_users():
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "GET users failed"
    assert isinstance(response.json(), list), "Response is not a list of users"

def test_create_user(user_data):
    response = requests.post(BASE_URL, json=user_data)
    assert response.status_code == 201, "User creation failed"
    data = response.json()
    assert data['name'] == user_data['name'], "User name mismatch"
    assert data['email'] == user_data['email'], "User email mismatch"

def test_update_user(user_data):
    # ایجاد کاربر جدید برای بروزرسانی
    create_response = requests.post(BASE_URL, json=user_data)
    user_id = create_response.json()["id"]

    updated_data = {
        "name": "John Updated",
        "email": "john.updated@example.com"
    }

    update_response = requests.put(f"{BASE_URL}/{user_id}", json=updated_data)
    assert update_response.status_code == 200, "User update failed"

    data = update_response.json()
    assert data['name'] == updated_data['name'], "User name not updated"
    assert data['email'] == updated_data['email'], "User email not updated"

def test_delete_user(user_data):
    # ابتدا یک کاربر جدید ایجاد می‌کنیم
    create_response = requests.post(BASE_URL, json=user_data)
    user_id = create_response.json()["id"]

    # حذف کاربر
    delete_response = requests.delete(f"{BASE_URL}/{user_id}")
    assert delete_response.status_code == 204, "User deletion failed"

    # بررسی می‌کنیم که کاربر دیگر وجود نداشته باشد
    get_response = requests.get(f"{BASE_URL}/{user_id}")
    assert get_response.status_code == 404, "User still exists after deletion"


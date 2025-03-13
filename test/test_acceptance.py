import requests

def test_user_registration_acceptance():
    user_data = {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "strong_password"
    }
    response = requests.post("http://localhost:8000/api/register", json=user_data)
    assert response.status_code == 201, "User registration failed"
    assert response.json()["message"] == "Registration successful"

def test_user_login_acceptance():
    login_data = {"username": "new_user", "password": "strong_password"}
    response = requests.post("http://localhost:8000/api/login", json=login_data)
    assert response.status_code == 200, "Login failed"
    assert "token" in response.json(), "Login token not found"


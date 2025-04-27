import requests

def test_english_localization():
    response = requests.get("http://localhost:8000/api/welcome?lang=en")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome", "English localization failed"

def test_spanish_localization():
    response = requests.get("http://localhost:8000/api/welcome?lang=es")
    assert response.status_code == 200
    assert response.json()["message"] == "Bienvenido", "Spanish localization failed"


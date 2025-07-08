import os
import requests
import pytest

@pytest.fixture
def app_url():
    """دریافت آدرس برنامه از متغیر محیطی"""
    return os.getenv("APP_URL")

def test_sql_injection_vulnerability(app_url):
    """تست آسیب‌پذیری تزریق SQL"""
    payload = {"username": "admin' OR '1'='1", "password": "test"}
    response = requests.post(f"{app_url}/login", data=payload)
    assert response.status_code != 200, "Potential SQL Injection vulnerability detected"
    assert "login failed" in response.text.lower()

def test_xss_vulnerability(app_url):
    """تست آسیب‌پذیری XSS"""
    payload = {"search": "<script>alert('xss')</script>"}
    response = requests.get(f"{app_url}/search", params=payload)
    assert response.status_code == 200
    assert "<script>" not in response.text, "Potential XSS vulnerability detected"
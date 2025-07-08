import os
import requests
import pytest

@pytest.fixture
def app_url():
    """دریافت آدرس برنامه از متغیر محیطی"""
    return os.getenv("APP_URL")

def test_homepage_access(app_url):
    """تست دسترسی به صفحه اصلی"""
    response = requests.get(f"{app_url}/")
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_api_health_check(app_url):
    """تست بررسی سلامت API"""
    response = requests.get(f"{app_url}/health")
    assert response.status_code == 200
    assert response.json().get("status") == "healthy"
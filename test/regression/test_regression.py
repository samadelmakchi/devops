import os
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    """تنظیم درایور Selenium"""
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=os.getenv("SELENIUM_HUB_URL"), options=options)
    yield driver
    driver.quit()

@pytest.fixture
def app_url():
    """دریافت آدرس برنامه از متغیر محیطی"""
    return os.getenv("APP_URL")

def test_login_functionality(driver, app_url):
    """تست عملکرد ورود به سیستم"""
    driver.get(f"{app_url}/login")
    driver.find_element(By.NAME, "username").send_keys("test_user")
    driver.find_element(By.NAME, "password").send_keys("test_password")
    driver.find_element(By.ID, "submit").click()
    assert "Dashboard" in driver.title

def test_api_user_list(app_url):
    """تست لیست کاربران از API"""
    response = requests.get(f"{app_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
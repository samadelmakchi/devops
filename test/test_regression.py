from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    # پیکربندی برای استفاده از Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_regression(setup):
    driver = setup
    driver.get("http://your-website-url/login")  # URL لاگین وب‌سایت شما

    # تست ورود با اطلاعات کاربری درست
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    username_input.send_keys("valid_user")
    password_input.send_keys("valid_password")
    login_button.click()

    # انتظار داریم که پس از ورود موفق به صفحه داشبورد هدایت شویم
    assert "Dashboard" in driver.page_source, "Login failed or regression issue occurred"

def test_logout_regression(setup):
    driver = setup
    driver.get("http://your-website-url/login")
    
    # مشابه تست ورود، لاگین انجام می‌شود
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    username_input.send_keys("valid_user")
    password_input.send_keys("valid_password")
    login_button.click()

    # تست لاگ‌اوت
    logout_button = driver.find_element(By.ID, "logout-btn")
    logout_button.click()

    # بررسی اینکه آیا دوباره به صفحه لاگین هدایت شده‌ایم
    assert "Login" in driver.page_source, "Logout failed or regression issue occurred"


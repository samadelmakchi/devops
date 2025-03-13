from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_ui():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    username_input.send_keys("test_user")
    password_input.send_keys("test_password")
    login_button.click()

    assert "Dashboard" in driver.page_source, "Login failed"
    driver.quit()

def test_signup_ui():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/signup")

    username_input = driver.find_element(By.NAME, "username")
    email_input = driver.find_element(By.NAME, "email")
    signup_button = driver.find_element(By.ID, "signup-btn")

    username_input.send_keys("new_user")
    email_input.send_keys("new_user@example.com")
    signup_button.click()

    assert "Signup successful" in driver.page_source, "Signup failed"
    driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
    yield driver
    driver.quit()

def test_homepage(driver):
    driver.get("http://your-app-host")
    assert "Welcome" in driver.find_element(By.TAG_NAME, "h1").text
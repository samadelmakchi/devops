
from selenium import webdriver
from pytest_axe import Axe
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
    yield driver
    driver.quit()

def test_accessibility(driver):
    driver.get("http://your-app-host")
    axe = Axe(driver)
    results = axe.run()
    assert len(results["violations"]) == 0, f"Accessibility violations found: {results['violations']}"
import pytest
import time
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    options = Options()
 #   options.add_argument("--headless=new")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_amazon_title(driver):
    driver.get("https://amazon.co.uk")
    time.sleep(3)

    # Take screenshot and attach to Allure
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name="Amazon Homepage", attachment_type=allure.attachment_type.PNG)

    # Intentional failure
 #   assert "NonexistentTitle" in driver.title

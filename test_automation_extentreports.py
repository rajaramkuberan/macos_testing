import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless=new")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_amazon_title(driver, pytestconfig):
    driver.get("https://amazon.co.uk")
    time.sleep(5)

    # Take screenshot and save to folder
    reports_dir = os.path.join(os.getcwd(), "Reports")
    os.makedirs(reports_dir, exist_ok=True)
    screenshot_path = os.path.join(reports_dir, "amazon_homepage.png")
    driver.save_screenshot(screenshot_path)

    # Attach screenshot to ExtentReport
    pytestconfig.extent.attach.file(screenshot_path, name="Amazon Homepage")

    # Intentional failure
 #   assert "NonexistentTitle" in driver.title

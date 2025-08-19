from selenium import webdriver
import time

# Create a Safari WebDriver instance
driver = webdriver.Safari()

driver.maximize_window()

# Navigate to Google
driver.get("https://amazon.co.uk")

# Wait for a few seconds (optional)
time.sleep(10)

# Close the browser
driver.quit()

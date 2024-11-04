from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import time as _time, sleep as _sleep

# Initialize the Chrome WebDriver

# download driver (optional with latest version of selenium):
# 1. Check chrome version: Chrome Browser > 3-dots > Help > About Google Chrome >> 130.0.6723.70
# 2. Download compatible driver from https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
# example: https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.69/win64/chromedriver-win64.zip is compatible with 130.0.6723.70
# 3. Extract downloaded webdriver to any location. Example: C:/Users/ssharma/software/chromedriver-win64/

# Initial the driver
driver = webdriver.Chrome(service=webdriver.ChromeService())

# Open a website
driver.get("https://www.google.com")

_sleep(15)

# Find the search box element
search_box = driver.find_element(By.NAME, 'q')

# Enter the search term
search_box.send_keys("Selenium automation")

_sleep(15)

# Simulate pressing the Enter key
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds (optional)
driver.implicitly_wait(600)

# Print the title of the results page
print(driver.title)

_sleep(100)

# Close the browser
# driver.quit()

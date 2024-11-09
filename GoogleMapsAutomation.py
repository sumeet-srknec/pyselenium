from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import time as _time, sleep as _sleep

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=webdriver.ChromeService())

# Open a website
driver.get("https://maps.google.com")

_sleep(15)

# Find the search box element
search_box = driver.find_element(By.NAME, 'q')

# Enter the search term
search_box.send_keys("No. 3, Old Madras Rd, Sadanandanagar, Bennigana Halli, Bengaluru, Karnataka 560016")

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

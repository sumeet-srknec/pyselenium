from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import time as _time, sleep as _sleep

# Initial the driver
driver = webdriver.Chrome(service=webdriver.ChromeService())

# Open a website
driver.get("https://www.youtube.com")

_sleep(15)

# Find the link element
live_link = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[5]/a/tp-yt-paper-item/yt-formatted-string')

# Click on the identified link.
live_link.click()

_sleep(15)

# Wait for a few seconds (optional)
driver.implicitly_wait(600)

# Print the title of the results page
print(driver.title)

_sleep(100)

# Close the browser
# driver.quit()

"""
Using selenium webdriver
open http://google.com in a window and print the page source and finally close the window.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get('https://www.google.com')

time.sleep(3)

driver.close() # closes a window only

driver.quit() # closes the browser and ends the test


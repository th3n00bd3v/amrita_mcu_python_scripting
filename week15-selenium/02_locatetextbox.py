"""
open http://google.com and try to locate the Google search text box with the help of its Name attribute value and enter text and search.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

finally:
    driver.quit()

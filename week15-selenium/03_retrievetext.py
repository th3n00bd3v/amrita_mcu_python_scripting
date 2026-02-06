"""
open http://google.com and print the text which we eneterd, from Google search text box and after retrieving the text, clear the search text box.
Use: find_element_by_xpath
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element_by_xpath("//input[@name='q']")
    search_box.send_keys("Selenium WebDriver")

    entered_text = search_box.get_attribute("value")
    print("Entered text:", entered_text)
    search_box.clear()
    time.sleep(2)

finally:
    driver.quit()

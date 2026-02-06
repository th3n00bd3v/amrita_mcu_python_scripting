"""
write a basic unit test using webdriver which check if the title of the webpage is yahoo or google?
(Tip: use assertTrue)
"""

from selenium import webdriver
import unittest

tc_obj = unittest.TestCase() # test case object

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    print("Page title:", title)

    tc_obj.assertTrue(
        "Google" in title or "Yahoo" in title,
        "Title is neither Google nor Yahoo"
    )
    
finally:
    driver.quit()
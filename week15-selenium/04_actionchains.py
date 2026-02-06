"""
open https://amrita.edu/ahead/mca-cyber/ and go to About page, by using ActionChains.
(Tip: use find_element_by_css_selector)
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.get("https://amrita.edu/ahead/mca-cyber/")
    driver.maximize_window()
    time.sleep(3)

    actions = ActionChains(driver)
    about_menu = driver.find_element_by_css_selector("a[title='About']")

    move_action = actions.move_to_element(about_menu)
    move_action.click().perform()

    time.sleep(5)

finally:
    driver.quit()

"""
open https://amrita.edu/ahead/mca-cyber/, and then get the website URL of your choice and click on the link which opens in a new window. And switch between them.
(Tip: use switch_to.window)
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("https://amrita.edu/ahead/mca-cyber/")
    driver.maximize_window()
    time.sleep(3)
    
    parent_window = driver.current_window_handle
    print("Parent window title:", driver.title)
    
    link = driver.find_element_by_css_selector("a[target='_blank']")
    link.click()
    time.sleep(3)
    
    all_windows = driver.window_handles

    # Switch to the new window
    for window in all_windows:
        if window != parent_window:
            driver.switch_to.window(window)
            break

    print("Child window title:", driver.title)
    print("Child window URL:", driver.current_url)

    time.sleep(3)

    driver.switch_to.window(parent_window)
    print("Back to parent window title:", driver.title)

    time.sleep(3)

finally:
    # Close all windows
    driver.quit()

    
    
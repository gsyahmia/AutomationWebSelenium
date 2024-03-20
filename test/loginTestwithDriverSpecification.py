# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).   
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title) 
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

import time
import sys
sys.path.insert(0, "D:/Automation/AutomationWebSelenium/")
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services = Service('C:/Drivers/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=services)
driver.get(config.web_OrangeHRM())
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)

dashboard_title= driver.title
#Dashboard tile
exp_title = "OrangeHRM"

if dashboard_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

driver.close()
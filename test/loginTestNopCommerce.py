# 1) Open Web Browser(Chrome/firefox/IE).
# 2) Open URL  https://admin-demo.nopcommerce.com/login
# 3) Provide Email  (admin@yourstore.com).
# 4) Provide password  (admin).   
# 5) Click on Login.
# 	driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# 6) Capture title of the dashboad page.(Actual title)
# 7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
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
driver.get(config.web_NopCommerce())
time.sleep(5)

driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
time.sleep(5)
exp_title = driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").is_displayed()

if exp_title:
    print("Login passed")
else:
    print("Login failed")
    
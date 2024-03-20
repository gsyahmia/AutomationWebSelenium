import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


services = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=services)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "egist").click()
time.sleep(3)

driver.close()
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo IdeaCentre 600 All-in-One PC")
# driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
# time.sleep(2)
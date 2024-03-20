from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=services)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))


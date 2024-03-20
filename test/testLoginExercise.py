import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
serv_obj = Service('C:/Drivers/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(5)
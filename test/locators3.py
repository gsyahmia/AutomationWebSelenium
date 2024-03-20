from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=services)
driver.get("https://id-id.facebook.com/login.php/")
driver.maximize_window()

#Tagname & Id -> tagname#valueofId
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("123")
#Tag (is always optiona) & Id -> #valueofId
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("123")

#Tagname & Class -> tagname.valueofClass
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

#Tagname & Attribute -> tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[autocomplete=username]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "input[autocomplete=current-password]").send_keys("1234")
# driver.find_element(By.CSS_SELECTOR, "[autocomplete=username]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[autocomplete=current-password]").send_keys("1234")


#Tagname & Class & Attribute -> tagname.valueofClass[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input.inputtext[autocomplete=username]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input.inputtext[autocomplete=current-password]").send_keys("1234")
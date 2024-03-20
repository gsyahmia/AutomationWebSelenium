import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()



#Relative Xpath
# driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[@id='searchbox']/button").click()
# time.sleep(3)

#Full Xpath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirt")
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
# time.sleep(3)


#Xpath 'Or'/'And' operator
# driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[@name='submit_search' and @class='btn btn-default button-search']").click()
# time.sleep(3)

#Xpath using Contains/Start with
driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("T-shirt")
driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()
time.sleep(3)

# Text() function
# driver.find_element(By.XPATH, "//b[text()='Cart']").click()
# time.sleep(3)
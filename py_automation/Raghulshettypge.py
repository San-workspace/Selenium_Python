from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")
import random

from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("gsankar3388@gmail.com") # parent-child traversing by using xpath

pswd="Selenium@"+str(random.randint(345,543))

driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input ").send_keys(pswd) ## parent-child traversing by using CSS-selector
driver.find_element(By.CSS_SELECTOR,'#confirmPassword').send_keys(pswd)
print(pswd)
driver.find_element(By.CSS_SELECTOR,".btn").click()



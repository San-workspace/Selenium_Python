import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
mouse=driver.find_element(By.XPATH,"//div[1]/a[2]").text
assert "Reload" in mouse
action.context_click().perform()


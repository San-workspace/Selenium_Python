import click
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Select() class to handle dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")

driver.find_element(By.CSS_SELECTOR,".btn").click()



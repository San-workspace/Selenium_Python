import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")

print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value") == "India"

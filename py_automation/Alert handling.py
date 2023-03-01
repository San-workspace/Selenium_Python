from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="San"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()





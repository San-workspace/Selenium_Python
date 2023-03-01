from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service = chrome_service,options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.NAME,"j_username").send_keys("2000734607221377")   #normal way of input by using artibute and value
driver.find_element(By.CSS_SELECTOR,"input[id='userName']").send_keys("2000734607221377")
driver.find_element(By.NAME,"j_password").send_keys("8870935744")
driver.find_element(By.NAME,"submit").click()
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.maximize_window()
message=driver.find_element(By.XPATH,"//p[@align='JUSTIFY']").text  #Xpath syntax is : //tagname[@artibute='value']
assert "out" in message
print(message,"- Test PASS")


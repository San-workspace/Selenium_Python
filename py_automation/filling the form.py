from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service = chrome_service,options=chrome_options)

driver.get("https://www.tnebnet.org/awp/login")

#driver.find_element(By.NAME,"j_username").send_keys("2000734607221377")   #normal way of input by using artibute and value
#driver.find_element(By.CSS_SELECTOR,"input[id='userName']").send_keys("2000734607221377") #by using CSS_selector - method 1
driver.find_element(By.CSS_SELECTOR,"#userName").send_keys("2000734607221377") #by using short method for css selector using #idname or can use .classname - method2

driver.find_element(By.NAME,"j_password").send_keys("8870935744")
driver.find_element(By.NAME,"submit").click()
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/awp/logout']").click()
message=driver.find_element(By.XPATH,"//p[@align='JUSTIFY']").text  #Xpath syntax is : //tagname[@artibute='value']
assert "out" in message
print(message,"- Test PASS")


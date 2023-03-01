#Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(service = chrome_service,options=chrome_options)
driver.maximize_window()
driver.get("https://www.python.org") #hit the url on the browser
print(driver.title) #title of the tab printed on console
print(driver.current_url) #to print current url on console
driver.refresh()
driver.get("https://www.python.org/jobs/")
driver.back()
driver.forward()
#driver.close()

#driver.close()
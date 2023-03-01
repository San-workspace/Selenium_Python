from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
#headless run
chrome_options.add_argument("headless")

#incase certificate error while opening the browser
chrome_options.add_argument("--ignore-certificate-error")


driver=webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#scroll down
driver.execute_script("window.scrollBy(0,700);")
#screenshot
driver.get_screenshot_as_file("screenshot.png")


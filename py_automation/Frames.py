from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.implicitly_wait(5)  #5 sec for max timeout
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("here it is iframe")
driver.switch_to.default_content()

print(driver.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text)



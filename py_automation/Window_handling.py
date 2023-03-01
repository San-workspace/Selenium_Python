import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windows_opened=driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
# action=ActionChains(driver)
# action.context_click(driver.find_element(By.TAG_NAME,"h3")).perform()
time.sleep(2)
driver.close() #child window only closed parent window still in open
driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

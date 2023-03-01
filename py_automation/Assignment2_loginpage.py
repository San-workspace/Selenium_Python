from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# driver.implicitly_wait(1)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
child_window=driver.window_handles
driver.switch_to.window(child_window[1])
searchText=driver.find_element(By.XPATH,"//a[normalize-space()='mentor@rahulshettyacademy.com']").text
print(searchText)
driver.switch_to.window(child_window[0])
driver.find_element(By.ID,"username").send_keys(searchText)
driver.find_element(By.ID,"password").send_keys('password')
driver.find_element(By.ID,"signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert")))
print(driver.find_element(By.CSS_SELECTOR,".alert").text)
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("@").strip().split(" ")[0]
# print(var)

import time

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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"(//button[@type='button'])[1]").click()

driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#explicit wait

wait=WebDriverWait(driver,10)

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)





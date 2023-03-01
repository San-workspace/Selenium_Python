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
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
products=driver.find_elements(By.XPATH,"//h4[contains(@class,'title')]")

# #By using list ,how to get an item from list
# # product_list=[]
# for i in products:
#     # product_list.append(i.text)
#     # print(product_list)
#     # if "Blackberry" in product_list:


for i in products:
        if i.text == "Blackberry":
            driver.find_element(By.XPATH, "(//button[contains(@class,'info')])[4]").click()
driver.find_element(By.XPATH,"//a[contains(@class,'btn-primary')]").click()
driver.find_element(By.XPATH, "(//button[contains(@class,'btn')])[3]").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,".checkbox").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
alert_text=driver.find_element(By.CLASS_NAME,"alert-success").text
print(alert_text)
assert "Success" in alert_text
driver.close()





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

#To check actual list nd expectd list
expected_list=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list=[]


for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text) #creating the actual list
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"(//button[@type='button'])[1]").click()
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#check actul list and epected list
assert actual_list == expected_list
#explicit wait
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

# #sum_validation
tprices=driver.find_elements(By.XPATH,"//td[5]/p")
sum=0
for tprice in tprices:
    sum=sum+int(tprice.text)
print(sum)
total=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == total

# #verify discount applied or not
dis_amt=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert dis_amt < total











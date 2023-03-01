#Test objective : web sorted item list == python sor
#----------------------------------------------------
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
chrome_options.add_argument("--start-maximized")

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# driver.implicitly_wait(1)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on header for sorting
browser_sortlist=[]

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
sorted_items=driver.find_elements(By.XPATH,"//tr/td[1]")
for items in sorted_items:
   browser_sortlist.append(items.text)

original_browsersortlist=browser_sortlist.copy()

print("original browser sort list is :",browser_sortlist)

#sorting browser sorting list with sort()

browser_sortlist.sort()
print("sorted list is :",browser_sortlist)

#asserting both the list

assert original_browsersortlist == browser_sortlist




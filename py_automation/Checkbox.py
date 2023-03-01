from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#checkbox
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
#radio_button
radio_buttons=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
print(len(radio_buttons))

for radio_button in radio_buttons:
    if radio_button.get_attribute('value') == "radio3":
        radio_button.click()
        assert radio_button.is_selected()
        break

#Is_displayed
assert driver.find_element(By.NAME,"show-hide").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.NAME,"show-hide").is_displayed()





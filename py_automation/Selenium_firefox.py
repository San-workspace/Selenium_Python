#Selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Firefox
# firefox_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/geckodriver-v0.32.0-win64/geckodriver.exe")
# driver = webdriver.Firefox(service =firefox_service)

#Edge
edge_service=Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service =edge_service)


from selenium.webdriver.edge.options import Options
edge_options=Options()
edge_options.add_experimental_option("detach",True)


driver.maximize_window()
driver.get("https://www.python.org") #hit the url on the browser
print(driver.title) #title of the tab printed on console
print(driver.current_url) #to print current url on console
driver.refresh()
driver.get("https://www.python.org/jobs/")
driver.back()
driver.forward()
#driver.close()


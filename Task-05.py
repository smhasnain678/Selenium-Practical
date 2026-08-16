import drive
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)
print(driver.title)

driver.execute_script("window.open('https://google.com','new window')")
print(driver.title)
time.sleep(5)
driver.quit()


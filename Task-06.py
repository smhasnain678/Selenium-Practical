import drive
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)


driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles
time.sleep(2)
driver.switch_to.window(wins[1])
print("This is my zero index"+ driver.title)
time.sleep(5)
driver.quit()


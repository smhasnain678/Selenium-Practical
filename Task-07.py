import drive
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)


driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles
time.sleep(2)
driver.switch_to.window(wins[0])
print("\n=============This is my zero index(Flipcart)==============\n"+ driver.title)
myflipcart = driver.find_elements(By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/a/div/div[1]/div")
print(myflipcart.text)
driver.switch_to.window(wins[1])
time.sleep(2)
print("\n==============This is my first index(google)==============\n"+ driver.title)
mygoogle = driver.find_elements(By.XPATH,'//*[@id="SlvCob"]')
print(mygoogle.text)
time.sleep(5)
driver.quit()


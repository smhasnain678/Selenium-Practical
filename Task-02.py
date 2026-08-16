# Method 2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/?utm_source=chatgpt.com")
driver.maximize_window()
driver.implicitly_wait(5)
rows_data = driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr")
total_rows_data = len(rows_data)
cols_data = driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")
total_cols_data = len(cols_data)
for i in rows_data:
   print(i.text)
time.sleep(5)
driver.quit()


# Method 2
#import time

#from selenium import webdriver
#from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()

#driver.get("https://testautomationpractice.blogspot.com/?utm_source=chatgpt.com")
#driver.maximize_window()
#driver.implicitly_wait(5)

#start_range = '//*[@id="HTML1"]/div[1]/table/tbody/tr['
#middle_range = ']/td['
#end_range = ']'

#rows_data = driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr")

#print("Rows:", len(rows_data))

#cols_data = driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")


#for row in range(2, len(rows_data) + 1):
 #   for col in range(2, len(cols_data) + 1):
  #      print(driver.find_element(By.XPATH, start_range + str(row) + middle_range + str(col) + end_range).text,end=" ")
   # print()
#time.sleep(5)
#driver.quit()
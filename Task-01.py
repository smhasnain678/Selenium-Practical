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

print("Total rows are: ", total_rows_data, "and Total columns are: ", total_cols_data )

time.sleep(5)
driver.quit()

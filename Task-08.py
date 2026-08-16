import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://alnafi.com/courses/diploma-in-devops-and-cloud")
driver.maximize_window()
time.sleep(5)

courses=[]
fees=[]

driver.execute_script("window.open('https://alnafi.com/courses/diploma-in-sysops-and-cloud','new window')")
wins = driver.window_handles
time.sleep(5)

#This is python course details
driver.switch_to.window(wins[0])
course_name = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[5]/div/section[1]/div[1]/div[1]/div/div/h1').text
fees_usd = driver.find_element(By.XPATH,'//*[@id="plans"]/div/div[2]/div[4]/div/h1/span').text
courses.append(course_name)
fees.append(fees_usd)


#This is sysops course details
driver.switch_to.window(wins[1])        #Sysops
time.sleep(8)
course_name = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[5]/div/section[1]/div[1]/div[1]/div/div/h1').text
fees_usd = driver.find_element(By.XPATH,'//*[@id="plans"]/div/div[2]/div[4]/div/h1/span').text
courses.append(course_name)
fees.append(fees_usd)
print(courses)
print(fees)


time.sleep(5)
driver.quit()
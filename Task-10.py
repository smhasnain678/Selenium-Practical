import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import  encoders
from datetime import *
import time as t

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://alnafi.com/courses/python")
driver.maximize_window()
t.sleep(5)

courses=[]
fees=[]

driver.execute_script("window.open('https://alnafi.com/courses/sysops','new window')")
wins = driver.window_handles
t.sleep(5)

#This is python course details
driver.switch_to.window(wins[0])
course_name = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[5]/div/section[1]/div[1]/div[1]/div/div/h1').text
fees_usd = driver.find_element(By.XPATH,'//*[@id="plans"]/div/div[2]/div[4]/div/h1/span').text
courses.append(course_name)
fees.append(fees_usd)


#This is sysops course details
driver.switch_to.window(wins[1])        #Sysops
t.sleep(8)
course_name = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[5]/div/section[1]/div[1]/div[1]/div/div/h1').text
fees_usd = driver.find_element(By.XPATH,'//*[@id="plans"]/div/div[2]/div[4]/div/h1/span').text
courses.append(course_name)
fees.append(fees_usd)
print(courses)
print(fees)

data = list(zip(courses,fees))
print(data)
file = open('myfile_abd.csv','w',newline='')
writer = csv.writer(file)
writer.writerows(data)
file.close()

t.sleep(5)
driver.quit()
day=date.today()
time1=datetime.now()

my_custom=day.strftime("%B %d %Y")
current_time=time1.strftime("%I:%M:%S %p")

filename=r"J:\smhasnain\Al-Nafi\DevOps\Python Selenium\Selenium-Practical\myfile_abd.csv"
mylogo=r"J:\smhasnain\Al-Nafi\DevOps\Python Selenium\Selenium-Practical\Alnafi.png"
msg=MIMEMultipart()

my_mail="devopsautomation076@gmail.com"
password="uuwvpoktbczvnhgi"
msg['Subject']= f"Alnafi Course fees details :  {my_custom} {current_time}"
msg['From']= my_mail
msg['To'] = my_mail
msg['Cc'] = 'smhasnain43@gmail.com'


body="""
<html><p> Hi Team,<br> We have collected Alanfi's course fees details from offical website and we have stored data into CSV file, So kindly find and attach.   <br><br><br>Hasnain<br> <img src="cid:alogo" width="100" height="50"></p> </html>
"""
msg.attach(MIMEText(body,'html'))


###LOGO section
filelogo=open(mylogo,'rb')
msgIMAGE=MIMEImage(filelogo.read())
filelogo.close()
msgIMAGE.add_header('Content-ID','<alogo>')
msg.attach(msgIMAGE)


#ATTACHMENT section
attachment=open(filename,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename=%s" % filename)
msg.attach(part)

connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()       #TLS transport layer security


connection.login(user=my_mail,password=password)
connection.send_message(msg)
connection.close()

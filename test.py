import csv

courses = ['Diploma in DevOps and Cloud Advancement', 'Diploma in SysOps & Cloud Advancement']
fees = ['PKR 250,000', 'PKR 300,000']
data = list(zip(courses, fees))
file = open('myfile_abd.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerows(data)
file.close()
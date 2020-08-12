#........Firstly We Get data From Web site........#
from selenium import webdriver
import pandas as pd

cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'


month=str(input('Enter the month in small letters : '))
year=str(input('Enter the year : '))
city=input("Enter the city : ")

chrome_browser = webdriver.Chrome(cd)
chrome_browser.get('https://www.accuweather.com/en/in/'+city+'/206690/'+month+'-weather/206690?year='+year+'&view=list')
# chrome_browser.get('https://www.accuweather.com/en/in/hyderabad/206690/august-weather/206690?year=2020&view=list')

#high temp
data=chrome_browser.find_elements_by_class_name("high")
temp_high=[]
for i in data:
    t=i.get_attribute('textContent')
    temp_high.append(int(t[:2]))

#Temp low
data2=chrome_browser.find_elements_by_class_name("low")
temp_low=[]
for i in data2:
    t=i.get_attribute('textContent')
    temp_low.append(int(t[3:5]))

#precipitation
precip=[]
precipdata = chrome_browser.find_elements_by_xpath("//div[@class='info precip']/p[2]")
for i in precipdata:
	t=i.get_attribute('textContent')
	precip.append(float(t[:2]))

#date
date=[]
for i in range(len(precip)):
    date.append(i+1)

#data to csv

d={"Date":date,"High_temp":temp_high, "Low_temp":temp_low, "Precipitation": precip}

df=pd.DataFrame(d)
df.to_csv("C:\\Users\\hp\\Desktop\\+"+city+month+".csv")

#.........Data Visualisation.............#

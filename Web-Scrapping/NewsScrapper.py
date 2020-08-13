from selenium import webdriver
import time
import pandas as pd

p=int(input("Enter the number of pages: "))
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'
browser=webdriver.Chrome(cd)

titles=[]
links=[]

for i in range(p):
	url='https://news.ycombinator.com/news?p='+str(i+1)
	browser.get(url)
	d=browser.find_elements_by_xpath("//a[@class='storylink']")

	for j in d:
		title=j.text
		link=j.get_attribute('href')
		titles.append(title)
		links.append(link)

dic={'news_title':titles,'URL':links}

df=pd.DataFrame(dic)

print(df)

df.to_csv("C:\\Users\\hp\\Desktop\\news.csv",index=False)
print("Done")

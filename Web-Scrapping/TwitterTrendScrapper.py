
from selenium import webdriver
import time
import pandas as pd
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'
browser=webdriver.Chrome(cd)
dic={'HashTag','URL'}
df=pd.DataFrame(columns=dic)
browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(5)
sp=browser.find_elements_by_xpath("//span[@dir='ltr']")

for i in sp:
    data={}
    a=i.text
    url='https://twitter.com/search?q=%23'+a+'&src=trend_click'
    data[df.columns[0]]=a
    data[df.columns[1]]=url
    df=df.append(data,ignore_index=True)



df.to_csv("C:\\Users\\hp\\Desktop\\Twitter_HT.csv",index=True)
print("The data is stored at C:\\Users\\hp\\Desktop\\Twitter_HashTags.csv")

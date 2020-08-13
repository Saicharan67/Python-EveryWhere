from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe' #path to your chrome driver


browser= webdriver.Chrome(cd)
browser.get("https://worldometers.info/population/countries-in-asia-by-population/")
col=["Country","Population","Yearly Change"]
df=pd.DataFrame(columns=col)
time.sleep(5)
for i in browser.find_elements_by_xpath("//*[@id='example2']/tbody/tr"):
    row=[]
    p=i.find_elements_by_tag_name('td')
    for ele in p:
      row.append(ele.get_attribute("textContent"))
    dic={}
    for i in range(len(df.columns)):
         dic[df.columns[i]]=row[i+1]
    df = df.append(dic, ignore_index=True)
print(df)
df.to_csv('C:\\Users\\hp\\Desktop\\Population.csv', index = False)

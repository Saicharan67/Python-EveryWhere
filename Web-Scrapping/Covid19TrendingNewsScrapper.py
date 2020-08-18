from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'
browser=webdriver.Chrome(cd)
dic={'HashTag','URL'}
df=pd.DataFrame(columns=dic)
browser.get('https://twitter.com/search?q=Covid19&src=recent_search_click')

time.sleep(10)

n=[]

ps=browser.page_source
soup=BeautifulSoup(ps,'html.parser')

news=soup.findAll('div',{'class':'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'})

for i in news:
    a=i.get_attribute('textContent')
    n.append(a)
    print(a)

# file1 = open("C:\\Users\\hp\\Desktop\\cov.txt","w")
# file1.writelines(n)
# file1.close()
# print("Finished")

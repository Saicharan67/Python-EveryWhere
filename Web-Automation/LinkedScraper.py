from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
cd="C:\\Users\\hp\\Anaconda3\\chromedriver.exe"
browser=webdriver.Chrome(cd)
browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
si=browser.find_element_by_xpath('//a[@class="main__sign-in-link"]')
si.click()
time.sleep(10)
user=input("Enter username")
pswd=input("Enter password")
u=browser.find_element_by_id("username")
p=browser.find_element_by_id("password")
u.send_keys(user)
p.send_keys(pswd)
btn=browser.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button")
btn.click()
#......Below Code Is For All the Connections.........#
# while True:
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#     time.sleep(0.1)
#     browser.execute_script('window.scrollTo(0,0);')
#     time.sleep(0.1)
#     lenpage = browser.execute_script(' return (window.scrollHeight - window.scrollTop === window.clientHeight)')
#     if lenpage:
#         break


pg=browser.page_source
soup=BeautifulSoup(pg,'html.parser')
de=soup.findAll('div',{'class':"mn-connection-card__details"})
conn=[]
for i in de:
    k=i.find('a')
    u=k.get('href')
    conn.append(u)
c_n=[]
c_p=[]
c_c=[]

for i in conn:
    url="https://www.linkedin.com/"+i
    browser.get(url)
    ne=browser.find_element_by_xpath('//div[@class="flex-1 mr5"]/ul[1]/li[1]')
    name=ne.text
    c_n.append(name)
    cpe=browser.find_element_by_xpath('//div[@class="flex-1 mr5"]/h2[1]')
    cpos=cpe.text
    c_p.append(cpos)
    url2=url+'detail/contact-info/'
    c_c.append(url2)

dic={'Name':c_n,'Current Position':c_p, 'Contact Info': c_c}
df=pd.DataFrame(dic)
df.to_csv("C:\\Users\\hp\\Desktop\\LinkedIn connection.csv",index=False)

print("DONE")

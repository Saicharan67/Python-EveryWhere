from selenium import webdriver
import time
import pandas as pd
import os

#path to your chromedriver
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'

chrome_browser = webdriver.Chrome(cd)
chrome_browser.get("https://www.worldometers.info/coronavirus/")
time.sleep(10)

column_names=['Rank','Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths','Recovered', 'Active Cases', 'Critical']
df=pd.DataFrame(columns= column_names)
print(df)
p=0
for i in chrome_browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr'): # tr for each of country
    td_list=i.find_elements_by_tag_name('td') # tag name retrieve each piece of info for a country
    row=[]
    for td in td_list:
        row.append(td.get_attribute("textContent")) # creating row ie each country data
    data = {}
    for j in range(len(df.columns)):
        data[df.columns[j]] = row[j]
    if p not in [0,1,3,4,6,8]:
      df = df.append(data, ignore_index=True)
    p+=1


print(df)

# base_path='C:\\Users\\hp\\Desktop'

# path=os.path.join(base_path,'Covid_Dataset_.csv')
# # os.mkdir(path)
# df.to_csv(path, index = False)
# print("The dataset has been saved at the loction: "+path)
# chrome_browser.quit()

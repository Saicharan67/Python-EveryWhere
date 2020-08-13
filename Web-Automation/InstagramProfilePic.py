from selenium import webdriver

url="https://www.instagram.com/"

user=input("Enter the username of the id:")

user_id=url+user

browser=webdriver.Chrome("C:\\Users\\hp\\Anaconda3\\chromedriver.exe")

browser.get(user_id)

try:
	image=browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
	image=browser.find_element_by_xpath('//img[@class="be6sR"]')


img_link=image.get_attribute('src')


path="C:\\Users\\hp\\Pictures\\"+user+".jpg"

import urllib.request

urllib.request.urlretrieve(img_link,path)

print("The profile pic has been downloaded at: "+path)
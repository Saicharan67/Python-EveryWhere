from selenium import webdriver

url="https://www.instagram.com/"

user=input("Enter the username of the id:")

user_id=url+user

browser=webdriver.Chrome("C:\\Users\\hp\\Anaconda3\\chromedriver.exe")

browser.get(user_id)

try:

  bio=browser.find_element_by_xpath('//*[@class="-vDIg"]/span[1]').get_attribute('textContent')

  print(bio)
except e:
	print(e)
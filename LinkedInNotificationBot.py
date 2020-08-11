from selenium import webdriver
from time import sleep

browser =webdriver.Chrome('C:\\Users\\hp\\Anaconda3\\chromedriver.exe')
browser.get('https://www.linkedin.com/')

user_id=input("Enter the Email or Phone number: ")
psd=input("Enter the Password: ")

# locate email form by_id_name
ep=browser.find_element_by_id(user_id)
# send_keys() to simulate key strokes
ep.send_keys(psd)

# locate password form by_id_name
pw=browser.find_element_by_id("session_password")
# send_keys() to simulate key strokes
pw.send_keys("<Enter password>")

sleep(5)
# locate submit button by_class_name
login=browser.find_element_by_class_name("sign-in-form__submit-button")

login.click()

sleep(8)

try:
	k='//div[@id="ember53"]//span[@class="notification-badge__count "]'
	n=browser.find_element_by_xpath(k).get_attribute('textContent')

	print("The current number of notifications in my profile: ", n)
except:
	print("No new Notifications for you")
from selenium import webdriver
import schedule
import time
from datetime import datetime as date
cd = 'C:\\Users\\hp\\Anaconda3\\chromedriver.exe'

#Chrome option to turn off default settings of chrome

chrome_options = webdriver.ChromeOptions()

#Turning off geoloaction and notifications "1" for on "2" for off

chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
                                                 })
chrome_options.add_argument("start-maximized")
browser = webdriver.Chrome(cd, options=chrome_options)
browser.get('https://mail.google.com/mail/u/0/#inbox')
email = browser.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys("mahankalisaicharan@gmail.com")
continuee = browser.find_element_by_xpath(
    '//*[@id="identifierNext"]/div/button')
continuee.click()
time.sleep(5)
password = browser.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("M.saicharan@02")
nextt = browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
nextt.click()
time.sleep(2)
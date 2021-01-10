from selenium import webdriver
import schedule
import time
from datetime import datetime as date
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'

#Chrome option to turn off default settings of chrome

chrome_options = webdriver.ChromeOptions()

#Turning off geoloaction and notifications "1" for on "2" for off

chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
  })
chrome_options.add_argument("start-maximized")

def openmeet():
    browser=webdriver.Chrome(cd,options=chrome_options)
    
    #setting default meetings codes in dict

    day={"Monday":"ec304","Tuesday":"ec351", "Wednesday":"ec304", "Thursday":"ec306", "Friday":"ec304"}
    code=day[date.today().strftime("%A")]

    browser.get('https://meet.google.com/landing?authuser=2')
    time.sleep(5)

    #entering mail and clicking to next

    email=browser.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys("<Enter your Mail>")
    continuee=browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    continuee.click()
    time.sleep(5)

  #entering password and clicking next

    password=browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys("<Enter Your Password>")
    nextt=browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
    nextt.click()
    time.sleep(2)

    #clicking enter meet code button

    browser.find_element_by_xpath('//div[@class="ox9SMb jginQb"]').click()
    time.sleep(2)

    #Get input feild and sending keys as code

    classcode=browser.find_element_by_xpath('//input')
    classcode.send_keys(code)
    time.sleep(2)
    
    #Clicking continue to join

    browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div').click()
    time.sleep(3)

    #Turning off microphoone and camera

    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div').click()
    
    Clicking  join now
    time.sleep(5)
    join=browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div')
    join.click()

#sheduling every day to do task

schedule.every().day.at("12:03").do(openmeet)
while True:
    schedule.run_pending()


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


user_id=input('Enter User Id of your Fb Account :')  # Take user id and password as input from the user
password=input('Enter the password :')

print(user_id)
print(password)

cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'


browser= webdriver.Chrome(cd)
browser.get('https://www.facebook.com/')


user_box = browser.find_element_by_id("email")       # For detecting the user id box
user_box.send_keys(user_id)                                               # Enter the user id in the box

password_box = browser.find_element_by_id("pass")    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box

login_box = browser.find_element_by_id("u_0_b")      # For detecting the Login button
login_box.click()                                                         # To click on the login box

time.sleep(20)

pro=browser.find_element_by_xpath('//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn e72ty7fz qlfml3jp inkptoze qmr60zad btwxx1t3 tv7at329 taijpn5t"]')
pro.click()

time.sleep(4)
fr=browser.find_element_by_xpath('//*[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 g0qnabr5 tkr6xdv7"][3]')
fr.click()

while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(0.1)
    browser.execute_script('window.scrollTo(0,0);')
    time.sleep(0.1)
    try:
        exit_control=browser.find_element_by_xpath("//*[contains(text(), 'More about you')]")
        break
    except:
        continue




f=browser.find_elements_by_xpath('//span[@class="oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql a8c37x1j s89635nw ew0dbk1b a5q79mjw g1cxx5fr lrazzd5p oo9gr5id"]')

friends=[]
for i in f:
    x=i.get_attribute("textContent")
    friends.append(x)



names_list=[]
for name in friends:
    if(name=='FriendFriends'):
        continue
    if('friends' in name):
        continue
    if(name==''):
        continue
    else:
        names_list.append(name)

print(friends)

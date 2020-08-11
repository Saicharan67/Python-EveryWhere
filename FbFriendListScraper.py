from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys

user_id=input('Enter User Id of your Fb Account :')  # Take user id and password as input from the user
password=input('Enter the password :')

print(user_id)
print(password)
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
        
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe' #path to your chrome driver


browser= webdriver.Chrome(cd)
browser.get('https://www.facebook.com/')


user_box = browser.find_element_by_id("email")       # For detecting the user id box
user_box.send_keys(user_id)                                               # Enter the user id in the box 

password_box = browser.find_element_by_id("pass")    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box
time.sleep(2)
login_box = browser.find_element_by_id("u_0_b")      # For detecting the Login button
login_box.click()
time.sleep(15)
bt = browser.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 datstx6m taijpn5t oi9244e8 d74ut37n']/a[1]")
bt.click()

time.sleep(15)

bt1=browser.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 btwxx1t3 k4urcfbm']/a[3]")
bt1.click()


browser.execute_script('window.scrollTo(1, 1000);')

time.sleep(10)
for i in range(10):
  p=browser.find_element_by_xpath("//*[@class='dati1w0a ihqw7lf3 hv4rvrfc discj3wi']/div[3]/div[1+{0}]/div/div/a/span".format(i)).text
  uprint(p)
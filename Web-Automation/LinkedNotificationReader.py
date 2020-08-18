from selenium import webdriver
from time import sleep
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
browser =webdriver.Chrome('C:\\Users\\hp\\Anaconda3\\chromedriver.exe')


user_id=input("enter username :")
psd=input("enter password :")

browser.get('https://www.linkedin.com/')

# locate email form by_id_name
ep=browser.find_element_by_id("session_key")
# send_keys() to simulate key strokes
ep.send_keys(user_id)

# locate password form by_id_name
pw=browser.find_element_by_id("session_password")
# send_keys() to simulate key strokes
pw.send_keys(psd)

sleep(5)
# locate submit button by_class_name
login=browser.find_element_by_class_name("sign-in-form__submit-button")

login.click()

sleep(5)

p=browser.find_element_by_xpath('//*[@id="ember32"]')
p.click()


sleep(3)


notif_list = browser.find_elements_by_xpath("//*[@class='nt-segment__occludable-area ember-view']/article/div/div[2]/a/span")


c=1
for i in notif_list:
  if c%2==1:
    uprint(i.get_attribute("textContent")+"\n")
  c+=1



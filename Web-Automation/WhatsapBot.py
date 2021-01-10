from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-data-dir=C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
)

driver = webdriver.Chrome("C:\\Users\\hp\\Anaconda3\\chromedriver.exe",
                          chrome_options=chrome_options)
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = 'Santhosh'

# Replace the below string with your own message
string = "Message sent using Python!!!"

x_arg = '//*[@id="pane-side"]/div[1]/div/div/div[13]/div/div/div[2]'
group_title = driver.find_element_by_xpath(x_arg)
sleep(3)
group_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
sleep(3)
input_box.send_keys(string + Keys.ENTER)
sleep(2)
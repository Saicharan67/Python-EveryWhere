from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\\Users\\hp\\Anaconda3\\chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/")
sleep(4)

from selenium.webdriver.common.keys import Keys

driver.find_element_by_xpath("//input[@name='username']").send_keys("<ENTER USER NAME>")
driver.find_element_by_xpath("//input[@name='password']").send_keys( "<ENTER PASSWORD>")
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()

sleep(10)


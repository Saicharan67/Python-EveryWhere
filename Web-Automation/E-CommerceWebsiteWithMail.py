from selenium import webdriver
import smtplib
import schedule
cd='C:\\Users\\hp\\Anaconda3\\chromedriver.exe'

browser=webdriver.Chrome(cd)

def get_price():
   browser.get('https://www.amazon.in/Test-Exclusive-750/dp/B078BN55WZ/ref=sr_1_1?crid=3OEL6DKYVV850&dchild=1&keywords=one%2Bpluse8%2Bpro%2Bmobile&qid=1597315955&sprefix=one%2Caps%2C290&sr=8-1&th=1')
   pe=browser.find_element_by_id('priceblock_ourprice')
   pr=pe.get_attribute('textContent')
   pr=pr[2:]
   pl=pr.split(',')

   price_a=''
   for i in pl:
      price_a+=i

   price=float(price_a)
   return price
def mail():
    s=smtplib.SMTP('smtp.gmail.com' , 587)
    s.starttls()
    #change this else code will not work
    ml='mahankalisaicharan@gmail.com'
    #change this else code will not work
    pw='M.saicharan@02'
    s.login(ml,pw)
    #change this else code will not work
    mt='611848@student.nitandhra.ac.in'
    message='Hurry Up. the price is low now. Grab the deal.'
    s.sendmail(ml, mt, message)
    s.quit()



def task():
    p=190000.00
    a=get_price()

    if(a<=p):
        mail()
        print("MAILED")
    else:
        print("Don't Buy")

schedule.every(10).seconds.do(task)
print("Getting inside the while loop.")
while True:
    schedule.run_pending()

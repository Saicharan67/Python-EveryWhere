from bs4 import BeautifulSoup
import schedule
import requests
import smtplib
from email.message import EmailMessage
import arrow


UserName = "Place Your UserName Here"

page = requests.get("https://github.com/"+UserName)
soup = BeautifulSoup(page.content, "html.parser")


def SendMail(count):
    msg = EmailMessage()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("example@gmail.com", "example")
    if count != "0":
        msg["Subject"] = "Well Done You Are Maintaining Your Git Streak..!"

        text = """
        
         You Have Made {} Contributions Today...!""".format(
            count
        )
        msg.set_content(text)
    else:
        msg["Subject"] = "Your Git Streak About To Break...!"
        text = """
        
        Your GitHub streak is about to break. Go and make a commit quick!

        """
        msg.set_content(text)
    s.sendmail(
        "example@gmail.com", "UserEmail@gmail.com", msg.as_string()
    )

    print("sent")
    s.quit()


def EmailStreak():
   
    Todays_Date = arrow.now().format('YYYY-MM-DD')
    Todays_Streak = soup.find_all("rect", attrs={"data-date": Todays_Date})
    count = Todays_Streak[0]["data-count"]

    SendMail(count)
    print(count,Todays_Date,Todays_Streak)


schedule.every().day.at("####TimeToGetMail####").do(EmailStreak)
while True:
    schedule.run_pending()


#!/usr/bin/python

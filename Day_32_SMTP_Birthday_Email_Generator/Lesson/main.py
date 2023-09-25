""" import smtplib

myEmail = "email@email.org"
myPassword = "<<key>>"

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=myEmail, password=myPassword)
    connection.sendmail(
        from_addr=myEmail, 
        to_addrs="new_email@email.org", 
        msg="Subject:Hello\n\nThis is the body of my email."
    )
 """

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1972, month=6, day=5)
print(date_of_birth)
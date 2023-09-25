import random
import smtplib
import datetime as dt

def generate_quote():
    with open("quotes.txt") as file:
        quotes=file.read().splitlines()
    quote = random.choice(quotes)
    return quote

def send_email(quote):
    myEmail = "email@email.org"
    myPassword = "<<key>>"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPassword)
        connection.sendmail(
            from_addr=myEmail, 
            to_addrs="new_email@email.org", 
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )

day_of_week = dt.datetime.now().weekday()
if day_of_week == 6:
    quote = generate_quote()
    send_email(quote)
else:
    print("Not the right day to send emails.")



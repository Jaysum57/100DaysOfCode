import smtplib
import datetime as dt
import random

MY_EMAIL = '''My email'''
MY_PASSWORD ='''app password'''

RECIPIENT = '''recipient email'''

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=RECIPIENT,
            msg=f"subject:Monday Motivation!\n\n{random_quote}"
        )
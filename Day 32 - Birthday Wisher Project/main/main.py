import datetime as dt
import smtplib
import pandas as pd
from random import randint

my_email = '''email'''
my_password = '''app password'''

now = dt.datetime.now()
today = (now.month, now.day)

birthday_df = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["email"]): data_row
    for (index, data_row) in birthday_df.iterrows()
    if (data_row["month"], data_row["day"]) == today
}

if birthdays_dict is not None:

    for (recipient_email, recipient_data) in birthdays_dict.items() :
        name = recipient_data["name"]
        email = recipient_email 
        letter_dir = f"./letter_templates/letter_{randint(1,3)}.txt"
        
        with open(letter_dir, "r") as letter:
            starting_letter = letter.read()
            new_letter = starting_letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=email,
                msg=f"subject:Happy Birthday!\n\n{new_letter}"
            )





---
tags:
  - 100_Days_of_Code
  - python
  - programming
---
# Day 32: Intermediate - Send Email (smtplib) & Manage Dates (datetime)

## Notes

### SMTP (Simple Mail Transfer Protocol)

![[vlc_wH7oWHAf4J.png]]

```python
import smtplib

my_email = #my main email
password = #my main email's app password
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=#email I want to send to,
        msg="subject:hello\n\nThis is the body of my email"
    )
#smtp.office365.com
```

### datetime lib

```python
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # starts with 0 as monday
print(year)

date_of_birth = dt.datetime(year=2003, month=5, day=7, hour=4)
print(date_of_birth)
```

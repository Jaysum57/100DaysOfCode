---
date: 
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 10: Functions with Outputs

# Notes

```python
def my_function():
	return 3*2

output = my_function # Output: 6
```

## Docstrings
```python
def format_name(f_name,l_name):
	""" This function takes two strings First Name and Last Name and converts it into title case """
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Hello {f_name} {l_name}"

formated_string = format_name("JudE,","AGUSTINO")
print(formated_string)

```

# Days in Month
##### Convert the is_leap() functtion

In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function `is_leap()` so that instead of printing "Leap year." or "Not leap year." it should **return** `True` if it is a leap year and **return** `False` if it is not a leap year.
##### Create a new function called days_in_month()

You are then going to modify a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.
```
days_in_month(year=2022, month=2)
```
And it will use this information to work out if the year is a leap year and decide the **number of days in the month**, then **return** that as the **output**, **e.g.:**
```
28
```

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

## Solution
```python
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
  if is_leap(year) and month == 2:
    return month_days[month-1]+1
  else:
    return month_days[month-1]
    
  
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

```


---
date: 
tags:
  - 100_Days_of_Code
---
# Day 2 - 100 days of Code

# Notes

```python
print(f"String {variable}") #format string with different variable types
```

>[!note] 
>For **better RAM efficiency, readability, and performance**, always prefer **f-strings** unless you have specific reasons to use concatenation. 

```
PEMDASLR (Order of operands, [par, exp, mul, div, add, sub, Left, Right] )

()
**
* /
+ -
```

---
# BMI Calculator
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

[BMI Wikipedia Page](https://en.wikipedia.org/wiki/Body_mass_index)

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![300](https://auditorium-storage.s3.eu-central-1.amazonaws.com/assets/ab9725bf-ed62-48ae-bd2e-5a97ff353c72)

NOTE: You should convert the BMI to a whole number and print out a whole number in order to pass all the tests. See examples below.

## Example Input 1

```
1.75
80
```

means: weight = 80 and height = 1.75
## Solution

```python
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2

# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)
```

### My solution

```python
height = input()
weight = input()

BMI = float(weight)/float(height) ** 2
print(int(BMI))
```

# Life in weeks problem
## Instructions  

I was reading this article by Tim Urban - [[Your Life in Weeks]] and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

```
You have x weeks left.
```

Where *x* is replaced with the actual calculated number of weeks the input age has left until age 90.

>[!warning] Warning 
>your output should match the Example Output format exactly, even the positions of the commas and full stops.

## Example Input

```
56
```
## Example Output

```
You have 1768 weeks left.
```
## Solution

```python
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")

```

# Final Project

## Scenario

```python
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
```
## Solution

```python
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? ")) / 100
people = int(input("How many people to split the bill? "))

payment = (bill * (1 + tip))/people
rounded_payment = "{:.2f}".format(payment)

print(f"Each person should pay: ${rounded_payment}")
```
>[!info] 
>"{:.2f}"


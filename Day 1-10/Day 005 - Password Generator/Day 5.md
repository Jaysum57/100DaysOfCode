---
date: 
tags:
  - 100_Days_of_Code
  - python
---
# Day 5: Python Loops

# Notes

## Loops
### For loop
```python
fruits = ['Apple','Peach','Pear']

for fruit in fruits:
  print(fruit + 'Pie')
```

### Accessing a specific list inside a list
```python
nums = ["1","2","3","4"]
letters = ["a","b","c","d"]

characters = [nums, letters]

for item in characters:
	if item == nums:
		print(item)
```

## Range
```python
number= [1,2,3,4,5,6,7,8,9,10]

for number in range(1,10): # not including 10
	print(number)
	
for number in range(1,10,2): # 2 is the step
	print(number)
```

### Gauss Problem using For in range
```python
list = []
for i in range (1,101):
	list.append(i)
print(sum(list))

total = 0
for number in range(1,101):
	total += number
print(total)
```
# Average height
You are going to write a program that calculates the average student height from a List of heights.

e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of **7** heights in `student_heights`

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = **164**

>[!Warning] **Important** 
>You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

## Solution
```python
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_heights = 0 
num_of_heights = 0

for height in student_heights:
  sum_of_heights += height
  num_of_heights += 1

avg_of_heights = round(sum_of_heights/num_of_heights)

print(f"total height = {sum_of_heights}")
print(f"number of students = {num_of_heights}") 
print(f"average height = {avg_of_heights}")
```

# High Score
You are going to write a program that calculates the highest score from a List of scores.

e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

```
The highest score in the class is: x
```

## Solution
```python
student_scores = [78,65,89,86,55,91,64,89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0

for current_score in student_scores:
  if highest_score < current_score:
    highest_score = current_score

print(f"The highest score in the class is: {highest_score}")
```

# Adding Even Numbers
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a **max of 1000**.

## Solution
```python
target = 52
total = 0
if target <= 1000:
  for num in range(2,target+1,2):
    total+= num
print(total)

```

# FizzBuzz
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100 in turn and include number 100.
- When the number is divisible by 3 then instead of printing the number it should print **"Fizz"**.
- When the number is divisible by 5, then instead of printing the number it should print **"Buzz"**.`
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print **"FizzBuzz"**

# Solution
```python
for num in range(1,101):
  if num % 3 == 0  and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
```

# Final Project: Random Password Generator

```python
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ''
# for n in range(1,nr_letters+1):
#   password += random.choice(letters)

# for n in range(1,nr_symbols+1):
#   password += random.choice(symbols)

# for n in range(1,nr_numbers+1):
#   password += random.choice(numbers)
  
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = [] 
for n in range(1,nr_letters+1):
  password.append(random.choice(letters))

for n in range(1,nr_symbols+1):
  password.append(random.choice(symbols))

for n in range(1,nr_numbers+1):
  password.append(random.choice(numbers))

random.shuffle(password)
print(''.join(password))
```

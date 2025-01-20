---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 26: Intermediate - List Comprehension and the NATO Alphabet

## Notes

### List Comprehension

- creating a list from a previous list

```python
numbers = [1, 2, 3]


# This:
new_list = [n + 1 for n in list]

#over this
new_list = []
for n in list:
  add_1 = n + 1

new_list.append(add_1)

```

```python
name = "Angela"

new_list = [char for char in name]

print(new_list) # ['A', 'n', 'g', 'e', 'l', 'a']
```

```python

new_list = [number*2 for number in range(1,5) ] # [1, 2, 3, 4]

print(new_list) # [2, 4, 6, 8]
```

### Conditional List Comprehension

```python
new_list = [new_item for item in list if test]
```

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Fredie"]
short_names = [name for name in names if len(name) < 5]
print(short_names) # ['Alex', 'Beth', 'Dave']
```

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Fredie"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names) # ['CAROLINE', 'ELENOR', 'FREDIE']
```

### Dictionary Comprehension

```python
new_dict = {new_key:new_value for item in list}
```

```python
new_dict = {new_key:new_value for (key, value) in dict.items()}
```

```python
new_dict = {new_key:new_value for (key, value) in dict.items() if test}
```

#### Example

```python
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Fredie"]
students_scores = {student:random.randint(1,100) for student in names}

print(students_scores) # {'Alex': 36, 'Beth': 40, 'Caroline': 32, 'Dave': 81, 'Elenor': 64, 'Fredie': 62}
```

```python
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Fredie"]

students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 50}

print(passed_students) # {'Alex': 86, 'Caroline': 86} 
```

### Looping through dictionaries

```python
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)
```

### Iterating over a pandas DataFrame

```python
import pandas

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(index) # print indexes
    print(row.student) # prints all students
    print(row.score) # prints all scores

  if row.student == "Angela":
    print(row.score)
```

## Squaring numbers

Instructions
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

e.g. 4 * 4 = 16
4 squared equals 16.
DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

Target Output
`[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]`

### Solution

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

```

## Filtering Even Numbers

Instructions
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.

First, use list comprehension to convert the list_of_strings to a list of integers.

Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.

Again, try to use Python's List Comprehension instead of a Loop.

Example Input
`9, 0, 32, 8, 2, 8, 64, 29, 42, 99`

Example Output
`[0, 32, 8, 2, 8, 64, 42]`

### Solution

```python
list_of_strings = input().split(',')
list_of_integers = [int(string) for string in list_of_strings]

result = [number for number in list_of_integers if number % 2 == 0]

print(result)
```

## Data Overlap

Instructions

💪 This exercise is HARD 💪

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if `file1.txt` contained:

1
2
3

and `file2.txt` contained:

2
3
4

`result = [2, 3]`

IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.

Example Output
`[3, 6, 5, 33, 12, 7, 42, 13]`

### Solution

```python
file1 = open("file1.txt", "r")
file1_list = file1.readlines()

file2 = open("file2.txt", "r")
file2_list = file2.readlines()

result = [int(num) for num in file1_list if num in file2_list]

print(result)
```

## Dictionary Comprehension1

Instructions

You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Example Input

`What is the Airspeed Velocity of an Unladen Swallow?`

Example Output

```python
{
'What': 4, 
'is': 2, 
'the': 3, 
'Airspeed': 8, 
'Velocity': 8, 
'of': 2, 
'an': 2, 
'Unladen': 7, 
'Swallow?': 8
}
```

### Solution

```python
sentence = input()
word_list = sentence.split()
result = {word: len(word) for word in word_list}

print(result)
```

## Dictionary Comprehension 2

Instructions  

You are going to use Dictionary Comprehension to create a dictionary called `weather_f` that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert `temp_c` into `temp_f` use this formula:

`(temp_c * 9/5) + 32 = temp_f`

![Celsius to Fahrenheit chart|300](https://auditorium-storage.s3.amazonaws.com/assets/a1a0f98b-fc42-46fc-b248-28744230060d)

**Do NOT** Create a dictionary directly. Try to use **Dictionary Comprehension** instead of a **Loop**.

The `eval()` function will help us convert the string input into a Python dictionary, provided that the inputs are already formatted with the correct syntax.

### Example Input

```python
{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
```

#### Example Output

{'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

### Solution

```python
weather_c = eval(input())

weather_f = {day:(celsius * 9/5) + 32 for (day, celsius) in weather_c.items()}


print(weather_f)
```

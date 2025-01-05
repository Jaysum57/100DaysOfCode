---
date: 05/01/2025
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 9: Beginner - Dictionaries, Nesting, and the Secret Auction

# Notes 
## Dictionary
```python
{
	Key: Value,
	Key: Value,
	Key: Value
}
```

|   Key    | Value                                                                     |
| :------: | :------------------------------------------------------------------------ |
|   Bug    | An error in a program that prevents the program from running as expected. |
| Function | A piece of code that you can easily call over and over again              |
|   Loop   | The action of doing something over and over again                         |
```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}
```
## Retrieving items from dictionary.
```python
print(programming_dictionary["Bug"])
```
## Adding new items to dictionary.
```python
programming_dictionary["Loop"] = "The action of doing something over and over again."
```
## Create an empty dictionary.
```python
empty_dictionary = {}
```
## Wipe an existing dictionary.
```python
programming_dictionary = {}
```
## Edit an item in a dictionary.
```python
programming_dictionary["Bug"] = "A moth in your computer."
```
## Loop through a dictionary.
```python
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # Access the value using the key.
```

## Nesting
```python
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
```

## Nesting a List in a Dictionary
```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
```
## Nesting Dictionary in a Dictionary
```python
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
```
## Nesting Dictionary in a List
```python
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
```

# Grading Program
You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the names of the students and the values are their exam scores.

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student names for **keys** and their **grades** for **values**.

The **final version** of the `student_grades` dictionary will be checked.

This is the scoring criteria:

- Scores 91 - 100: Grade = "Outstanding"
- Scores 81 - 90: Grade = "Exceeds Expectations"
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail"

## Solution
```python
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)
```

# Dictionary in List
You are going to write a program that adds to a `travel_log`. You can see a `travel_log` which is a **List** that contains 2 **Dictionaries**. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the `travel_log`.

```
add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
```

**DO NOT** modify the `travel_log` directly. The goal is to create a function that modifies it.

## Solution
```python
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
  # MY PREVIOUS SOLUTION
  # travel_log.append({
  #   "country": country,
  #   "visits": visits,
  #   "cities": list_of_cities
  # })
  new_country = {
    "country": country,
    "visits": visits,
    "cities": list_of_cities
  }
  travel_log.append(new_country) 

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
```
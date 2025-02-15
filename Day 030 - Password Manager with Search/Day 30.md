---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 30: Intermediate - Errors, Exceptions and JSON Data Improving the Password

## Notes

### KeyError

```python
a_dictionary = {"key": "value"}

value = a_dictionary("non_existent_key")
# KeyError: 'non_existent_key'
```

### IndexError

```python
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]
# IndexError: list index out of range
```

### TypeError

```python
text = "abc"
print(text + 5)
# TypeError: can only concatenate str (not "int") to str
```

### Catching Exceptions

```python
try # something that might cause anexception

except # Do this if there was an exception

else # Do this if there were no exceptions

finally # Do this no matter what happens
```

```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
     print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)

finally:
    file.close()

```

### Raise

```python
height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 1 meters")

bmi = weight/ (height**2)
print(bmi)
```

## IndexError Handling

Issue

We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're looking through the list of fruits for an index that is out of range.

Bad Output

Objective
Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie".

Example Input
`["Apple", "Pear", "Orange"]`

Example Output
`Fruit pie`

IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie".

### Solution

```python
fruits = eval(input())

def make_pie(index):
  try:
    fruit = fruits[index]
    print(fruit + " pie")
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")

make_pie(4)

```

## KeyError Handling

Instructions
We've got some buggy code, try running the code. The code will crash and give you a KeyError. This is because some of the posts in the facebook_posts don't have any "Likes".

Objective
Use what you've learnt about exception handling to prevent the program from crashing.

Example Input
`[{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]`

Using the eval() function we can create a list of dictionaries that looks like this:

```text
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]
```

Example Output
`86`

### Solution

```python
# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass


print(total_likes)
```

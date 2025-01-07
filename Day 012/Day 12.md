---
date: 
tags:
  - 100_Days_of_Code
  - python
  - programming
---
# Day 12: Scope & Guessing number

# Notes
## Local Scope
```python
def my_function():
	local_variable = 1
	print(local_variable)

print(local_variable) # Error: name 'local_variable' is not defined
```

## Global Scope
```python
global_variable = 3

def my_function():
	local_variable = 1
	print(global_variable) 

my_function() # Output: 3
```

## Global Keyword (NOT RECCOMMENDED)
```python
enemies = 2

def increase_enemies():
	global enemies
	enemies += 1
	print(f"enemies inside function: {enemies})

increase_enemies()
print(f"enemies outside function: {enemies}")
```

## Do this instead
```python
enemies = 2
def increase_enemies():
	return enemies + 1

increase_enemies()
print(f"enemies outside functions: {enemies}")

```

## Better to use global scope in constants

```python
# It's better to make constant variables into UPPERCASE

PI = 3.14159
URL = "https://www.somelink.com/"
TWITTER_HANDLE = "@jay_agust"
```
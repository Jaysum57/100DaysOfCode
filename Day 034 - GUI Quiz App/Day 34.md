---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 34: Intermediate+ API Practice - Creating a GUI Quiz App

## Notes

Open Trivia Database
https://opentdb.com/api_config.php

https://freeformatter.com/json-formatter.html

### Type Hints and arrows

```python
age: int
name: str
height: float
is_human: bool

age = "twelve" # Error: age type must be int

def police_check(age: int) -> bool: # -> : return type
	if age > 18:
		can_drive = True
	else:
		can_drive = False
	return can_drive

if police_check(19):
	print("You may pass.")
else:
	print("Pay a fine.")
```

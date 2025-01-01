---
date: 
tags:
  - 100_Days_of_Code
  - python
  - programming
---
# Day 6: Python Functions and Karel

# Notes
## Creating a function
```python
def my_function():
	print("Hello")
	print("Bye")
	
my_function()
```
## while loop
```python
while something_is_true:
	#do something
```

# hurdle 4
## My solution
```python
def jump():
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if not front_is_clear():
        turn_left()
        while wall_on_right() and front_is_clear():
            move()
        jump()
        while not wall_in_front():
            move()
        turn_left()
    else:
        move()
```
## Angela's solution
```python
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```

#
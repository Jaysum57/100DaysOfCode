---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 16: Intermediate - Object Oriented Programming

## Notes

### Procedural Programming

- where we setup procedures or functions that do particular things and then one procedure leads to another procedure.

### Object Oriented Programming

| **Class** | **Object** |
| --------- | ---------- |
| `Waiter`  | Henry      |
| `Waiter`  | Betty      |

Class: `Waiter`
Object: `Betty`, `Henry`

### Creating an object

```python
car = CarBlueprint()
```

`Carblueprint()` --> Class
`car` --> Object

#### car has attributes

```python
speed = 0
fuel = 32
```

```python
car.speed
```

car --> object
speed --> attribute

#### car has methods (functions)

```python
car.stop()
```

### Python Packages

- Different from modules
  
- its a whole bunch of code (lots of files) that are all packaged together

## Turtle

```python
from turtle import Turtle, Screen

# create new object called timmy with the class Turtle 
timmy = Turtle() 

print(timmy) # <turtle.Turtle object at 0x0000020DBABFA540> 
timmy.shape('turtle') # turns the object shape into a turtle
timmy.color('DarkGreen') # turns the object color into DarkGreen

# create new object called my_screen with the class Screen
my_screen = Screen() 

print(my_screen.canvheight) # 300
print(timmy.position()) # (0.00,0.00)

timmy.forward(100) # moves the object timmy forward 100 paces on object my_screen

my_screen.exitonclick() # close window when it detects a click
```

## Pretty Table

```python
from prettytable import PrettyTable

# create new object called table with the class PrettyTable
table = PrettyTable() 

# Add one column to table object with header: Pokemon name 
# rows as "Pikachu", "Squirtle", "Charmander"
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"]) 

# Add one column to table object with header: Pokemon name
# rows as "Electric", "Water", "Fire"
table.add_column("Type",["Electric", "Water", "Fire"])

#aligns the table to left-aligned
table.align = 'l' 
print(table.align) # {'base_align_value': 'c', 'Pokemon Name': 'l', 'Type': 'l'}
print(table) 
"""
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
"""
```

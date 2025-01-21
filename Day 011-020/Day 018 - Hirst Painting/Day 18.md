---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 18: Turtle & the Graphical User Interface (GUI)

## Notes

### TK

- short for tkinter
- used to make GUI (Graphical User Interface)

### From... import...

```python
from turtle import Turtle

tim = Turtle()
tom = Turtle()
tommy = Turtle()
```

### from... import * (not recommended)

```python
from random import *

choice([1,2,3,4,5]) #instead of random.choice() 
```

### Aliasing Modules

```python
import turtle as t

tim = t.Turtle()

```

### Installing Modules

we can look for python packages in [Python Package Index (Pypi)](https://pypi.org)

`pip install heroes` --> we can enter this in a python environment terminal

### Python Tuples

Tuples are like lists but the difference is that you are not able to change the value of a tuple.

- useful for when you don't want people to mess up with the values

```python
my_tuple = (1,2,3)

my_tuple[0] = 15 # error
```

#### Tuple to List conversion

If you've changed your mind about using tuples instead of using lists, you can simply convert a tuple into a list by using the `list()` function:

```python
my_tuple = (1,2,3)
print(my_tuple) # (1, 2, 3)

print(list(my_tuple)) # [1, 2, 3]
```

## Drawing a dashed line

```python
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(40):
    tim.forward(5)
    tim.pu()
    tim.forward(5)
    tim.pd()


screen = Screen()
screen.exitonclick()
```

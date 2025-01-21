---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 17: Intermediate - The Quiz Project & the Benefits of OOP

## Notes

### How to create a class

```python
class Car:
    #attributes, methods
```

### Naming Classes

#### Use Pascal Case

```python
class CarCamshaftPulley:
    pass
```

**PascalCase** - first letter of every word is capitalized

**camelCase** - first word is not capitalized and every subsequent.

**snake_case** - all the words are lowercased and every words are separated by an underscore

### Constructor

- allows us to specify what should happen when our object is being constructed
- also known as initializing an object

### How to make a Constructor

```python
class Car:
    def __init__(self):
        # initialize attributes
```

### Setting Attribute in Constructors

```python
class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5)
print(my_car)
```

`self` - is the OBJECT itself

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id    
        self.username = username

user_1 = User('001', 'jude')
user_2 = User('002', 'sophia')
```

### Methods vs. Functions

Methods

- are functions that are associated with an object.

Function

- is just a block of reusable code that accepts arguments.

### Create a method

```python
clase Car:
    def enter_race_mode(self):
        self.seats = 2
```

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id    
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'jude')
user_2 = User('002', 'sophia')

user_1.follow(user_2)

print("user 1:")
print(user_1.followers)
print(user_1.following)

print("user2:")
print(user_2.followers)
print(user_2.following)

```

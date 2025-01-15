---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 21: Build the Snake Game Part 2 Inheritance & List Slicing

## Notes

### Class Inheritance

| **Chef**  | **Pastry Chef** |
| --------- | --------------- |
| bake()    | bake()          |
| stir()    | stir()          |
| measure() | measure()       |
|           | knead()         |
|           | whisk()         |

```python
class Fish(Animal):
    def __init__(self):
        super().__init__()
```

#### Example

```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal): # Animal is the superclass

    def __init__(self):
        super().__init__()

def breathe(self):
    super().breath()
        print("doing this underwater.")

def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)
```

### Slicing

```python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
            #  0    1    2    3    4    5    6

# Accessing sublists using slicing
print(piano_keys[2:5])  # Prints "c", "d", "e"
print(piano_keys[2:])  # Prints "c", "d", "e", "f", "g"
print(piano_keys[:5])  # Prints "a", "b", "c", "d", "e"
print(piano_keys[2:5:2])  # Prints "c", "e" (skips every other element)
print(piano_keys[::2]) # Prints "a" "c" "e" "g"
print(piano_keys[::-1]) # Prints "g" "f" "e" "d" "c" "b" "a" (reverse)
```

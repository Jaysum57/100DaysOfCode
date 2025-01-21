---
date: 
tags:
  - 100_Days_of_Code
---
# Day 4: Randomization and python lists

# Notes

## What is a module?
* When the code is getting too long and it would be harder to read it, the code is split into separate "modules" where each module is responsible for each functionality of your program. 

## Random Module
```python
import random

random_int = random.randint(1,10) # generate a random number from 1-10
print(random_int)
```

### What is a data structure?
* a way or algorithm for storing data.
## Python List

```python
fruits = ["item1", "item2", "item3"]

print(fruits[0]) # first on the list
print(fruits[-1]) # start from the last of the list

fruits[0] = "Apple" # reassigning in fruits[0]
print(fruits[0])

# adding an item to an end of a list
fruits.append("Orange")
print(fruits[-1])

#adding multiple items to the end of the list
fruits.extend(["Grapes", "Mango"])
print(fruits)
```

## Nested List

```python
nums = ["1","2","3","4"]
letters = ["a","b","c","d"]

characters = [nums, letters]
print(characters)
```

# Heads or Tails
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", **not** "heads".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

## Solution
```python
import random

result = random.randint(0,1)

if result == 1:
  print("Heads")
else:
  print("Tails")
```

# Banker Roulette
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

**Important**: You are not allowed to use the `choice()` function.

NOTE: In this exercise, you are working collaboratively with another programmer. They already dealt with `input()` and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.

The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called `names`. For their code to work correctly, you must enter all the names in the input area followed by comma then space. e.g. name, name, name

You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).

Assume that `names` works like this:

```
input area: x, y, z, 
names = ["x", "y", "z"]
```

## Solution
```python
import random
length_names = len(names)
random_name = random.randint(0,length_names-1)
print(f"{names[random_name]} is going to buy the meal today!")
```

# Treasure Map (HARD)
This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an `X`.

In the starting code, you will find a variable called `map`.

This `map` contains a nested list. When `map` is printed this is what it looks like, notice the nesting:

`[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]`

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code `print(f"{line1}\n{line2}\n{line3}")` to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

```
['⬜', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

Now it looks a bit more like the coordinates of a real map:

![300](https://auditorium-storage.s3.amazonaws.com/assets/f957d61b-ea70-4634-81de-94e753fe7e13)

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

![300](https://auditorium-storage.s3.eu-central-1.amazonaws.com/assets/1fe4ca84-33b2-499e-8967-fe005daaf2d2)

So an input of A3 should place an X at the position shown below:

![300](https://auditorium-storage.s3.eu-central-1.amazonaws.com/assets/69f93f28-16be-441f-be2a-133832eb4eb0)

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

```
[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
```

## Solution
```python
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = 'B3'#input()
columns = ['a','b','c']
col = columns.index(position[0].lower())
row = int(position[1])-1

map[row][col] = 'X'
print(f"{line1}\n{line2}\n{line3}")
```

# Final Project - Rock, Paper, Scissor

## Solution
```python
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

choices = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

if user > 3 or user < 0:
    print("Invalid choice!")
else:
    print(choices[user])
    print("Computer chose:")
    print(choices[computer])
    if user == computer:
        print("It's a draw")
    elif user == 0 and computer == 2:
        print("You Win!")
    elif computer == 0 and user == 2:
        print("You Lose!")
    elif computer > user:
        print("You Lose!")
    elif user > computer:
        print("You Win!")
```
---
date: 
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 8: Function Parameters & Caesar Cipher

# Notes
## Functions with inputs
```python
def my_function(something):
	#Do this with something
	#Then do this
	#Finally do this

my_function(123)
```

```
something = 123
```

`something` - parameter
`123` - argument

## Positional Argument
```python
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Dumaguete", "Jude") 
```

## Keyword Argument
```python

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name="Jude", location="Dumaguete")
```

# Paint Area Calculator
You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

```
number of cans = (2 * 4) / 5
               = 1.6
```

But because you can't buy 0.6 of a can of paint, the result should be **rounded up to 2** cans.

**IMPORTANT**: Notice the name of the function and parameters must match those on line 13 for the code to work.

```python
from math import ceil

def paint_calc(height, width, cover):
  num_of_cans = ceil((height * width) / cover)
  print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

```

# Prime Number Checker
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)

**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

![Prime number graphic|300](https://auditorium-storage.s3.amazonaws.com/assets/19db279b-10a7-4f24-8b4a-46401658e30d)

Here are the numbers up to 100, prime numbers are highlighted in yellow:

![First 100 Primes|300](https://auditorium-storage.s3.eu-central-1.amazonaws.com/assets/1bcfc529-8afa-426f-adda-8add07274e9a)

```python

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
      
n = int(input())
prime_checker(number=n)
```

# Final Project: Caesar Cipher

```python
# Future Implementation: Support case sensitive text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    output_text = ""

    if direction == "decode":
        shift *= -1
    
    for char in text:
        if char not in alphabet:
            output_text += char
            continue
        alphabet_index = alphabet.index(char)
        new_index = alphabet_index + shift
        if new_index > 25:
            new_index -= 26
        elif new_index < 0:
            new_index += 26
        output_text += alphabet[new_index]

    print(f"The {direction}d text is \"{output_text}\"")

# main function

from art import logo
from os import system
Loop = True
while Loop == True:
    print(logo) 

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(text, shift, direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if choice == "no":
        Loop = False
        print("Goodbye")
    elif choice == "yes":
        system('cls')
        continue
```

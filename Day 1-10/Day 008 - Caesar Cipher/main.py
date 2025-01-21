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
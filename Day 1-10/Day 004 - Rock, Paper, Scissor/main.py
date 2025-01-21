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
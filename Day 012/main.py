""" 
TODO 🗒️ :
  - set difficulty
  - set attempts based on difficulty
  - generate random number
  - loop guess the number 
    - Check if guess is wrong/right 
    - if wrong minus attempt
    - if right game over
  - try again prompt
"""

from art import logo
from random import randint
from os import system

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def logo_and_ui():
  """
  Displays the game logo and user interface messages.

  This function prints the game logo, a welcome message, and instructions
  for the Number Guessing Game. It informs the player that the game involves
  guessing a number between 1 and 100.
  """
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

def set_attempts():
  """
  Prompts the user to choose a difficulty level and returns the number of attempts
  based on the chosen difficulty.
  Returns:
    int: The number of attempts for the chosen difficulty level.
       Returns EASY_ATTEMPTS if 'easy' is chosen, and HARD_ATTEMPTS if 'hard' is chosen.
  """
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulty == 'easy':
    return EASY_ATTEMPTS
  elif difficulty == 'hard':
    return HARD_ATTEMPTS

def check_guess(guess,random_number, attempts):
  """
  Compares the user's guess to the random number and provides feedback.

  Parameters:
  guess (int): The user's guessed number.
  random_number (int): The randomly generated number to be guessed.
  attempts (int): The number of attempts remaining.

  Returns:
  int: The updated number of attempts remaining if the guess is incorrect.
  None: If the guess is correct.
  """
  if guess > random_number:
    print("Too high.")
    input()
    return attempts - 1
  elif guess < random_number:
    print("Too low.")
    input()
    return attempts - 1
  else:
    print(f"You got it! The answer was {random_number}.")
    input()
    return None
  
def start_game():
  """
  Starts the number guessing game.
  The game generates a random number between 1 and 100 and allows the player to guess the number.
  The player has a limited number of attempts to guess the correct number based on the chosen difficulty level.
  The game provides feedback on the number of remaining attempts and whether the guess was correct.
  If the player runs out of attempts, the game ends and reveals the correct number.
  Functions:
  - logo_and_ui(): Displays the game logo and user interface.
  - get_difficulty(): Prompts the player to select a difficulty level and returns the number of attempts.
  - set_attempts(difficulty): Sets the number of attempts based on the selected difficulty level.
  - check_guess(guess, random_number): Checks the player's guess against the random number and returns whether the guess was correct.
  The game continues until the player guesses the correct number or runs out of attempts.
  """
  game_over = False
  random_number = randint(1,100)
  logo_and_ui()
  attempts = set_attempts()

  while not game_over:
    system('cls')
    print(logo)
    print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"psst the number is: {random_number}")
    guess = int(input("Make a guess: "))

    result = check_guess(guess, random_number, attempts)
    
    if result is None:
        game_over = True
    else:
        attempts = result
        if attempts == 0:
            print(f"You've run out of guesses. The number was {random_number}")
            print("GAME OVER. 🥲")
            input()
            game_over = True

# Main
end_game = False

while not end_game:
  print(logo)
  
  decision = input("Do you want to play Guess the Number? 'y/n': ").lower()
  
  if decision == 'y':
    system('cls')
    start_game()
  elif decision == 'n':
    end_game = True
  else:
    print("Input invalid. Try again")
    input()
  system('cls')

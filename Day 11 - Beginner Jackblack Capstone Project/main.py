############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def deal_card():
    """
    Returns a random card from a standard deck of cards.

    The deck is represented as a list of integers where:
    - 11 represents an Ace
    - 2-10 represent the numbered cards
    - 10 represents the face cards (Jack, Queen, King)

    Returns:
        int: A randomly selected card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def start_game(player_cards, computer_cards):
    """
    Initializes the game by clearing the player's and computer's cards and dealing two new cards to each.
    Args:
        player_cards (list): The list of cards currently held by the player.
        computer_cards (list): The list of cards currently held by the computer.
    Returns:
        None
    """

    if player_cards is not None:
        player_cards.clear()
    
    if computer_cards is not None:
        computer_cards.clear()

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

def check_condition(player_score, computer_score):
    """
    Determines the outcome of a game based on the player's and computer's scores.

    Args:
        player_score (int): The score of the player.
        computer_score (int): The score of the computer.

    Returns:
        None: Prints the result of the game.
    """
    if player_score == computer_score:
        print("It's a draw 🙃")
    elif player_score > 21:
        print("You went over. You lose 😔")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif player_score > computer_score:
        print("You win 😁")
    else:
        print("You lose 😭")

def player_turn(player_cards, computer_cards):
    """
    Manages the player's turn in a game of Blackjack.
    Parameters:
    end_of_player (bool): A flag indicating whether the player's turn has ended.
    player_cards (list): A list of integers representing the player's current cards.
    computer_cards (list): A list of integers representing the computer's current cards.
    The function will continue to prompt the player to either draw another card or pass until the player's turn ends.
    If the player's score exceeds 21, the turn ends automatically.
    """
    end_of_player = False
    if calculate_score(player_cards) == 21:
        end_of_player = True
    while not end_of_player:
        player_score = calculate_score(player_cards)

        if player_score >= 21:
            end_of_player = True
        else:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            
            decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
            if decision == 'y':
                player_cards.append(deal_card())
            elif decision == 'n':
                end_of_player = True
            else:
                input("Invalid character input. Press any key to continue...")

def computer_turn(computer_cards):
    """
    Simulates the computer's turn in a card game.
    The computer will keep drawing cards until its score is 17 or higher, or it hits 21.
    The function modifies the computer_cards list in place.
    Args:
        computer_cards (list): A list of integers representing the computer's current hand of cards.
    Returns:
        None
    """
    end_of_computer = False
    if calculate_score(computer_cards) == 21:
        end_of_computer = True

    while not end_of_computer:
        computer_score = calculate_score(computer_cards)
        if computer_score < 17:
            computer_cards.append(deal_card())
        else:
            end_of_computer = True

def end_game(player_cards, computer_cards):
    """
    Ends the game by calculating and displaying the final scores of the player and the computer,
    and then checks the game condition to determine the winner.

    Args:
        player_cards (list): A list of integers representing the player's cards.
        computer_cards (list): A list of integers representing the computer's cards.

    Returns:
        None
    """
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    check_condition(player_score, computer_score)

# Main
import random
from art import logo
from os import system

player_cards = []
computer_cards = []

while True:
    system('cls')
    print(logo)
    should_continue = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if should_continue == 'n':
        break
    elif should_continue == 'y':
        start_game(player_cards, computer_cards)
        player_turn(player_cards, computer_cards)
        computer_turn(computer_cards)
        end_game(player_cards, computer_cards)
        input("Press any key to continue...")
    else:
        print("Invalid input. Please type 'y' or 'n'.") 
#future implementation:
# 1. Allow cents in the bid

from os import system
from art import logo

bidders = {}
bidding_finished = False

def add_bidder(name, bid):
    bidders[name] = bid

def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""

    for person in bidders:
        bid_amount = bidders[person]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            highest_bidder = person
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# Main Program
while not bidding_finished:
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your Name?: ")
    bid = int(input("What's your bid?: $"))
    add_bidder(name, bid)
    
    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if decision == "no":
        bidding_finished = True
    elif decision == "yes":
        system('cls')

find_highest_bidder(bidders)



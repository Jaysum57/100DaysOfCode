# import modules
from art import logo, vs
from game_data import data
import random
from os import system

def get_random_element():
    return random.choice(data)

def show_element(element):
    name = element["name"]
    description = element["description"]
    country = element["country"]
    return f"{name}, a {description} from {country}."

def get_higher(A, B):
    count_A = A["follower_count"] 
    count_B = B["follower_count"]
    
    if count_A > count_B:
        return "A"
    else:
        return "B"

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False

score = 0
element_A = get_random_element()
element_B = get_random_element()
game_over = False

print(logo)
while not game_over:

    while element_A == element_B: # if element A is equal to B, get another random element B
        element_B = get_random_element()

    print(f"Compare A: {show_element(element_A)}")
    print(vs)
    print(f"Compare B: {show_element(element_B)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    is_correct = check_answer(answer, get_higher(element_A, element_B))

    system('cls')
    print(logo)

    if is_correct:
        score +=1
        print(f"You are right! Current Score: {score}")
        element_A = element_B
        element_B = get_random_element()
    else:
        game_over = True
        print(f"Sorry that's wrong. Final score: {score}")
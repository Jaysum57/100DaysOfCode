from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = randint(1,10)
        turtle.forward(rand_distance)

        if turtle.xcor() >=210:
            is_race_on = False
            winner = turtle.pencolor()
            print(f"{winner.title()} turtle has won.")
            if winner == bet:
                 print("You win!")
            else:
                print("You Lose!")

screen.exitonclick()

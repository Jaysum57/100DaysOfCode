from turtle import Turtle, Screen, colormode
from random import randint, choice

def random_color():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return (r, g, b)

tim = Turtle()
tim.pensize(10)
tim.pendown()
tim.speed(0)
screen = Screen()
colormode(255)

choice_move = [tim.forward, tim.back]
heading = [0,90,180,270]

while True:
    tim.color(random_color())
    choice(choice_move)(20)
    tim.setheading(choice(heading))

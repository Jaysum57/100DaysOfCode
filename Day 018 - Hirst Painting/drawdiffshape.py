from turtle import Turtle, Screen, colormode
from random import randint

def random_color():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return (r, g, b)

screen = Screen()
colormode(255)

tim = Turtle()
tim.shape("turtle")

for i in range(3,11):
    angle = 360/i
    tim.color(random_color())
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)

screen.exitonclick()
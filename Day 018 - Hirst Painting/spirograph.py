from turtle import Turtle, Screen, colormode
from random import randint

def random_color():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return (r, g, b)

def draw_circle(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(gap)
    

screen = Screen()
colormode(255)

tim = Turtle()
tim.speed(0)

draw_circle(5)

screen.exitonclick()
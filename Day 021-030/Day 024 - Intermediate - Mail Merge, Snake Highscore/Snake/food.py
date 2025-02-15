from turtle import Turtle
from random import randint

def rand_coordinates():
    return(randint(-280,280), randint(-280,280))


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.0, stretch_wid=1.0)
        self.color("blue")
        self.speed("fastest")
        self.goto(rand_coordinates())

    def refresh(self):
        self.goto(rand_coordinates())

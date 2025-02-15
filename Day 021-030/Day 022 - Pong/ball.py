from turtle import Turtle
import time

class Ball(Turtle):
    
    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
    
    def move(self):
        # print(f"x: {self.xcor()}")
        # print(f"y: {self.ycor()}")
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9

    def reset_position(self):
        self.bounce_x()
        self.home()
        self.move_speed = 0.05
        # time.sleep(1)

    def increase_speed(self):
        self.x_move +=5
        self.y_move +=5
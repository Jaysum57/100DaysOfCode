from turtle import Turtle

MOVE_DISTANCE = 50

class Paddle(Turtle):
    
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1,None)
        self.penup()
        self.teleport(x_cor, y_cor)
        
    def move_up(self):
        self.goto((self.xcor(), self.ycor() + MOVE_DISTANCE))
    
    def move_down(self):
        self.goto((self.xcor(), self.ycor() - MOVE_DISTANCE))

from turtle import Turtle
MOVE_DISTANCE = 20
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in POSITIONS:
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.snake_body.append(snake_segment)
    
    def move(self):
        for segment in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[segment -1].xcor() 
            new_y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    
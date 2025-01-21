from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_right():
    tim.right(45)

def move_left():
    tim.left(45)

def clear_drawing():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
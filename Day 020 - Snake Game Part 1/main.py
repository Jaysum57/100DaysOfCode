from turtle import Screen
from snake import Snake
import time

snake = Snake()

WIDTH = 600
HEIGHT = 600


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Down",fun=snake.move_down)
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

screen.exitonclick()
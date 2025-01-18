from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Wall collision
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()

    # Body collision
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
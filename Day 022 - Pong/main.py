from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# IDEA: turn the paddle body into a list

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()
player_paddle = Paddle(350.0,0)
opponent_paddle = Paddle(-350.0,0)

screen.listen()

# player movement functions
screen.onkey(key="Up",fun=player_paddle.move_up)
screen.onkey(key="Down",fun=player_paddle.move_down)

# opponent movement functions
screen.onkey(key="w",fun=opponent_paddle.move_up)
screen.onkey(key="s",fun=opponent_paddle.move_down)


game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Wall collision (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision (player paddle)
    if ball.distance(player_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    # Paddle collision (opponent paddle)
    if ball.distance(opponent_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball miss on right
    if ball.xcor() > 400 :
        scoreboard.opponent_point()
        ball.reset_position()
    
    # Ball miss on left
    if ball.xcor() < -400 :
        scoreboard.player_point()
        ball.reset_position()


    
screen.exitonclick()
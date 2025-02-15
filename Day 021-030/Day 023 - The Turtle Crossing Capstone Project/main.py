import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False 
    
    if player.is_finished():
        scoreboard.increase_level()
        car_manager.reset_cars()
        car_manager.increase_car_speed()
        player.reset_position()

screen.exitonclick()
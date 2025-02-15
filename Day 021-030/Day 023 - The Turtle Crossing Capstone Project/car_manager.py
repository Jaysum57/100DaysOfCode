from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            New_car = Turtle ("square")
            New_car.penup()
            New_car.shapesize(1,2, None)
            New_car.color(random.choice(COLORS))
            New_car.goto(300,random.randint(-250,250))
            self.cars.append(New_car)
        
    def move_cars(self):
        for car in self.cars:
            car.seth(180)
            car.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()


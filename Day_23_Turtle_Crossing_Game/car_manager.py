from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.create_car()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        #only generate a car every 1 in 6 times
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            rand_y = random.randint(-250,250)
            new_car.goto(300,rand_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_speed)





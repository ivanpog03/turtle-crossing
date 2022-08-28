import player
from turtle import *
import random
import scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            ccar = Turtle("square")
            ccar.penup()
            ccar.shapesize(stretch_len=2, stretch_wid=1)
            ccar.color(COLORS[random.randint(0, 5)])
            ccar.speed("fastest")
            random_y = random.randint(-280, 280)
            ccar.goto(300, random_y)
            self.all_cars.append(ccar)

    def move(self):
        for car in self.all_cars:
            car.backward(5)


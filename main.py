import time
from turtle import *
from player import *
from car_manager import *
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player(0, -280)

screen.listen()

car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car)<20:
            game_is_on=False
            scoreboard.game_over()

    if player.ycor() >= 280:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        player.goto(0, -280)

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect lvl up)
    if player.check_position():
        scoreboard.increase_lvl()
        car_manager.increase_car_speed()

screen.exitonclick()

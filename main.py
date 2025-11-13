import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

cars = []
iteration_count = 0


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if iteration_count == 6:
        cars.append(CarManager())
        iteration_count = 0

    for i in cars:
        i.move()

    # detect collision with car
    for i in cars:
        if player.distance(i) < 20:
            game_is_on = False


    iteration_count += 1

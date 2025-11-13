COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid= 1, stretch_len= 2)
        self.penup()
        self.goto(300, random.randint(-250,250))
        self.left(180)


    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
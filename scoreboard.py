FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.color("black")
        self.penup()
        self.goto(-200,250)
        self.write_lvl()

    def write_lvl(self):
        self.write(f"Level: {self.lvl}",False, "Center", FONT)


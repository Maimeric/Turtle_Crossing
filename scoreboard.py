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
        self.hideturtle()

    def write_lvl(self):
        self.clear()
        self.write(f"Level: {self.lvl}",False, "Center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "Center", FONT)

    def increase_lvl(self):
        self.lvl += 1
        self.write_lvl()
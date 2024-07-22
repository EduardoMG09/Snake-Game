from turtle import Turtle
ALLIGN = "center"
FONT = "Arial"
SIZE = 24
STYLE = "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.puntuation = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.puntuation}", align=ALLIGN, font=(FONT, SIZE, STYLE))

    def increase_score(self):
        self.puntuation+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over!", align=ALLIGN, font=(FONT, SIZE, STYLE))


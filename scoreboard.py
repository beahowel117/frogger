from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

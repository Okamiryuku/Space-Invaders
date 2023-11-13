from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "bold")


class ScoreBoard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, 550)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

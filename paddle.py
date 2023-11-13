from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_pos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(paddle_pos)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

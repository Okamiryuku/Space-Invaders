from turtle import Turtle


class Spaceship(Turtle):

    def __init__(self, paddle_pos):
        super().__init__()
        self.speed("fastest")
        self.shape("triangle")
        self.color("white")
        self.tilt(90)
        self.penup()
        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.goto(paddle_pos)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

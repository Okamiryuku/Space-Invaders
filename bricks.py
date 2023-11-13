from turtle import Turtle


class Brick(Turtle):

    def __init__(self, brick_pos, width, color):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color(color)
        self.penup()
        self.turtlesize(stretch_wid=2, stretch_len=width)
        self.goto(brick_pos)

    def delete_brick(self):
        self.hideturtle()

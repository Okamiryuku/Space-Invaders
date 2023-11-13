from turtle import Turtle


class Brick(Turtle):

    def __init__(self, brick_pos, color):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.color(color)
        self.tilt(-90)
        self.x_move = 10
        self.move_speed = 0.1
        self.penup()
        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.goto(brick_pos)

    def delete_brick(self):
        self.hideturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x)

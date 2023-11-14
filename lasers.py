from turtle import Turtle


class Laser(Turtle):

    def __init__(self, ball_pos):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.2
        self.turtlesize(stretch_wid=.5, stretch_len=.5)
        self.goto(ball_pos)

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_up(self):
        self.x_move *= -1

    def move_down(self):
        self.x_move *= -1

    def delete_laser(self):
        self.hideturtle()

    def laser_speed(self):
        self.move_speed *= .6
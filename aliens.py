from turtle import Turtle


class Aliens(Turtle):

    def __init__(self, alien_pos, color):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.color(color)
        self.tilt(-90)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.penup()
        self.turtlesize(stretch_wid=2, stretch_len=2)
        self.goto(alien_pos)

    def delete_alien(self):
        self.hideturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def move_left(self):
        self.x_move *= -1

    def move_right(self):
        self.x_move *= -1

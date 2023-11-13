from turtle import Turtle


class Ball(Turtle):

    def __init__(self, ball_pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.goto(ball_pos)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def paddle_bounce(self):
        self.y_move *= -1

    def brick_bounce(self):
        self.y_move *= -1

    def ball_speed(self):
        self.move_speed *= .6

    def reset_position(self):
        self.goto(0, -530)
        self.move_speed = 0.1
        self.paddle_bounce()

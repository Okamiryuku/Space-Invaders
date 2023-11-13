import time
from turtle import Screen
from spaceship import Spaceship
from ball import Ball
from score import ScoreBoard
from aliens import Aliens
import random


BALL_SPEED_PARAM = 10  # If the score gets over this the ball moves faster
COLORS = ["white", "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "grey", "cyan"]

# Window Setup
screen = Screen()
screen.setup(width=800, height=1200)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Calling classes
spaceship = Spaceship((0, -550))
ball = Ball((spaceship.xcor(), spaceship.ycor()))
list_aliens = []  # My list of Spaceships Objects

# Set the initial position for the first line of spaceships
y_pos = 390
spaceship_count = 9  # Number of bricks in a row


# Loop to create multiple rows of bricks
for _ in range(5):
    x_pos = -380
    random_color = random.choice(COLORS)
    for _ in range(spaceship_count):
        alien = Aliens((x_pos, y_pos), color=random_color)
        list_aliens.append(alien)
        x_pos += 50
    y_pos -= 50

# Player Scoreboard
scoreboard = ScoreBoard(0)

# Registering Commands
screen.listen()
screen.onkeypress(spaceship.move_right, "d")
screen.onkeypress(spaceship.move_left, "a")

# Running the Game
game_is_on = True
c_move = False
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 585:
        ball.bounce_y()

    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.bounce_x()

    if ball.ycor() < -600:
        scoreboard.game_over()
        game_is_on = False

    if len(list_aliens) == 0:
        scoreboard.win()
        game_is_on = False

    # Alien movement
    if list_aliens[8].xcor() > 400:
        for n in range(len(list_aliens)):
            list_aliens[n].move_left()

    if list_aliens[0].xcor() < -400:
        for n in range(len(list_aliens)):
            list_aliens[n].move_right()
        c_move = False

    for alien_status in list_aliens:
        alien_status.move()

        # Alien laser collision
        if ball.distance(alien_status) < 20:
            alien_status.delete_alien()
            scoreboard.increase_score()
            list_aliens.remove(alien_status)

    if scoreboard.score > BALL_SPEED_PARAM:
        ball.ball_speed()
        BALL_SPEED_PARAM += 5

screen.exitonclick()

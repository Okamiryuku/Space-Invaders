import time
from turtle import Screen
from spaceship import Spaceship
from lasers import Laser
from score import ScoreBoard
from aliens import Aliens
import random


BALL_SPEED_PARAM = 10  # If the score gets over this the ball moves faster
COLORS = ["red", "green", "blue", "yellow", "orange", "purple", "grey", "cyan"]
LIVES = 3

# Window Setup
screen = Screen()
screen.setup(width=800, height=1200)
screen.bgpic("Space.gif")  # Background image
screen.title("Space Invaders")
screen.tracer(0)

# Calling classes
spaceship = Spaceship((0, -550))
list_aliens = []  # My list of Spaceships Objects
user_lasers = []  # My list of Lasers
alien_lasers = []  # My list of Lasers

# Set the initial position for the first line of spaceships
y_pos = 390
spaceship_count = 9  # Number of spaceships in a row


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


# Shooting Lasers
def laser_shot():
    laser = Laser((spaceship.xcor(), spaceship.ycor()))
    laser.move()
    user_lasers.append(laser)
    user_lasers[-1].move_up()


# Registering Commands
screen.listen()
screen.onkeypress(spaceship.move_right, "d")
screen.onkeypress(spaceship.move_left, "a")
screen.onkeypress(laser_shot, "space")

# Running the Game
game_is_on = True

while game_is_on:
    time.sleep(.6)
    screen.update()

    if len(list_aliens) == 0:
        scoreboard.win()
        game_is_on = False

        # User Lasers Out of Bounds
        for laser in user_lasers:
            if laser.ycor() > 600:
                laser.delete_laser()
                user_lasers.remove(laser)

        # Alien Lasers Out of Bounds
        for laser in alien_lasers:
            if laser.ycor() < -600:
                laser.delete_laser()
                alien_lasers.remove(laser)

        # Alien Lasers Hit the User
        for laser in alien_lasers:
            if laser.distance(spaceship) < 30:
                LIVES -= 1
                laser.delete_laser()
                alien_lasers.remove(laser)

        # Checking User Lives
        if LIVES == 0:
            scoreboard.game_over()
            game_is_on = False

    # Alien movement
    for alien in list_aliens:
        if alien.xcor() > 400:
            alien.move_left()

    for alien in list_aliens:
        if alien.xcor() < -400:
            alien.move_right()

    for alien_status in list_aliens:
        alien_status.move()

        # Alien laser collision
        # for laser in user_lasers:
        #     if laser.distance(alien_status) > 20:
        #         alien_status.delete_alien()
        #         scoreboard.increase_score()
        #         list_aliens.remove(alien_status)
        #
        # # Shooting lasers
        # if random.randint(0, 16) == 2:
        #     random_choice = random.choice(list_aliens)
        #     laser_shot()


screen.exitonclick()

import time
from turtle import Screen
from spaceship import Spaceship
from lasers import Laser
from score import ScoreBoard
from aliens import Aliens
import random


BALL_SPEED_PARAM = 10  # If the score gets over this the ball moves faster
COLORS = ["red", "green", "yellow", "orange", "purple", "cyan"]
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
scoreboard = ScoreBoard(0, lives=LIVES)


# Shooting Lasers
def laser_shot():
    u_laser = Laser((spaceship.xcor(), spaceship.ycor()), color="yellow")
    user_lasers.append(u_laser)


def alien_laser_shot(alien_pos):
    a_laser = Laser((alien_pos.xcor(), alien_pos.ycor()), color="red")
    alien_lasers.append(a_laser)


# Registering Commands
screen.listen()
screen.onkeypress(spaceship.move_right, "d")
screen.onkeypress(spaceship.move_left, "a")
screen.onkey(laser_shot, "space")

# Running the Game
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(list_aliens) == 0:
        scoreboard.win()
        game_is_on = False

    # Laser Movement
    for ul in user_lasers:
        ul.move_up()

    for al in alien_lasers:
        al.move_down()

    # User Lasers Out of Bounds
    for ul in user_lasers:
        if ul.ycor() > 600:
            ul.delete_laser()
            user_lasers.remove(ul)

    # Alien Lasers Out of Bounds
    for al in alien_lasers:
        if al.ycor() < -600:
            al.delete_laser()
            alien_lasers.remove(al)

    # Alien Lasers Hit the User
    for al in alien_lasers:
        if al.distance(spaceship) < 20:
            LIVES -= 1
            al.delete_laser()
            alien_lasers.remove(al)
            scoreboard.decrease_lives()

    # Checking User Lives
    if LIVES == 0:
        scoreboard.game_over()
        game_is_on = False

    # Alien movement
    for alien in list_aliens:
        if alien.xcor() > 400:
            for n in range(len(list_aliens)):
                list_aliens[n].move_left()

    for alien in list_aliens:
        if alien.xcor() < -400:
            for n in range(len(list_aliens)):
                list_aliens[n].move_right()

    for alien in list_aliens:
        alien.move()

    # Alien laser collision
    for alien in list_aliens:
        for ul in user_lasers:
            if ul.distance(alien) < 20:
                alien.delete_alien()
                ul.delete_laser()
                scoreboard.increase_score()
                user_lasers.remove(ul)
                list_aliens.remove(alien)

    # Shooting lasers
    for alien in list_aliens:
        if random.randint(0, 300) == 2:
            random_choice = random.choice(list_aliens)
            alien_laser_shot(alien)


screen.exitonclick()

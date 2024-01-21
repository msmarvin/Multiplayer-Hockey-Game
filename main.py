import time
import random
import pygame as pg
import utilities
import client
import asyncio
import server

pg.init()

# Constants
width, height = 1000, 600
black = (0, 0, 0)
white = (255, 255, 255)

blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
degree = "init"

# Variables
x1 = x2 = y1 = y2 = 1
ball_speed = [1, 1]
color = red
count = 0
hit_count = 0
sidehit_count = 0
angle_check = False
hitpad_left_movement_check = False
hitpad_right_movement_check = False
hitpad_speed = [0, 0]
hitpad_speed_increment = 5

# Window init
screen = pg.display.set_mode((width, height))

# Caption Set
pg.display.set_caption("Batu Game V1")

# Font set
font = pg.font.Font(None, 36)

# Ball Object
ball = pg.draw.circle(
    surface=screen, color=red, center=[100, 100], radius=40
)

# Hitpad Object
hitpad = pg.draw.rect(
    surface=screen, color=white, rect=pg.Rect(350, 50, 200, 25), border_radius=25
)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            # Hit esc to quit
            if event.key == pg.K_ESCAPE:
                exit()
            # When hit enter increase speed
            elif event.key == pg.K_RETURN:
                utilities.speedAcc(ball_speed, 5)
            # To detect
            if event.key == pg.K_LEFT:
                hitpad_left_movement_check = True
            elif event.key == pg.K_RIGHT:
                hitpad_right_movement_check = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                hitpad_left_movement_check = False
            elif event.key == pg.K_RIGHT:
                hitpad_right_movement_check = False

    if hitpad_right_movement_check:
        hitpad_speed[0] = hitpad_speed_increment
    elif hitpad_left_movement_check:
        hitpad_speed[0] = -hitpad_speed_increment
    else:
        hitpad_speed[0] = 0

    ball = ball.move(ball_speed)
    hitpad = hitpad.move(hitpad_speed)

    screen.fill(black)

    # Draw circle in every render
    pg.draw.circle(
        surface=screen, color=color, center=ball.center, radius=40
    )

    # Draw hitpad in every render
    pg.draw.rect(
        surface=screen, color=white, rect=pg.Rect(hitpad.left, 550, 200, 25), border_radius=25
    )

    # To keep ball inside the border
    if ball.left <= 0 or ball.right >= width:
        color = utilities.randomizeColor()
        ball_speed[0] = -ball_speed[0]
        angle_check = True
        sidehit_count += 1
    if ball.bottom >= height:
        if ball.bottom >= height:
            print(f"Final Score: {hit_count}")
            exit()

        color = utilities.randomizeColor()
        ball_speed[1] = -ball_speed[1]
        angle_check = True
        sidehit_count += 1

    if height - ball.bottom <= hitpad.top and hitpad.left <= ball.left <= hitpad.right:
        ball_speed[1] = -ball_speed[1]
        utilities.speedAcc(ball_speed, 0.5)
        hit_count += 1

    print(f"left {ball.left}  {hitpad.left}")

    # To destroy ball when it goes opponents side
    if count % 2 != 0:
        x1, y1 = ball.center
    elif count % 2 == 0:
        x2, y2 = ball.center
        print(x1, y1, x2, y2)
        degree = utilities.slopeAngle(x1, y1, x2, y2)
        print(degree)

        angle_check = False

    if ball.centery <= 0:
        print(degree, ball_speed, color)
        asyncio.run(client.client(ball.centerx, degree, ball_speed, color))
        exit()

    degree_surface = font.render(f"Degree: {degree}", True, red)
    hit_surface = font.render(f"Hit: {hit_count}", True, red)

    screen.blit(degree_surface, (800, 500))
    screen.blit(hit_surface, (800, 525))

    count += 1
    pg.display.flip()
    pg.time.Clock().tick(144)

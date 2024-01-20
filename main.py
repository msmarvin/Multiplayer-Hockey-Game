import time
import random
import pygame as pg


width, height = 1000, 600

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

# Window init
screen = pg.display.set_mode((width, height))

# Caption Set
pg.display.set_caption("Batu Game V1")

ball = pg.draw.circle(
    surface=screen, color=red, center=[100, 100], radius=40
)

speed = [1, 1]
color = red


def randomize():
    return random.randrange(256), random.randrange(256), random.randrange(256)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()

    ball = ball.move(speed)
    screen.fill(black)
    pg.draw.circle(
        surface=screen, color=color, center=ball.center, radius=40
    )

    if ball.left <= 0 or ball.right >= width:
        color = randomize()
        speed[0] = -speed[0]

    if ball.bottom <= 5 or ball.top >= height:
        color = randomize()
        speed[1] = -speed[1]

    time.sleep(0.001)
    pg.display.flip()

pg.quit()



import os
import sys, pygame
from pygame.locals import *
import time

pygame.init()

X = 450
Y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
size = width, height = 1200, 700
speed = [1.5,1.5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ball = pygame.transform.scale(ball, (125,125))
ballrect = ball.get_rect()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
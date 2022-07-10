import pygame
import random
import sys


pygame.init()
scr = pygame.display.set_mode((700,650))
a1 = random.randint(0,255)
a2 = random.randint(0,255)
a3 = random.randint(0,255)
clock = pygame.time.Clock()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    if 0 < a1 < 255:
        a1 += 1
    elif a1 >= 255:
        a1 -= 255
    elif a1 <= 0:
        a1 += 3
    clock.tick(60)
    scr.fill((a1,a2,a3))
    pygame.display.update()
import sys, pygame
from pygame import *

pygame.init()

size = width, height = 640, 480
speed: list[int, int] = [1, 3]
black: tuple[int, int, int] = 0, 0, 0
target = x, y = 30, 50

screen: Surface = pygame.display.set_mode(size)

ball: Surface = pygame.image.load("intro_ball.gif")
ballrect : Rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)

    pygame.display.flip()
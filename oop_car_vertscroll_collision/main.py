import pygame, sys
from pygame.locals import *
from pygame.sprite import Group, Sprite
from pygame import Clock
from Enemy import Enemy
from Player import Player
import colors
import const
import time


pygame.init()
FramePerSec: Clock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
DISPLAYSURF.fill(colors.WHITE)
pygame.display.set_caption("Game")


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
print(enemies)

all_sprites: Group = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            const.SPEED += 2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(colors.WHITE)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(colors.RED)
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(const.FPS)

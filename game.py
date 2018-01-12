import sys
import pygame
from pygame.locals import *

size = width, height = 800, 600
black = (0, 0, 0)
lastTickTime = 0
fps = 30

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

background_img = pygame.image.load("assets/background.png").convert()
background_img.set_colorkey(black)
background_rect = background_img.get_rect()
player_img = pygame.image.load("assets/player.png").convert()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (40, 40))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.ms = 150
        self.hp = 100

    def update(self, delta):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_w]:
            self.rect.centery -= self.ms * delta
        if keystate[pygame.K_s]:
            self.rect.centery += self.ms * delta
        if keystate[pygame.K_a]:
            self.rect.centerx -= self.ms * delta
        if keystate[pygame.K_d]:
            self.rect.centerx += self.ms * delta


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    clock.tick(fps)
    time = pygame.time.get_ticks()
    deltaTime = (time - lastTickTime) / 1000.0
    lastTickTime = time

    # all_sprites.update()
    player.update(delta=deltaTime)

    screen.fill(black)
    screen.blit(background_img, background_rect)

    all_sprites.draw(screen)

    pygame.display.flip()
    pygame.event.pump()

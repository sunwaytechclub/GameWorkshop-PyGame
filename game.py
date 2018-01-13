import math
import pygame
from pygame.locals import *
import random
import sys

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

bullet_sprite_sheet = pygame.image.load("assets/bullet.png")
bullet_img_list = []
for x in range(0, 16):
    for y in range(2, 4):
        bullet_img_list.append(bullet_sprite_sheet.subsurface(x * 16, y * 16, 16, 16))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (40, 40))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.ms = 200
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


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, targetx, targety):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img_list[random.randrange(0, len(bullet_img_list))]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 4
        self.rect.centerx = x
        self.rect.centery = y
        self.ms = 400
        self.originx = x
        self.originy = y
        self.targetx = targetx
        self.targety = targety
        self.distTravelled = 0
        self.alive = True

    def update(self, delta):
        self.distTravelled += self.ms * delta
        if self.distTravelled > 500:
            self.alive = False
            return

        try:
            self.rect.centerx -= (self.dx() / self.dist() * self.ms) * delta
            self.rect.centery -= (self.dy() / self.dist() * self.ms) * delta
        except:
            self.alive = False

    def dx(self):
        return self.originx - self.targetx

    def dy(self):
        return self.originy - self.targety

    def dist(self):
        return math.sqrt(self.dx() * self.dx() + self.dy() * self.dy())


all_sprites = pygame.sprite.Group()
player = Player()
bullet_list = []
all_sprites.add(player)

while True:
    clock.tick(fps)
    time = pygame.time.get_ticks()
    deltaTime = (time - lastTickTime) / 1000.0
    lastTickTime = time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        bullet = Bullet(player.rect.centerx, player.rect.centery, mousex, mousey)
        bullet_list.append(bullet)
        all_sprites.add(bullet)

    all_sprites.update(deltaTime)

    for bullet in bullet_list:
        if not bullet.alive:
            all_sprites.remove(bullet)
            bullet_list.remove(bullet)

    screen.fill(black)
    screen.blit(background_img, background_rect)

    all_sprites.draw(screen)

    pygame.display.flip()

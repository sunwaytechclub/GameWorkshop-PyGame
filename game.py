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

mob_sprite_sheet_list = []
for mob in range(1, 4):
    mob_sprite_sheet = pygame.image.load("assets/mob{}.png".format(mob))
    mob_img_list = []
    for x in range(0, 8):
        for y in range(0, 3):
            mob_img_list.append(mob_sprite_sheet.subsurface(x * 32, y * 51, 32, 51))
    mob_sprite_sheet_list.append(mob_img_list)


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
        self.dmg = 10

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


class Mob(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = mob_sprite_sheet_list[random.randrange(0, len(mob_sprite_sheet_list))]
        self.image = self.image_list[0]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 4
        self.rect.centerx = random.randrange(0, width)
        self.rect.centery = random.randrange(0, height)
        self.ms = 200
        self.alive = True
        self.hp = 100
        self.dmg = 10
        self.frametime = 0
        self.framecycle = 2

    def update(self, delta):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.sqrt(dx * dx + dy * dy)

        self.rect.centerx += (dx / dist * self.ms) * delta
        self.rect.centery += (dy / dist * self.ms) * delta

        self.frametime = (self.frametime + delta) % self.framecycle
        try:
            self.image = self.image_list[int(self.frametime / (self.framecycle / len(self.image_list)))]
        except:
            self.image = self.image_list[0]


player_sprite = pygame.sprite.Group()
player = Player()
player_sprite.add(player)
bullet_list = pygame.sprite.Group()
mob_list = pygame.sprite.Group()
spawn_delay = 2

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
        bullet_list.add(bullet)

    spawn_delay -= deltaTime
    if spawn_delay < 0:
        spawn_delay = 2
        mob = Mob()
        mob_list.add(mob)

    player.update(deltaTime)
    bullet_list.update(deltaTime)
    mob_list.update(deltaTime)

    for mob in mob_list:
        bullet_hit = pygame.sprite.spritecollide(mob, bullet_list, True)
        for bullet in bullet_hit:
            mob.hp -= bullet.dmg
            if mob.hp < 0:
                mob.alive = False
                break

    mob_hit = pygame.sprite.spritecollide(player, mob_list, True)
    for mob in mob_hit:
        player.hp -= mob.dmg
        print(player.hp)

    for bullet in bullet_list:
        if not bullet.alive:
            bullet_list.remove(bullet)

    for mob in mob_list:
        if not mob.alive:
            mob_list.remove(mob)

    screen.fill(black)
    screen.blit(background_img, background_rect)

    player_sprite.draw(screen)
    bullet_list.draw(screen)
    mob_list.draw(screen)

    pygame.display.flip()

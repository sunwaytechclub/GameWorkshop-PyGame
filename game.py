import math
import pygame
import random
import sys

size = width, height = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

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


def draw_text(screen, text, color, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text_surface, text_rect)


def draw_bar(screen, current_val, max_val, outline_color, fill_color, bar_width, bar_height, outline, x, y):
    fill = (current_val / max_val) * bar_width
    outline_rect = pygame.Rect(x, y, bar_width, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(screen, fill_color, fill_rect)
    pygame.draw.rect(screen, outline_color, outline_rect, outline)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (40, 40))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.ms = 250
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
        self.dmg = 5

    def update(self, delta):
        dx = self.originx - self.targetx
        dy = self.originy - self.targety
        dist = math.sqrt(dx * dx + dy * dy)
        self.distTravelled += self.ms * delta
        if self.distTravelled > 500:
            self.alive = False
            return

        try:
            self.rect.centerx -= (dx / dist * self.ms) * delta
            self.rect.centery -= (dy / dist * self.ms) * delta
        except:
            self.alive = False


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
        self.ms = 150
        self.alive = True
        self.hp = 100
        self.dmg = 10
        self.frametime = 0
        self.framecycle = 2

    def update(self, delta, x, y):
        dx = x - self.rect.centerx
        dy = y - self.rect.centery
        dist = math.sqrt(dx * dx + dy * dy)

        self.rect.centerx += (dx / dist * self.ms) * delta
        self.rect.centery += (dy / dist * self.ms) * delta

        self.frametime = (self.frametime + delta) % self.framecycle
        try:
            self.image = self.image_list[int(self.frametime / (self.framecycle / len(self.image_list)))]
        except:
            self.image = self.image_list[0]


def main_screen():
    start_game = False

    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    start_game = True

        screen.fill(black)
        screen.blit(background_img, background_rect)

        draw_text(screen, "Game Workshop", white, 100, width / 2, height / 2 - 50)
        draw_text(screen, "Press SPACE to start", white, 30, width / 2, (height / 2))
        draw_text(screen, "Press ESC to quit", white, 30, width / 2, (height / 2) + 30)

        pygame.display.flip()


def game():
    lastTickTime = 0
    fps = 30

    player_sprite = pygame.sprite.Group()
    player = Player()
    player_sprite.add(player)
    bullet_list = pygame.sprite.Group()
    mob_list = pygame.sprite.Group()
    spawn_delay = 2
    end_game = False

    while not end_game:
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

        player_sprite.update(deltaTime)
        bullet_list.update(deltaTime)
        mob_list.update(deltaTime, player.rect.centerx, player.rect.centery)

        for mob in mob_list:
            bullet_hit = pygame.sprite.spritecollide(mob, bullet_list, False)
            for bullet in bullet_hit:
                if bullet.alive:
                    bullet.alive = False
                    mob.hp -= bullet.dmg
                    if mob.hp <= 0:
                        mob.alive = False
                        break

        mob_hit = pygame.sprite.spritecollide(player, mob_list, False)
        for mob in mob_hit:
            mob.alive = False
            player.hp -= mob.dmg

        if player.hp <= 0:
            end_game = True

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

        draw_text(screen, "HP: {!s}".format(player.hp), white, 30, 40, 10)
        for mob in mob_list:
            draw_bar(screen, mob.hp, 100, white, red, mob.rect.width, 6, 1, mob.rect.left, mob.rect.top)

        pygame.display.flip()


def game_over():
    start_game = False

    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    start_game = True

        screen.fill(black)
        screen.blit(background_img, background_rect)

        draw_text(screen, "GAME OVER", red, 100, width / 2, height / 2)
        draw_text(screen, "Press SPACE to continue", red, 30, width / 2, (height / 2) + 50)
        draw_text(screen, "Press ESC to quit", red, 30, width / 2, (height / 2) + 80)

        pygame.display.flip()


while True:
    main_screen()
    game()
    game_over()

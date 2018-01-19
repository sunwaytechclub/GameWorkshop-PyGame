# GameWorkshop-PyGame

![Main Menu](screenshots/main_menu.png)

![In Game 1](screenshots/in_game_1.png)

![In Game 2](screenshots/in_game_2.png)

![In Game 3](screenshots/in_game_3.png)

![Game Over](screenshots/game_over.png)

## Tutorial

### Terminology

1. Sprite

    - A bitmap of an arbitrary shape that can be moved across complex backgrounds without flicker or damage to the background image

1. Sprite Sheet

    - A sheet with a collection of sprite

1. Texture

    - Surface of an object

1. Frame

    - A sequence of events ending in a page flip

1. FPS

    - Frame per seconds for speed of animation

1. Animation

    - A technique where successive still frames of a particular object appear to constitute a seamless sequence of movements

1. Time delta

    - Different in time comparing to last frame

1. Assets

    - Images, sound, music, texture, etc that used in a game

1. Render

    - A technique used to generate 2d or 3d model

### PyGame Tutorial

***Please make sure you had installed PyGame by using following command***

`$ python3 -m pip install pygame`

1. First of all, download the assets and create a empty folder. Directory should looks as below

    ```
    GameWorkshop\
        assets\
            background.png
            bullet.png
            mob1.png
            mob2.png
            mob3.png
            player.png
        game.py
    ```

1. Then, we need to import some of the basic library that we need

    ```
    import math # math library
    import pygame # pygame library
    import random # random library
    import sys # system library
    ```

1. Initialize some of the variable in the game

    ```
    size = width, height = 800, 600 # size of the game, change the value as you see fit, but please be aware that the background is quite small
    black = (0, 0, 0) # black color
    white = (255, 255, 255) # white color
    red = (255, 0, 0) # red color
    ```

1. Initialize a empty game screen

    ```
    pygame.init() # Initialize the game
    screen = pygame.display.set_mode(size) # Initialize a screen
    pygame.display.set_caption("Shooting Game") # Name in the title bar

    def game():
        end_game = False

        while not end_game:
            for event in pygame.event.get(): # get all the event list
                if event.type == pygame.QUIT: # if the window had receive kill signal
                    sys.exit() # close the program

            screen.fill(black) # fill the screen with black

            pygame.display.flip() # display the screen

    while True:
        game()
    ```

1. Run the game, and you should be able to see a black screen

    `$ python3 game.py`

1. Move on, let's load the assets of background and player

    ```
    background_img = pygame.image.load("assets/background.png").convert() # Get get image assets
    background_img.set_colorkey(black) # set the color key (same color key can achieve transparency)
    background_rect = background_img.get_rect()
    player_img = pygame.image.load("assets/player.png").convert()
    ```

1. Make a player class

    ```
    class Player(pygame.sprite.Sprite): # Class Player is subclass of Sprite class

        def __init__(self): # Initialize the player
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (40, 40)) # transform the image into 40 x 40
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 20
            self.rect.centerx = width / 2 # Set the x position of the player
            self.rect.centery = height / 2 # set the y position of the player
            self.ms = 250
            self.hp = 100

        def update(self, delta): # update at every frame
            keystate = pygame.key.get_pressed() # Get all the key that had been pressed

            if keystate[pygame.K_w]: # w key
                self.rect.centery -= self.ms * delta
            if keystate[pygame.K_s]: # s key
                self.rect.centery += self.ms * delta
            if keystate[pygame.K_a]: # a key
                self.rect.centerx -= self.ms * delta
            if keystate[pygame.K_d]: # d key
                self.rect.centerx += self.ms * delta
    ```

1. Initialize a clock

    ```
    clock = pygame.time.Clock()
    ```

1. Initialize game variable

    ```
    lastTickTime = 0
    fps = 30

    player_sprite = pygame.sprite.Group()
    player = Player()
    player_sprite.add(player)
    ```

1. Make the animation of the game

    ```
    clock.tick(fps)
    time = pygame.time.get_ticks()
    deltaTime = (time - lastTickTime) / 1000.0
    lastTickTime = time
    ```

    ```
    player_sprite.update(deltaTime)

    screen.fill(black)
    screen.blit(background_img, background_rect)

    player_sprite.draw(screen)

    pygame.display.flip()
    ```

1. If you cannot follow so far, this is the full snipper of the game right now

    ```
    import math # math library
    import pygame # pygame library
    import random # random library
    import sys # system library

    size = width, height = 800, 600 # size of the game, change the value as you see fit, but please be aware that the background is quite small
    black = (0, 0, 0) # black color
    white = (255, 255, 255) # white color
    red = (255, 0, 0) # red color

    pygame.init() # Initialize the game
    screen = pygame.display.set_mode(size) # Initialize a screen
    pygame.display.set_caption("Shooting Game") # Name in the title bar
    clock = pygame.time.Clock()

    background_img = pygame.image.load("assets/background.png").convert() # Get get image assets
    background_img.set_colorkey(black) # set the color key (same color key can achieve transparency)
    background_rect = background_img.get_rect()
    player_img = pygame.image.load("assets/player.png").convert()

    class Player(pygame.sprite.Sprite): # Class Player is subclass of Sprite class

        def __init__(self): # Initialize the player
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (40, 40)) # transform the image into 40 x 40
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 20
            self.rect.centerx = width / 2 # Set the x position of the player
            self.rect.centery = height / 2 # set the y position of the player
            self.ms = 250
            self.hp = 100

        def update(self, delta): # update at every frame
            keystate = pygame.key.get_pressed() # Get all the key that had been pressed

            if keystate[pygame.K_w]: # w key
                self.rect.centery -= self.ms * delta
            if keystate[pygame.K_s]: # s key
                self.rect.centery += self.ms * delta
            if keystate[pygame.K_a]: # a key
                self.rect.centerx -= self.ms * delta
            if keystate[pygame.K_d]: # d key
                self.rect.centerx += self.ms * delta

    def game():
        lastTickTime = 0
        fps = 30

        player_sprite = pygame.sprite.Group()
        player = Player()
        player_sprite.add(player)

        end_game = False

        while not end_game:
            clock.tick(fps)
            time = pygame.time.get_ticks()
            deltaTime = (time - lastTickTime) / 1000.0
            lastTickTime = time

            for event in pygame.event.get(): # get all the event list
                if event.type == pygame.QUIT: # if the window had receive kill signal
                    sys.exit() # close the program

            player_sprite.update(deltaTime)

            screen.fill(black)
            screen.blit(background_img, background_rect)

            player_sprite.draw(screen)

            pygame.display.flip()

    while True:
        game()
    ```

1. Run again now and you should be able to see a space background and a space ship. Try control it using w, a, s, d

    `$ python3 game.py`

1. Now, let's load some bullet

    ```
    bullet_sprite_sheet = pygame.image.load("assets/bullet.png") # load the spirte sheet
    bullet_img_list = [] # store each sprite into the list
    for x in range(0, 16): # row 0 to row 15
        for y in range(2, 4): # column 2 to column 3
            bullet_img_list.append(bullet_sprite_sheet.subsurface(x * 16, y * 16, 16, 16)) # (x position in pixels, y position in pixels, width, height)
    ```

1. Create a bullet class

    ```
    class Bullet(pygame.sprite.Sprite):

        def __init__(self, x, y, targetx, targety):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img_list[random.randrange(0, len(bullet_img_list))] # random a bullet within the list
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 4
            self.rect.centerx = x
            self.rect.centery = y
            self.ms = 400
            self.originx = x # x position where the bullet start
            self.originy = y # y posiiton where the bullet start
            self.targetx = targetx # mouse position when the bullet had been shoot
            self.targety = targety # mouse position when the bullet had been shoot
            self.distTravelled = 0
            self.alive = True
            self.dmg = 5

        def update(self, delta):
            dx = self.originx - self.targetx
            dy = self.originy - self.targety
            dist = math.sqrt(dx * dx + dy * dy)
            self.distTravelled += self.ms * delta
            if self.distTravelled > 500: # when the distance traveled more than 500 will be killed
                self.alive = False
                return

            try:
                self.rect.centerx -= (dx / dist * self.ms) * delta
                self.rect.centery -= (dy / dist * self.ms) * delta
            except:
                self.alive = False # this happen when the origin are same with target, so the bullet will never move
    ```

1. Shoot the bullet when space is pressed

    ```
    # add under the game variable
    bullet_list = pygame.sprite.Group()
    ```

    ```
    # within the loop
    mousex, mousey = pygame.mouse.get_pos() # get x and y position of mouse
    key = pygame.key.get_pressed() # get all the key pressed
    if key[pygame.K_SPACE]:
        bullet = Bullet(player.rect.centerx, player.rect.centery, mousex, mousey) # when space is pressed, new bullet is created
        bullet_list.add(bullet) # and add into the bullet list
    ```

    ```
    # under update player sprite
    bullet_list.update(deltaTime)

    for bullet in bullet_list: # check if the bullet is not alive, it will be removed
        if not bullet.alive:
            bullet_list.remove(bullet)
    ```

    ```
    # under draw player sprite
    bullet_list.draw(screen)
    ```

1. Run the game again, and you will be able to see the bullet fly all around the places

    `$ python3 game.py`

1. Load mob sprite assets

    ```
    mob_sprite_sheet_list = []
    for mob in range(1, 4): # total of 3 sprite sheet representing 3 different mob
        mob_sprite_sheet = pygame.image.load("assets/mob{}.png".format(mob)) # name are named as mob<num:Int>.png
        mob_img_list = [] # the image list within the sprite sheet
        for x in range(0, 8):
            for y in range(0, 3):
                mob_img_list.append(mob_sprite_sheet.subsurface(x * 32, y * 51, 32, 51))
        mob_sprite_sheet_list.append(mob_img_list) # all different kind of mob made up of different list
    ```

1. Create a mob class

    ```
    class Mob(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_list = mob_sprite_sheet_list[random.randrange(0, len(mob_sprite_sheet_list))] # random choose list of animation image from 3 types of mob
            self.image = self.image_list[0] # get the first frame
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 4
            self.rect.centerx = random.randrange(0, width) # random the starting x position
            self.rect.centery = random.randrange(0, height) # random the starting y position
            self.ms = 150
            self.alive = True
            self.hp = 100
            self.dmg = 10
            self.frametime = 0 # track the time
            self.framecycle = 2 # total time of a animation cycle

        def update(self, delta, x, y):
            dx = x - self.rect.centerx
            dy = y - self.rect.centery
            dist = math.sqrt(dx * dx + dy * dy)

            self.rect.centerx += (dx / dist * self.ms) * delta
            self.rect.centery += (dy / dist * self.ms) * delta

            self.frametime = (self.frametime + delta) % self.framecycle # since animation time cycle is 2 second, we only need to track up to 2 seconds
            try:
                self.image = self.image_list[int(self.frametime / (self.framecycle / len(self.image_list)))]
            except:
                self.image = self.image_list[0] # in case when array out of bound
    ```

1. Implement mob

    ```
    # under game variable
    mob_list = pygame.sprite.Group()
    spawn_delay = 2
    ```

    ```
    # within the main loop
    # under the check space pressed and shoot bullet

    spawn_delay -= deltaTime # when spawn delay less than 2, spawn mob and reset spawn delay
    if spawn_delay < 0:
        spawn_delay = 2
        mob = Mob()
        mob_list.add(mob)
    ```

    ```
    # update mob
    mob_list.update(deltaTime, player.rect.centerx, player.rect.centery)
    ```

    ```
    # under draw sprites
    mob_list.draw(screen)
    ```

1. Collision detection for bullet with mob and player

    ```
    for mob in mob_list:
        bullet_hit = pygame.sprite.spritecollide(mob, bullet_list, False) # check when mob collied with bullet, and when collied do not remove bullet from the list
        for bullet in bullet_hit:
            if bullet.alive:
                bullet.alive = False
                mob.hp -= bullet.dmg
                if mob.hp <= 0:
                    mob.alive = False
                    break

    mob_hit = pygame.sprite.spritecollide(player, mob_list, False) # check if player hit the mob, and if hit it will not removed from the mob_list
    for mob in mob_hit:
        mob.alive = False
        player.hp -= mob.dmg
    ```

    ```
    for mob in mob_list: # remove mob when mob is dead
        if not mob.alive:
            mob_list.remove(mob)
    ```

1. If you are lost, the code so far is as below

    ```
    import math # math library
    import pygame # pygame library
    import random # random library
    import sys # system library

    size = width, height = 800, 600 # size of the game, change the value as you see fit, but please be aware that the background is quite small
    black = (0, 0, 0) # black color
    white = (255, 255, 255) # white color
    red = (255, 0, 0) # red color

    pygame.init() # Initialize the game
    screen = pygame.display.set_mode(size) # Initialize a screen
    pygame.display.set_caption("Shooting Game") # Name in the title bar
    clock = pygame.time.Clock()

    background_img = pygame.image.load("assets/background.png").convert() # Get get image assets
    background_img.set_colorkey(black) # set the color key (same color key can achieve transparency)
    background_rect = background_img.get_rect()
    player_img = pygame.image.load("assets/player.png").convert()

    bullet_sprite_sheet = pygame.image.load("assets/bullet.png") # load the spirte sheet
    bullet_img_list = [] # store each sprite into the list
    for x in range(0, 16): # row 0 to row 15
        for y in range(2, 4): # column 2 to column 3
            bullet_img_list.append(bullet_sprite_sheet.subsurface(x * 16, y * 16, 16, 16)) # (x position in pixels, y position in pixels, width, height)

    mob_sprite_sheet_list = []
    for mob in range(1, 4): # total of 3 sprite sheet representing 3 different mob
        mob_sprite_sheet = pygame.image.load("assets/mob{}.png".format(mob)) # name are named as mob<num:Int>.png
        mob_img_list = [] # the image list within the sprite sheet
        for x in range(0, 8):
            for y in range(0, 3):
                mob_img_list.append(mob_sprite_sheet.subsurface(x * 32, y * 51, 32, 51))
        mob_sprite_sheet_list.append(mob_img_list) # all different kind of mob made up of different list


    class Player(pygame.sprite.Sprite): # Class Player is subclass of Sprite class

        def __init__(self): # Initialize the player
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (40, 40)) # transform the image into 40 x 40
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 20
            self.rect.centerx = width / 2 # Set the x position of the player
            self.rect.centery = height / 2 # set the y position of the player
            self.ms = 250
            self.hp = 100

        def update(self, delta): # update at every frame
            keystate = pygame.key.get_pressed() # Get all the key that had been pressed

            if keystate[pygame.K_w]: # w key
                self.rect.centery -= self.ms * delta
            if keystate[pygame.K_s]: # s key
                self.rect.centery += self.ms * delta
            if keystate[pygame.K_a]: # a key
                self.rect.centerx -= self.ms * delta
            if keystate[pygame.K_d]: # d key
                self.rect.centerx += self.ms * delta


    class Bullet(pygame.sprite.Sprite):

        def __init__(self, x, y, targetx, targety):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img_list[random.randrange(0, len(bullet_img_list))] # random a bullet within the list
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 4
            self.rect.centerx = x
            self.rect.centery = y
            self.ms = 400
            self.originx = x # x position where the bullet start
            self.originy = y # y posiiton where the bullet start
            self.targetx = targetx # mouse position when the bullet had been shoot
            self.targety = targety # mouse position when the bullet had been shoot
            self.distTravelled = 0
            self.alive = True
            self.dmg = 5

        def update(self, delta):
            dx = self.originx - self.targetx
            dy = self.originy - self.targety
            dist = math.sqrt(dx * dx + dy * dy)
            self.distTravelled += self.ms * delta
            if self.distTravelled > 500: # when the distance traveled more than 500 will be killed
                self.alive = False
                return

            try:
                self.rect.centerx -= (dx / dist * self.ms) * delta
                self.rect.centery -= (dy / dist * self.ms) * delta
            except:
                self.alive = False # this happen when the origin are same with target, so the bullet will never move


    class Mob(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_list = mob_sprite_sheet_list[random.randrange(0, len(mob_sprite_sheet_list))] # random choose list of animation image from 3 types of mob
            self.image = self.image_list[0] # get the first frame
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 4
            self.rect.centerx = random.randrange(0, width) # random the starting x position
            self.rect.centery = random.randrange(0, height) # random the starting y position
            self.ms = 150
            self.alive = True
            self.hp = 100
            self.dmg = 10
            self.frametime = 0 # track the time
            self.framecycle = 2 # total time of a animation cycle

        def update(self, delta, x, y):
            dx = x - self.rect.centerx
            dy = y - self.rect.centery
            dist = math.sqrt(dx * dx + dy * dy)

            self.rect.centerx += (dx / dist * self.ms) * delta
            self.rect.centery += (dy / dist * self.ms) * delta

            self.frametime = (self.frametime + delta) % self.framecycle # since animation time cycle is 2 second, we only need to track up to 2 seconds
            try:
                self.image = self.image_list[int(self.frametime / (self.framecycle / len(self.image_list)))]
            except:
                self.image = self.image_list[0] # in case when array out of bound

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

            for event in pygame.event.get(): # get all the event list
                if event.type == pygame.QUIT: # if the window had receive kill signal
                    sys.exit() # close the program

            mousex, mousey = pygame.mouse.get_pos() # get x and y position of mouse
            key = pygame.key.get_pressed() # get all the key pressed
            if key[pygame.K_SPACE]:
                bullet = Bullet(player.rect.centerx, player.rect.centery, mousex, mousey) # when space is pressed, new bullet is created
                bullet_list.add(bullet) # and add into the bullet list

            spawn_delay -= deltaTime # when spawn delay less than 2, spawn mob and reset spawn delay
            if spawn_delay < 0:
                spawn_delay = 2
                mob = Mob()
                mob_list.add(mob)

            player_sprite.update(deltaTime)
            bullet_list.update(deltaTime)
            mob_list.update(deltaTime, player.rect.centerx, player.rect.centery)

            for mob in mob_list:
                bullet_hit = pygame.sprite.spritecollide(mob, bullet_list, False) # check when mob collied with bullet, and when collied do not remove bullet from the list
                for bullet in bullet_hit:
                    if bullet.alive:
                        bullet.alive = False
                        mob.hp -= bullet.dmg
                        if mob.hp <= 0:
                            mob.alive = False
                            break

            mob_hit = pygame.sprite.spritecollide(player, mob_list, False) # check if player hit the mob, and if hit it will not removed from the mob_list
            for mob in mob_hit:
                mob.alive = False
                player.hp -= mob.dmg

            for bullet in bullet_list: # check if the bullet is not alive, it will be removed
                if not bullet.alive:
                    bullet_list.remove(bullet)

            for mob in mob_list: # remove mob when mob is dead
                if not mob.alive:
                    mob_list.remove(mob)

            screen.fill(black)
            screen.blit(background_img, background_rect)

            player_sprite.draw(screen)
            bullet_list.draw(screen)
            mob_list.draw(screen)

            pygame.display.flip()

    while True:
        game()
    ```

1. Now start the game again and play the game

    `$ python3 game.py`

1. We need to display our own hp and enemy hp, so we need to draw text and hp bar

    ```
    font_name = pygame.font.match_font('arial') # Initialize font
    ```

    ```
    def draw_text(screen, text, color, size, x, y):
        font = pygame.font.Font(font_name, size) # get the font template
        text_surface = font.render(text, True, color) # use font template to render a text
        text_rect = text_surface.get_rect() # get the rect representing of the text
        text_rect.centerx = x
        text_rect.centery = y
        screen.blit(text_surface, text_rect) # render it onto the screen


    def draw_bar(screen, current_val, max_val, outline_color, fill_color, bar_width, bar_height, outline, x, y):
        fill = (current_val / max_val) * bar_width # The width of the inner side of the bar
        outline_rect = pygame.Rect(x, y, bar_width, bar_height) # generate the outer part of the bar
        fill_rect = pygame.Rect(x, y, fill, bar_height) # generate the inner part of the bar
        pygame.draw.rect(screen, fill_color, fill_rect) # draw the filling bar (the inner one)
        pygame.draw.rect(screen, outline_color, outline_rect, outline) # draw the outer square, outline is the width of the outer square
    ```

1. Let use it in showing the hp and also the mob hp

    ```
    draw_text(screen, "HP: {!s}".format(player.hp), white, 30, 40, 10)
    for mob in mob_list:
        # (screen, mob current hp, mob max hp, color of outer square, color of fill, bar width, bar height, outline width, x position, y position)
        draw_bar(screen, mob.hp, 100, white, red, mob.rect.width, 6, 1, mob.rect.left, mob.rect.top)
    ```

1. Create a game over screen

    ```
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
    ```

1. Might as well create main game screen

    ```
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
    ```

1. Check player dead

    ```
    # under game collision detection
    if player.hp <= 0:
        end_game = True # end the loop
    ```

1. Add them into game loop

    ```
    # go to the most bottom and add this
    while True:
        main_screen()
        game()
        game_over()
    ```

1. If you cannot follow, heres the whole code

    ```
    import math # math library
    import pygame # pygame library
    import random # random library
    import sys # system library

    size = width, height = 800, 600 # size of the game, change the value as you see fit, but please be aware that the background is quite small
    black = (0, 0, 0) # black color
    white = (255, 255, 255) # white color
    red = (255, 0, 0) # red color

    pygame.init() # Initialize the game
    screen = pygame.display.set_mode(size) # Initialize a screen
    pygame.display.set_caption("Shooting Game") # Name in the title bar
    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('arial') # Initialize font

    background_img = pygame.image.load("assets/background.png").convert() # Get get image assets
    background_img.set_colorkey(black) # set the color key (same color key can achieve transparency)
    background_rect = background_img.get_rect()
    player_img = pygame.image.load("assets/player.png").convert()

    bullet_sprite_sheet = pygame.image.load("assets/bullet.png") # load the spirte sheet
    bullet_img_list = [] # store each sprite into the list
    for x in range(0, 16): # row 0 to row 15
        for y in range(2, 4): # column 2 to column 3
            bullet_img_list.append(bullet_sprite_sheet.subsurface(x * 16, y * 16, 16, 16)) # (x position in pixels, y position in pixels, width, height)

    mob_sprite_sheet_list = []
    for mob in range(1, 4): # total of 3 sprite sheet representing 3 different mob
        mob_sprite_sheet = pygame.image.load("assets/mob{}.png".format(mob)) # name are named as mob<num:Int>.png
        mob_img_list = [] # the image list within the sprite sheet
        for x in range(0, 8):
            for y in range(0, 3):
                mob_img_list.append(mob_sprite_sheet.subsurface(x * 32, y * 51, 32, 51))
        mob_sprite_sheet_list.append(mob_img_list) # all different kind of mob made up of different list


    def draw_text(screen, text, color, size, x, y):
        font = pygame.font.Font(font_name, size) # get the font template
        text_surface = font.render(text, True, color) # use font template to render a text
        text_rect = text_surface.get_rect() # get the rect representing of the text
        text_rect.centerx = x
        text_rect.centery = y
        screen.blit(text_surface, text_rect) # render it onto the screen


    def draw_bar(screen, current_val, max_val, outline_color, fill_color, bar_width, bar_height, outline, x, y):
        fill = (current_val / max_val) * bar_width # The width of the inner side of the bar
        outline_rect = pygame.Rect(x, y, bar_width, bar_height) # generate the outer part of the bar
        fill_rect = pygame.Rect(x, y, fill, bar_height) # generate the inner part of the bar
        pygame.draw.rect(screen, fill_color, fill_rect) # draw the filling bar (the inner one)
        pygame.draw.rect(screen, outline_color, outline_rect, outline) # draw the outer square, outline is the width of the outer square


    class Player(pygame.sprite.Sprite): # Class Player is subclass of Sprite class

        def __init__(self): # Initialize the player
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (40, 40)) # transform the image into 40 x 40
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 20
            self.rect.centerx = width / 2 # Set the x position of the player
            self.rect.centery = height / 2 # set the y position of the player
            self.ms = 250
            self.hp = 100

        def update(self, delta): # update at every frame
            keystate = pygame.key.get_pressed() # Get all the key that had been pressed

            if keystate[pygame.K_w]: # w key
                self.rect.centery -= self.ms * delta
            if keystate[pygame.K_s]: # s key
                self.rect.centery += self.ms * delta
            if keystate[pygame.K_a]: # a key
                self.rect.centerx -= self.ms * delta
            if keystate[pygame.K_d]: # d key
                self.rect.centerx += self.ms * delta


    class Bullet(pygame.sprite.Sprite):

        def __init__(self, x, y, targetx, targety):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img_list[random.randrange(0, len(bullet_img_list))] # random a bullet within the list
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 4
            self.rect.centerx = x
            self.rect.centery = y
            self.ms = 400
            self.originx = x # x position where the bullet start
            self.originy = y # y posiiton where the bullet start
            self.targetx = targetx # mouse position when the bullet had been shoot
            self.targety = targety # mouse position when the bullet had been shoot
            self.distTravelled = 0
            self.alive = True
            self.dmg = 5

        def update(self, delta):
            dx = self.originx - self.targetx
            dy = self.originy - self.targety
            dist = math.sqrt(dx * dx + dy * dy)
            self.distTravelled += self.ms * delta
            if self.distTravelled > 500: # when the distance traveled more than 500 will be killed
                self.alive = False
                return

            try:
                self.rect.centerx -= (dx / dist * self.ms) * delta
                self.rect.centery -= (dy / dist * self.ms) * delta
            except:
                self.alive = False # this happen when the origin are same with target, so the bullet will never move


    class Mob(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_list = mob_sprite_sheet_list[random.randrange(0, len(mob_sprite_sheet_list))] # random choose list of animation image from 3 types of mob
            self.image = self.image_list[0] # get the first frame
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.radius = 4
            self.rect.centerx = random.randrange(0, width) # random the starting x position
            self.rect.centery = random.randrange(0, height) # random the starting y position
            self.ms = 150
            self.alive = True
            self.hp = 100
            self.dmg = 10
            self.frametime = 0 # track the time
            self.framecycle = 2 # total time of a animation cycle

        def update(self, delta, x, y):
            dx = x - self.rect.centerx
            dy = y - self.rect.centery
            dist = math.sqrt(dx * dx + dy * dy)

            self.rect.centerx += (dx / dist * self.ms) * delta
            self.rect.centery += (dy / dist * self.ms) * delta

            self.frametime = (self.frametime + delta) % self.framecycle # since animation time cycle is 2 second, we only need to track up to 2 seconds
            try:
                self.image = self.image_list[int(self.frametime / (self.framecycle / len(self.image_list)))]
            except:
                self.image = self.image_list[0] # in case when array out of bound


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

            for event in pygame.event.get(): # get all the event list
                if event.type == pygame.QUIT: # if the window had receive kill signal
                    sys.exit() # close the program

            mousex, mousey = pygame.mouse.get_pos() # get x and y position of mouse
            key = pygame.key.get_pressed() # get all the key pressed
            if key[pygame.K_SPACE]:
                bullet = Bullet(player.rect.centerx, player.rect.centery, mousex, mousey) # when space is pressed, new bullet is created
                bullet_list.add(bullet) # and add into the bullet list

            spawn_delay -= deltaTime # when spawn delay less than 2, spawn mob and reset spawn delay
            if spawn_delay < 0:
                spawn_delay = 2
                mob = Mob()
                mob_list.add(mob)

            player_sprite.update(deltaTime)
            bullet_list.update(deltaTime)
            mob_list.update(deltaTime, player.rect.centerx, player.rect.centery)

            for mob in mob_list:
                bullet_hit = pygame.sprite.spritecollide(mob, bullet_list, False) # check when mob collied with bullet, and when collied do not remove bullet from the list
                for bullet in bullet_hit:
                    if bullet.alive:
                        bullet.alive = False
                        mob.hp -= bullet.dmg
                        if mob.hp <= 0:
                            mob.alive = False
                            break

            mob_hit = pygame.sprite.spritecollide(player, mob_list, False) # check if player hit the mob, and if hit it will not removed from the mob_list
            for mob in mob_hit:
                mob.alive = False
                player.hp -= mob.dmg

            # under game collision detection
            if player.hp <= 0:
                end_game = True # end the loop

            for bullet in bullet_list: # check if the bullet is not alive, it will be removed
                if not bullet.alive:
                    bullet_list.remove(bullet)

            for mob in mob_list: # remove mob when mob is dead
                if not mob.alive:
                    mob_list.remove(mob)

            screen.fill(black)
            screen.blit(background_img, background_rect)

            player_sprite.draw(screen)
            bullet_list.draw(screen)
            mob_list.draw(screen)

            draw_text(screen, "HP: {!s}".format(player.hp), white, 30, 40, 10)
            for mob in mob_list:
                # (screen, mob current hp, mob max hp, color of outer square, color of fill, bar width, bar height, outline width, x position, y position)
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
    ```

1. You had completed your first game, enjoy

    `$ python3 game.py`

## Sunway Tech Club

We are now recruiting new committee members! If you are interested, do approach any of the Sunway Tech Club committee!

Also, do checkout on us!

[Our Facebook Page](https://www.facebook.com/sunwaytechclub/)

[Our Website](https://joinstc.stamplayapp.com/)

[Our Slack Channel](https://sunwaytechclub.slack.com/)

Our Email: <sunwaytechclub@gmail.com>

"""
Made from the following YouTube playlist by "KidsCanCode":
https://www.youtube.com/watch?v=uWvb3QzA48c&list=PLsk-HSGFjnaG-BwZkuAOcVwWldfCLu1pq
"""

# Jumpy! - Platform game
import pygame as pg
import random
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # Initialize game window, etc
        # Initialize pygame and create window
        pg.init()

        # For sound
        pg.mixer.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        # Keeps track of how fast we are running
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # Load high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        # Load spritesheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
            


    def new(self):
        # Start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        
        for plat in PLATFORM_LIST:
            p = Platform(self, *plat) # * stands for 'explode'
            self.all_sprites.add(p)
            self.platforms.add(p)
        
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
        self.run()


    def run(self):
        # Game Loop
        self.playing = True

        while self.playing:
            # keep loop running at the right speed
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # Check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            # False, since we do not want to delete the platform we hit

            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # If player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT//4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)

                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)

                if sprite.rect.bottom < 0:
                    sprite.kill()

        if len(self.platforms) == 0:
            self.playing = False


        # Spawn new platforms to keep same average number
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(self, random.randrange(0, WIDTH-width),
                random.randrange(-75, -30))
        
            self.platforms.add(p)
            self.all_sprites.add(p)


    def events(self):
        # Game Loop - events
        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()


    def draw(self):
        # Game Loop - draw
        # Draw / render
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 22, WHITE, WIDTH//2, 15)
        
        # *after* drawing everything, flip the display
        pg.display.flip()


    def show_start_screen(self):
        # Game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH//2, HEIGHT//4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH//2, HEIGHT//2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH//2, HEIGHT*3/4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH/2, 15)
        pg.display.flip()
        self.wait_for_key()


    def show_go_screen(self):
        # Game over/continue
        if not self.running:
            return
            
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH//2, HEIGHT//4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH//2, HEIGHT//2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH//2, HEIGHT*3/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH//2, HEIGHT//2 + 40)

            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))

        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH/2, HEIGHT//2 + 40)


        pg.display.flip()
        self.wait_for_key()


    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                    
                if event.type == pg.KEYUP:
                    waiting = False

            


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)



g = Game()

g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()


pg.quit()

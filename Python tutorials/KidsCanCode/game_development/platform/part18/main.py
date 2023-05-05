"""
Made from the following YouTube playlist by "KidsCanCode":
https://www.youtube.com/watch?v=uWvb3QzA48c&list=PLsk-HSGFjnaG-BwZkuAOcVwWldfCLu1pq

Art from Kenney.nl
Happy Tune and Melancholy Piano by https://opengameart.org/users/syncopika
Yippee by https://opengameart.org/users/snabisch
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

        # Cloud images
        self.cloud_images = []
        for i in range(1, 3+1):
            self.cloud_images.append(pg.image.load(path.join(img_dir, f'cloud{i}.png')).convert())

        # Load sound
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump33.wav'))
        self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Boost16.wav'))

        # Reduce volume
        self.jump_sound.set_volume(SFX_VOL)        
        self.boost_sound.set_volume(SFX_VOL)        


    def new(self):
        # Start a new game
        self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        self.player = Player(self)
        
        for plat in PLATFORM_LIST:
            Platform(self, *plat) # * stands for 'explode'
        
        self.mob_timer = 0
        pg.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
        pg.mixer.music.set_volume(MUSIC_VOL)

        # Spawn some clouds to begin with
        for i in range(8):
            c = Cloud(self)
            c.rect.y += 500

        self.run()


    def run(self):
        # Game Loop

        # The music loops indefinitely
        pg.mixer.music.play(loops=-1)
        self.playing = True

        while self.playing:
            # keep loop running at the right speed
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        # Let the music fade out over a period of 500 ms
        pg.mixer.music.fadeout(500)


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

        # Spawn a mob?
        now = pg.time.get_ticks()
        if now - self.mob_timer > MOB_FREQ + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Mob(self)

        # Hit mobs?
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False, pg.sprite.collide_mask)
        # Mask collision can give performance issues
        # If that is the case, use rectangle collision to narrow it down

        if mob_hits:
            self.playing = False


        # Check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            # False, since we do not want to delete the platform we hit

            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                
                if self.player.pos.x < lowest.rect.right +10 and self.player.pos.x > lowest.rect.left - 10:

                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

        # If player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT//4:
            # Spawn a cloud
            if random.randrange(100) < 15:
                Cloud(self)

            self.player.pos.y += max(abs(self.player.vel.y), 2)

            for cloud in self.clouds:
                # Moves by at half the speed
                cloud.rect.y += max(abs(self.player.vel.y/2), 2)
            
            for mob in self.mobs:
                mob.rect.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)

                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # if player hits powerup
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.boost_sound.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False

                
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
            Platform(self, random.randrange(0, WIDTH-width),
                random.randrange(-75, -30))
        

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
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()


    def draw(self):
        # Game Loop - draw
        # Draw / render
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH//2, 15)
        
        # *after* drawing everything, flip the display
        pg.display.flip()


    def show_start_screen(self):
        # Game splash/start screen
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.set_volume(MUSIC_VOL)
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH//2, HEIGHT//4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH//2, HEIGHT//2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH//2, HEIGHT*3/4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH/2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)


    def show_go_screen(self):
        # Game over/continue
        if not self.running:
            return
        
        #pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.load(path.join(self.snd_dir, 'Melancholy Piano.ogg'))
        pg.mixer.music.set_volume(MUSIC_VOL)
        pg.mixer.music.play(loops=-1)

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
        pg.mixer.music.fadeout(500)


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

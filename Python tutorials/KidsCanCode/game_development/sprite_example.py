"""
Made from the following YouTube playlist by "KidsCanCode":
https://www.youtube.com/watch?v=VO8rTszcW4s&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=1
"""

# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

# Constants
WIDTH = 800
HEIGHT = 600

# Frames per second
FPS = 30

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        
        """
        Sprites by Kenney.nl
        https://opengameart.org/content/platformer-art-complete-pack-often-updated
        """
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        
        # Make black transparent
        self.image.set_colorkey(BLACK)
        
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        
        self.y_speed = 5
        
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
            
        if self.rect.top < 200:
            self.y_speed = 5
        
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Initialize pygame and create window
pygame.init()

# For sound
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Keeps track of how fast we are running
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        
    
    # Update
    all_sprites.update()
        
    
    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()


pygame.quit()




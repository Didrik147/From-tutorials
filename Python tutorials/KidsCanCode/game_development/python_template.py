"""
Made from the following YouTube playlist by "KidsCanCode":
https://www.youtube.com/watch?v=VO8rTszcW4s&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=1
"""

# Pygame template - skeleton for a new pygame project
import pygame
import random

# Constants
WIDTH = 360
HEIGHT = 480

# Frames per second
FPS = 30

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame and create window
pygame.init()

# For sound
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Keeps track of how fast we are running
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

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
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()


pygame.quit()



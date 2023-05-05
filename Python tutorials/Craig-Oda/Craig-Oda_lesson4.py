# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()


# Frames per second
FPS = 30
clock = pygame.time.Clock()

size = (480, 320)
screen = pygame.display.set_mode(size)

#RGB
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#left edge of rectangle, top, width, height
player_rect = pygame.Rect(0, 0, 64, 64)

up_rect = pygame.Rect(300, 100, 50, 50)
down_rect = pygame.Rect(300, 180, 50, 50)

direction = "down"

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if up_rect.collidepoint(mouse_pos):
				direction = "up"
			if down_rect.collidepoint(mouse_pos):
				direction = "down"
			
	if direction == "down":
		player_rect.centery += 3
	elif direction == "up":
		player_rect.centery -= 3
   
	if player_rect.bottom > size[1]:
		direction = "up"
	if player_rect.top < 0:
		direction = "down"
      
	screen.fill(BLACK)
	pygame.draw.rect(screen, RED, player_rect)
   
	pygame.draw.rect(screen, GREEN, up_rect)
	pygame.draw.rect(screen, BLUE, down_rect)
	
	#slow the game down to 30 fps
	clock.tick(FPS)
	pygame.display.update()

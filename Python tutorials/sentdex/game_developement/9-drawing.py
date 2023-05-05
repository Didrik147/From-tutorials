# -*- coding: utf-8 -*-

###Some modifications

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#COLOR = (red, green, blue)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WINDOWSIZE = (800, 600)

gameDisplay = pygame.display.set_mode(WINDOWSIZE)
gameDisplay.fill(BLACK)


pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = GREEN

#pygame.draw.line(gameDisplay, COLOR, start, end, thickness)
pygame.draw.line(gameDisplay, BLUE, (100,200), (300,450), 5)

pygame.draw.rect(gameDisplay, RED, (400,400,50,25))

pygame.draw.circle(gameDisplay, WHITE, (150,150), 75)

pygame.draw.polygon(gameDisplay, GREEN, 
      ((25,75), (76,125), (250,375), (400,25), (60,540)))


running = True

while running:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      running = False
      
  pygame.display.update()
  
  

pygame.quit()
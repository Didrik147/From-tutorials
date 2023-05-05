# -*- coding: utf-8 -*-
import pygame
import paddle


ScreenW, ScreenH = 1280, 720
backgroundColor = (125, 125, 125)


offset = 30
PaddleW = 200
PaddleH = 30
Paddlex = ScreenW/2 - PaddleW/2
Paddley = ScreenH - PaddleH - offset




pygame.init()

pygame.display.set_caption("Breakout Game")
Display = pygame.display.set_mode((ScreenW, ScreenH))
Display.fill(backgroundColor)

player = paddle.Paddle(Paddlex, Paddley, PaddleW, PaddleH)

FPSClock = pygame.time.Clock()
FPS = 60



GameOver = False

while not GameOver:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      GameOver = True
    
    Display.fill(backgroundColor)
    mousex = pygame.mouse.get_pos()[0]
    player.draw(Display)
    player.move(mousex)
    
    pygame.display.flip()
    pygame.display.update()
    FPSClock.tick(FPS)
      
      
    
pygame.quit()
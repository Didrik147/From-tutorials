# -*- coding: utf-8 -*-
import pygame

WHITE = (255, 255, 255)

class Paddle:
  def __init__(self, posx, posy, width, height):
    self.posx = posx
    self.posy = posy
    self.width = width
    self.height = height
    
    
  def draw(self, Display):
    pygame.draw.rect(Display, WHITE, 
                     [self.posx, self.posy, self.width, self.height])
    
  
  def move(self, mousex):
    self.posx = mousex - self.width/2
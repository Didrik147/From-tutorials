# -*- coding: utf-8 -*-

import scene
import pygame

def run():
  pygame.init()
  screen = pygame.display.set_mode((800,600))
  
  clock = pygame.time.Clock()
  
  sm = scene.SceneManager(scene)
  
  
  while sm.running:
    clock.tick(30) #30 FPS
    
    sm.update()
    sm.render()
    
    
  pygame.quit()
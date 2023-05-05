# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


class SceneManager(object):
  def __init__(self, screen):
    self.screen = screen
    
    self.scenes = {}
    
    self.activate_scene = None
    
    self.running = True


  def add_scene(scene, name):
    self.scenes[scene.name] = scene
    
    
  def activate_scene(self, scene, data=None):
    self.active_scene = self.scenes(scene)
    self.activate_scene.activate(data)
    
    
  def update(self):
    if self.running and self.activate_scene:
      self.active_scene.update()
    
  def render(self):
    if self.running and self.activate_scene:
      self.active_scene.render()





class Scene(object):
  def __init__(self, scene_manager, name):
    self.scene_manager = scene_manager
    self.name = 'default'
    
    self.setup()
    
    self.scene_manager.app_scene(self)
    
    def setup(self):
      return 
    
    def activate(self, data):
      return 
    
    def render(self):
      return 
    
    def update(self):
      return 
    
    


class MainMenu(Scene):
  def setup(self):
    self.name = 'menu'
    
    self.level = None
    self.difficulty = 1
    
    
    
    
    
    
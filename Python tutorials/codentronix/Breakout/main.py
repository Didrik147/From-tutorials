# -*- coding: utf-8 -*-
import pygame
import pygame as pg
import sys

SCREEN_SIZE = 640, 480

# Object dimensions
BRICK_WIDTH = 60
BRICK_HEIGHT = 15
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 12
BALL_DIAMETER = 16
BALL_RADIUS = BALL_DIAMETER/2

MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y = SCREEN_SIZE[1] - BALL_DIAMETER

# Paddle Y coordinate
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10


# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BRICK_COLOR = (200, 200, 0)


# State constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3    


def init_game(self):
  self.lives = 3
  self.score = 0
  self.state = STATE_BALL_IN_PADDLE
  
  self.paddle = pg.Rect(
      300, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT
      )
  
  self.ball = pg.Rect(
      300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER
      )
  
  self.ball_vel = [5, -5]
  
  #self.create_bricks()


def run(self):
  while True:
    for e in pg.event.get():
      if e.type == pygame.QUIT:
        sys.exit
    
    self.clock.tick(60)
    self.screen.fill(BLACK)
    

class Bricka:
  def __init__(self):
    pg.init()
    
    self.screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("bricka (a breakout clone)")
    
    self.clock = pg.time.Clock()
    
    if pg.font:
      self.font = pg.font.Font(None, 30)
    else:
      self.font = None
      
    self.init_game()


#if __name__ == "__main__":
Bricka().run()
# -*- coding: utf-8 -*-

import pygame as pg

pg.init()

win = pg.display.set_mode((500,500))

pg.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

RED = (255, 0, 0)
BLACK = (0, 0, 0)

#FPS = 60
#clock = pg.time.Clock()

run = True

while run:
    pg.time.delay(20) #can instead use FPS
    #clock.tick(FPS)
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT]:
        x -= vel
        
    if keys[pg.K_RIGHT]:
        x += vel
        
    if keys[pg.K_UP]:
        y -= vel
        
    if keys[pg.K_DOWN]:
        y += vel
        
    win.fill(BLACK)
    pg.draw.rect(win, RED, (x, y, width, height))
    
    pg.display.update()


pg.quit()
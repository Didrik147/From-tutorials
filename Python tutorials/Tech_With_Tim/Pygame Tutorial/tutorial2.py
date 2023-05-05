# -*- coding: utf-8 -*-

import pygame as pg

pg.init()

screenWidth = 500
screenHeight = 500

win = pg.display.set_mode((screenWidth,screenHeight))

pg.display.set_caption("First Game")

width = 40
height = 60
x = 100
y = 400
vel = 5

RED = (255, 0, 0)
BLACK = (0, 0, 0)

isJump = False
jumpCount = 10

run = True

FPS = 60
clock = pg.time.Clock()

while run:
    #pg.time.delay(20) #can instead use FPS
    clock.tick(FPS)
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    #We do not really need to use vel to set boudaries
    if keys[pg.K_LEFT] and x > 0:
        x -= vel
        
    if keys[pg.K_RIGHT] and x < screenWidth - width:
        x += vel
        
    if not isJump:
        if keys[pg.K_UP] and y > 0:
            y -= vel
            
        if keys[pg.K_DOWN] and y < screenHeight - height:
            y += vel
        
        if keys[pg.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
        
    
    
    win.fill(BLACK)
    pg.draw.rect(win, RED, (x, y, width, height))
    
    pg.display.update()


pg.quit()
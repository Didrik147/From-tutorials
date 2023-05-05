# -*- coding: utf-8 -*-

import pygame as pg


pg.init()

walkRight = []
walkLeft = []
folder = "Game/"
for i in range(1, 9+1):
    picR = folder + "R" + str(i) + ".png"
    picL = folder + "L" + str(i) + ".png"
    
    walkRight.append(pg.image.load(picR))
    walkLeft.append(pg.image.load(picL))



bg = pg.image.load(folder + 'bg.jpg')
char = pg.image.load(folder + 'standing.png')

bg_size = bg.get_rect().size

#screenWidth = 500
#screenHeight = 500
screenWidth = bg_size[0]
screenHeight = bg_size[1]


win = pg.display.set_mode((screenWidth,screenHeight))

pg.display.set_caption("Pygame Tutorial")

width = 40
height = 60
x = 100
y = 400
vel = 5



isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    
    
    win.blit(bg, (0,0)) #sprite, where to place it
    
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
        
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    
    
    #win.fill((0,0,0))
    #pg.draw.rect(win, (255,0,0), (x, y, width, height))
    
    pg.display.update()


run = True

FPS = 27
clock = pg.time.Clock()

#Main loop
while run:
    clock.tick(FPS)
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    #We do not really need to use vel to set boudaries
    if keys[pg.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
        
    elif keys[pg.K_RIGHT] and x < screenWidth - width:
        x += vel
        left = False
        right = True
     
    else:
        right = False
        left = False
        walkCount = 0
        
    if not isJump:        
        if keys[pg.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
        
    

    redrawGameWindow()



pg.quit()
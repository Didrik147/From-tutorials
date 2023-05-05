# -*- coding: utf-8 -*-

import pygame as pg

pg.init()


walkRight = []
walkLeft = []
folder = "Game/"
for i in range(1, 9+1):
    picR = folder + "R" + str(i) + ".png"
    picL = folder + "L" + str(i) + ".png"
    
    picR = pg.image.load(picR)
    #picR = pg.transform.scale(picR, (32,32))
    
    picL = pg.image.load(picL)
    #picL = pg.transform.scale(picL, (32,32))
    
    walkRight.append(picR)
    walkLeft.append(picL)



bg = pg.image.load(folder + 'bg.jpg')
char = pg.image.load(folder + 'standing.png')

bg_size = bg.get_rect().size

screenWidth = 600
screenHeight = 480
#screenWidth = bg_size[0]
#screenHeight = bg_size[1]

win = pg.display.set_mode((screenWidth,screenHeight))

pg.display.set_caption("Pygame Tutorial")


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    
    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
    
        if self.left:
            win.blit(walkLeft[self.walkCount//3], 
                     (self.x, self.y))
            self.walkCount += 1
            
        elif self.right:
            win.blit(walkRight[self.walkCount//3], 
                     (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))



def redrawGameWindow():
    win.blit(bg, (0,0)) #sprite, where to place it
    man.draw(win)
    pg.display.update()



FPS = 27
clock = pg.time.Clock()

man = player(300, 410, 64, 64)

#Main loop
run = True
while run:
    clock.tick(FPS)
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        
    elif keys[pg.K_RIGHT] and man.x < screenWidth - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
     
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not man.isJump:        
        if keys[pg.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount**2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
        
    

    redrawGameWindow()



pg.quit()
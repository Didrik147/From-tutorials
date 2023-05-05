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

screenWidth = 500
screenHeight = 480

win = pg.display.set_mode((screenWidth,screenHeight))

pg.display.set_caption("Pygame Tutorial")

BLACK = (0,0,0)


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
        self.standing = True
    
    
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
    
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], 
                         (self.x, self.y))
                self.walkCount += 1
                
            elif self.right:
                win.blit(walkRight[self.walkCount//3], 
                         (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))



class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        
        self.vel = 8 * facing
        
    def draw(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)




def redrawGameWindow():
    win.blit(bg, (0,0)) #sprite, where to place it
    man.draw(win)
    
    for bullet in bullets:
        bullet.draw(win)


    pg.display.update()



FPS = 27
clock = pg.time.Clock()

man = player(300, 410, 64, 64)
bullets = []

#Main loop
run = True
while run:
    clock.tick(FPS)
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pg.key.get_pressed()
    
    if keys[pg.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(man.x + man.width//2,
                           man.y + man.height//2, 
                           6, BLACK, facing))
        
            
    if keys[pg.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
        
    elif keys[pg.K_RIGHT] and man.x < screenWidth - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
     
    else:
        man.standing = True
        man.walkCount = 0
        
    if not man.isJump:        
        if keys[pg.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
            man.standing = True
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
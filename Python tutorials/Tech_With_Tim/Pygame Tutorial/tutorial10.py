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

BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARKGREEN = (0, 128, 0)

score = 0


bulletSound = pg.mixer.Sound('Game/bullet.wav')
hitSound = pg.mixer.Sound('Game/hit.wav')

music = pg.mixer.music.load('Game/music.mp3')
pg.mixer.music.play(-1)


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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    
    
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
        
        
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pg.draw.rect(win, RED, self.hitbox, 2)



    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pg.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, RED)
        win.blit(text, (250 - (text.get_width()/2), 200))
        pg.display.update()
        
        i = 0
        
        while i < 300:
            pg.time.delay(10)
            i += 1
            
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    i = 301
                    pg.quit()

        



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




class enemy(object):
    walkRight = []
    walkLeft = []
    folder = "Game/"
    for i in range(1, 11+1):
        picR = folder + "R" + str(i) + "E.png"
        picL = folder + "L" + str(i) + "E.png"
    
        walkRight.append(pg.image.load(picR))
        walkLeft.append(pg.image.load(picL))
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        
    def draw(self, win):
        self.move()
        
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        
            
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pg.draw.rect(win, RED, self.hitbox, 2)
            pg.draw.rect(win, RED, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pg.draw.rect(win, DARKGREEN, (self.hitbox[0], 
                self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
    
    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel*(-1)
                self.walkCount = 0
        
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel*(-1)
                self.walkCount = 0
            
        
    def hit(self):
        #if self.health > 0:
        if self.health > 1: #for at goblinen skal ha 10 liv
            self.health -= 1
        else:
            self.visible = False
        
        print("Hit")



def redrawGameWindow():
    win.blit(bg, (0,0)) #sprite, where to place it
    text = font.render("Score: " + str(score), 1, BLACK)
    
    win.blit(text, (350, 10))
    
    man.draw(win)
    goblin.draw(win)
    
    for bullet in bullets:
        bullet.draw(win)


    pg.display.update()



FPS = 27
clock = pg.time.Clock()


font = pg.font.SysFont("comicsans", 30, True)


man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []


#Main loop
run = True
while run:
    clock.tick(FPS)
    
    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
            
    keys = pg.key.get_pressed()
    
    if keys[pg.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.right:
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(projectile(int(man.x + man.width//2),
                           int(man.y + man.height//2), 
                           6, BLACK, facing))
        
        shootLoop = 1
            
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
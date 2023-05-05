import pygame

pygame.init()

display_width = 800
display_height = 600
SIZE = (display_width, display_height)

#RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


gameDisplay = pygame.display.set_mode(SIZE)
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar_V2.png')

sf = 2.5 #scaling factor
new_w = int(carImg.get_rect().size[0]/sf)
new_h = int(carImg.get_rect().size[1]/sf)
carImg = pygame.transform.scale(carImg, (new_w, new_h))


def car(x,y):
	# .blit(what, where) draws what we want to a background
	# where = (x,y)
	gameDisplay.blit(carImg, (x,y))


x = (display_width * 0.45)
y = (display_height * 0.8)


crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True	
		
	gameDisplay.fill(WHITE)
	car(x,y) # draws the car
		# can modify x and y to move the car
	pygame.display.update()
	FPS = 60
	clock.tick(FPS)


pygame.quit()
quit()




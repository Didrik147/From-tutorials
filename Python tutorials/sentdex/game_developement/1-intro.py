import pygame

pygame.init() #initiate pygame

#display with a specific size
SIZE = (800, 600)
gameDisplay = pygame.display.set_mode(SIZE)

pygame.display.set_caption('A bit Racey') #title

#Can be used to set FPS
clock = pygame.time.Clock()


crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #when hitting x on window
			crashed = True
	
		print(event)
	
	pygame.display.update() #can update things in the parameters
	#no parameters updates everything
	#can use display.flip instead?
	
	
	FPS = 60
	clock.tick(FPS)
	
	#change use FPS to make things faster, but
	#better to change movements instead (less taxing)
	

pygame.quit()
quit()




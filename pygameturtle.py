import pygame

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("thomas kitaba")
running = True

batteryimg= pygame.image.load("battery.png")
bayyeryx = 145
batyeryy = 550

def battery ():
 screen.blit(batteryimg,(batteryx,batteryy))
	
while running:
	screen.fill((205,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	battery()
	pygame.display.update()
	
	
	
	
import pygame

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("thomas kitaba")
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	
	screen.fill((255,0,0))
	pygame.display.update()

import pygame
import math
import time
import random
import csv

pygame.init()

pygame.time.Clock()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("thomas kitaba")
running = True

	
while running:
		

	current_time = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
			
		if event.type == pygame. MOUSEBUTTONDOWN:
			pass
				
	
				
	
	

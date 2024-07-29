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

jet_image= pygame.image.load("jet_1.png")






jet_cord_l = [0,0]
def jet(x, y):
	jet_image_s= pygame.transform.scale(jet_image, (80,80))
	jet_image_l= pygame.transform.rotate(jet_image_s, (45))
	screen.blit(jet_image_l,(x,y))
	

center_x = 300
center_y = 300
radius  = 200
	
def ufo(x, y):
	jet_image_l = pygame.transform.scale(jet_image, (80,80))
	screen.blit(jet_image_l,(x,y))
	
	
	
	
	
running = True
while running:
	screen.fill((255,255,255))
	current_time = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
			
		if event.type == pygame. MOUSEBUTTONDOWN:
			pass
	
	#======= jet line=====
	
	tank_x = 600
	tank_y = 600
	m = (tank_y - jet_cord_l[1])/(tank_x - jet_cord_l[1])
		
	b = jet_cord_l[1] - m * jet_cord_l[0]
		
	jet_cord_l[0] += 2
	
	jet_cord_l[1] = m* jet_cord_l[0] + b
		
	jet(jet_cord_l[0],jet_cord_l[1])
	
	if jet_cord_l[0] > 590 or jet_cord_l[1] > 590:
		
		jet_cord_l[0] = 0
		jet_cord_l[1] = 0

#====== UFO CIRCLE =======
	
	
	
	
	
	
	
	
	
	
	
	pygame.display.update()
				
	
				
	
	

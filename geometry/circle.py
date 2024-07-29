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

jet_image= pygame.image.load("ufo_1.png")
jet_l = [0,0]
jet_l[0] = 100
jet_l[1] = int(math.sqrt(200)**2 - (jet_l[0] - 300) - 300)

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
	jet_l[0] += 2
	center_l = [300,0]
	r = 200
	
	jet_l[1] = int(math.sqrt(r)**2 - (jet_l[0] - center_l[0]) - center_l[1])
	#jet_l[1] = int(math.sqrt(200)**2 - (jet_l[0] - 300))
	if jet_l[0] >450 and jet_l[1] <500:
		
		jet_l[0]= 0
	jet(jet_l[0], jet_l[1])
#====== UFO CIRCLE =======
	
	
	
	
	
	
	
	
	
	
	
	pygame.display.update()
				
	
				
	
	

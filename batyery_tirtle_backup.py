import pygame
import math
import time
import random
pygame.init()

pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("thomas kitaba")
running = True

velocity = 5
forward = 0
backward = 0
battery_index = 0
battery_step = 0
t_b = 80
life = 1
game_over = False

bush_l = []
tree_l = []




bullets_fired = 0
fired = False
scored = False
score = 0
shoot_missed = 0
top_screen = 20

up = 0
down = 0
#=========== EXPOLISION ============
tank_fire_x = 0
tank_fire_y = 0
tank_fire_l = []
car_expload_l = []
car_explosion_x = 0
car_explosion_y = 0
blast = False
exploaded_on_x = 0#
exploaded_on_y = 0#
explode = False
explode_coordinate = []



score_clock = 0
car_expload_image_1 = pygame.image.load("shockwave_1.png")

car_expload_image_2 = pygame.image.load("shockwave_2.png")

car_expload_l.append(pygame.transform.scale(car_expload_image_1,(50,50)))
car_expload_l.append(pygame.transform.scale(car_expload_image_1,(50,50)))

tank_fire_image = pygame.image.load("explosion_1.png")
tank_fire_l.append(pygame.transform.scale(tank_fire_image,(50,50)))

def tank_fire(i,j):
	if fired:
		screen.blit(tank_fire_l[0],(i+ 15,j -20))

def car_explosion(i,j):
	
		screen.blit(car_expload_l[1], (i,j))
		
		
#==========GAME_ LEVEL ==========
level_1 = True
level_2 = False
level_3 = False


#=========== BACKGROUND ==========
back_image_l= []
bg_index = 0
bg_image_1= pygame.image.load( "desert_1.jpg")
bg_image_2= pygame.image.load( "desert_2.jpg")
bg_image_3= pygame.image.load( "desert_3.jpg")

back_image_l.append(pygame.transform.scale(bg_image_1, (900,700)))

back_image_l.append(pygame.transform.scale(bg_image_2, (900,700)))

back_image_l.append(pygame.transform.scale(bg_image_3, (900,700)))



def background(bg_index):
	screen.blit(back_image_l[bg_index],(0,0))
	
	
#=========== BUSH AND TREE ==========
bush_x = int(random.randint(0,300))
bush_y = int(random.randint(100,300))
tree_x  = int(random.randint(300,600))
tree_y = int(random.randint(100,300))
rand_landscape = True
landscape_changed = False

bush_image = pygame.image.load("plant_1.png")
tree_image = pygame.image.load("tree_1.png")

bush_l.append(pygame.transform.scale(bush_image, (100,100)))

tree_l.append(pygame.transform.scale(tree_image,(100,100)))

#def bush_tree(b_x,b_y,t_x,t_y):

def bush_tree():
	screen.blit(bush_l [0], (bush_x,bush_y))
	screen.blit(tree_l[0], (tree_x, tree_y))
	
#========== TURTLE ============
turtleimg0= pygame.image.load("car_1.png")
turtlex = 300
turtley = 0
turtle_velocity = 3

def turtle(m,n,t):
	turtle = pygame.transform.scale(turtleimg0, (80,80))
	screen.blit(turtle,(turtlex,turtley))

#========== TANK=========
battery_l = []
bullet_l = []
batteryimg = []
batteryimg= [pygame.image.load('battery1.png'), pygame.image.load('battery1.png'),pygame.image.load('battery_fired.png')]
batteryx = 245 
batteryy = 550

battery_l.append(pygame.transform.scale(batteryimg[0],(80,80)))

battery_l.append(pygame.transform.scale(batteryimg[1],(80,80)))

battery_l.append(pygame.transform.scale(batteryimg[2],(80,80)))

#========= BULLET ========

bulletimg = pygame.image.load("bullet1.png")
bulletx = batteryx 
bullety = batteryy 
b_velocity_y = 10

def bullet():
	
	bullet_l = pygame.transform.scale(bulletimg,(20,50))
	
	if fired:
		screen.blit(bullet_l,(bulletx + 30, bullety))
#=======TURTLE========


def battery (x,y,i):
	    if not fired:
	    	screen.blit(battery_l[i],(batteryx,batteryy))
	    else:
	    	screen.blit(battery_l[2],(batteryx,batteryy))

#def game
def game_life(s,l):
	s = str(s)
	l = str(l)

	myfont = pygame.font.SysFont("Comic Sans MS", 60)
# apply it to text on a label
	lable = myfont.render('LIFE:', 1, (250,0,0))
	lable_score = myfont.render('SCORE:', 1, (255,0,0))
# put the label object on the screen at point x=100, 
	myscore = myfont.render(l,1,(0,0,0))
	mylife = myfont.render(s,1,(0,0,0))
	
	screen.blit(lable_score,(350,0))
	screen.blit(myscore,(550,0))
	screen.blit(lable, (50, 0))	
	screen.blit(mylife,(150,0))   
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
running = True
if  game_over == False:
	while running:
		# Initialize timer
		current_time = pygame.time.get_ticks()
		exploded_on_x = 0
		exploded_on_y = 0
		
		# ------ change BACKGROUND according to SCORE----
		
		if score >= 0 and score < 10:
			level_1 = True
			level_2 = False
			level_3 = False
			
		if score >= 10 and score < 20:
			level_1 = False
			level_2 = True
			level_3 = False
			
		if score >= 20 and score < 22:
			level_1 = False
			level_2 = False
			level_3 = True
			
		if score >= 30: # to be deleyed at the end
			score = 0
			
		if level_1:
			bg_index = 0
			turtle_velocity = 3
			
		if level_2:
			bg_index = 1
			turtle_velocity = 6
			
		if level_3:
			bg_index = 2
			turtle_velocity = 15
			
			
		screen.fill((205,0,0))
		background(bg_index)
		
		bullet()  
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame. MOUSEBUTTONDOWN:
				fired = True
				
		#battery(batteryx,batteryy,battery_index)
		
		# HORIZONTAL MOVEMENT
		
		if batteryx < 600 and forward == 1:
			# when going to the right
			batteryx += 6
			battery_step += 1 # costume change 
			battery_index =1 # for costume change
			
			if  fired == False:
			       bulletx = batteryx
			       tank_fire_x = batteryx
			       bullets_fired += 1 # for shooting bullet
			
			
		else:
			forward = 0
			backward = 1
			#battery_index = 0
			
		if batteryx > 0 and backward == 1 :
			
			batteryx -= 6
			battery_step += 1
			if fired == False:
				bulletx= batteryx #move bullet with battery
				tank_fire_x = batteryx
				bullets_fired += 1
			 # for shooting bullet
		else:
			forward = 1
			backward = 0
			#batteryy -= 1
		
		# VERTICAL MOVEMENT of turtle ENEMY
		
		if turtley < 600:#and down == 1:
			## down ward m]vment
			turtley += turtle_velocity
			#car_explosion_y = turtley
			#car_explosion_x = turtlex
			
			
			if turtley > 600:
				turtlex = int(random.randint(0,600))
				turtley = 20
				car_explosion_x = turtlex
				car_explosion_y = turtley
				
		#----- to move turtle UP AND DOWN -----
	#	if turtley < 600 and down == 1:
			## down ward m]vment
		#	turtley += 6
		
	#	else:
			
			#up = 1
			#down = 0
			
			
		#if turtley > 0 and up == 1:
			#turtley -= 6
		#else:
			#up = 0
			#down = 1
	#--------------------------------------------------		
			
					# FIRE BULLET
	#	shoot_missed means bullet touched the top
	#TODO    ADD CODE FOR TRIGERING EVENT
		if fired == True:
			bullety -= 50
		
		if bullety <= top_screen:
				bulletx = batteryx
				bullety = batteryy  # remove 50 later
				fired = False
				#bullets_fired += 1
	# change costume
	# RESET STER COUNTER AND BOX INDEX
		if battery_step >=0 and	battery_step < 30 :
			battery_index = 0
			#battery_step = 0
			
			
		if battery_step > 30 and battery_step <= 60:
			battery_index = 1
		
		if battery_step > 60:
			battery_step = 0
			
		battery(batteryx,batteryy,battery_index )
	
	# check collision for life lost
	
		d = int(math.sqrt((turtlex-batteryx)**2 + (turtley-batteryy)**2))
		
		if d > 100:
				turtle(turtlex, turtley,t_b)		
		else:
				life -= 1
				turtlex = int(random.randint(0,600))
				turtley = 20
				 # bleeding tirtle
				 #play hit sound
		if	life == 0:
			life = 5
		#global game_over
			game_over = True
			runnning = False
		
		#check collision for SCORE OR HIT POINTS
		hit_distance = int(math.sqrt((turtlex-bulletx)**2 + (turtley-bullety)**2))
		if (hit_distance >= 0 and hit_distance <=50):
			scored = True
			explode_coordinate.append(turtlex)
			explode_coordinate.append(turtley)
			
			turtlex = int(random.randint(0,600))
			turtley = 20
			score_clock = pygame.time.get_ticks()
		else:
					
		# record SCORE
			if scored == True :
			     score += 1
			     blast = True
			     #exploded_on_x = turtlex
			     #exploded_on_y = turtley
			     
			 	
		
			
				
			scored = False
			
			if current_time - score_clock < 500:
				explode = True
				
			else:
				explode = False
				
			if explode == True:
				car_explosion(explode_coordinate[0], explode_coordinate[1])
			else:
				explode_coordinate.clear()
				
				#car_explosion(299,234)
				
				
			
	
		
			
		game_life(life, score)
		
		
		# DROW BUSH AND TREE RANDOMELY
		
		
	
		car_explosion(car_explosion_x, car_explosion_y)
		bush_tree()
		tank_fire(batteryx, batteryy)
		pygame.display.update()
		
	pygame.quit()
else:
		
	background()
	
	

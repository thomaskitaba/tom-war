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
life = 5
game_over = False

gun_equiped = True
missiel_equiped = False
weapon = ["gun"] # defoult

bush_l = []
tree_l = []

#------MOVEMENT-------
move_right = False
move_left = False


bullets_fired = 0
fired = False
scored = False
score = 0
shoot_missed = 0
top_screen = 20

up = 0
down = 0
#=========== MUSIC ================
#Powerful Trap Beat | Strong by Alex-Productions | https://www.youtube.com/channel/UCx0_M61F81Nfb-BRXE-SeVA
#Music promoted by https://www.chosic.com/free-music/all/
#Creative Commons CC BY 3.0
#https://creativecommons.org/licenses/by/3.0/
 
 
# moving tank sound 
# car exploding 
pygame.mixer.music.load("Powerful-Trap-.mp3")
#pygame.mixer.music.load("mixkit-tank-engine-working-2753.wav")
pygame.mixer.music.play(-1)


tank_firing_0 = pygame.mixer.Sound("12-Gauge-Pump-Action-Shotgun-Far-Gunshot-C-www.fesliyanstudios.com (1).mp3")


car_explode_sound_0 = pygame.mixer.Sound("Big-Glass-Breaking-Combo-www.fesliyanstudios.com.mp3")
car_explode_sound_0 = pygame.mixer.Sound("Big-Glass-Breaking-Combo-www.fesliyanstudios.com.mp3")
#tank_hit_sound = pygame.mixer.sound()

	


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
hit_time = [0]



score_clock = 0
car_expload_image_1 = pygame.image.load("shockwave_1.png")

car_expload_image_2 = pygame.image.load("explosion_2.png")

car_expload_l.append(pygame.transform.scale(car_expload_image_1,(70,70)))
car_expload_l.append(pygame.transform.scale(car_expload_image_2,(100,100)))

tank_fire_image = pygame.image.load("explosion_1.png")
tank_fire_l.append(pygame.transform.scale(tank_fire_image,(50,50)))

def tank_fire(i,j):
	if fired:
		screen.blit(tank_fire_l[0],(i+ 15,j -30))

def car_explosion(i,j):
	
		screen.blit(car_expload_l[0], (i,j))
def explode_tank(i,j):
	screen.blit(car_expload_l[1], (i,j))
	


		
		
#==========GAME_ LEVEL ==========
level_1 = True # when it starts it is LEVEL 1
level_2 = True
level_3 = True


#=========== BACKGROUND ==========
back_image_l= []
bg_index = 0
screen_width = 900
screen_height = 700
txt_bg_l = []

bg_image_1= pygame.image.load( "desert_1.jpg")
bg_image_2= pygame.image.load( "desert_2.jpg")
bg_image_3= pygame.image.load( "desert_3.jpg")

back_image_l.append(pygame.transform.scale(bg_image_1, (900,700)))

back_image_l.append(pygame.transform.scale(bg_image_2, (900,700)))

back_image_l.append(pygame.transform.scale(bg_image_3, (900,700)))

# text back ground
text_bg = pygame.image.load("txt_bg.jpg")
txt_bg_l.append( pygame.transform.scale(text_bg,(screen_width
,60)))

def background(bg_index):
	screen.blit(back_image_l[bg_index],(0,0))
	screen.blit(txt_bg_l[0], (0,0))
	screen.blit(txt_bg_l[0], (0,650))

#def background(bg_index):
	#screen.blit(back_image_l[bg_index],(0,0))
	
	
#=========== BUSH AND TREE ==========
#bush 0


rand_landscape = True
landscape_changed = False

bush_image_0 = pygame.image.load("plant_1.png")
bush_image_1 = pygame.image.load("plant_2.png")
bush_image_2= pygame.image.load("plant_3.png")

tree_image_0 = pygame.image.load("tree_1.png")
tree_image_1 = pygame.image.load("tree_2.png")
tree_image_2 = pygame.image.load("tree_3.png")

bush_l.append(pygame.transform.scale(bush_image_0, (100,100)))#
bush_l.append(pygame.transform.scale(bush_image_1, (100,100)))#
bush_l.append(pygame.transform.scale(bush_image_2, (100,100)))#

tree_l.append(pygame.transform.scale(tree_image_0,(100,100)))#
tree_l.append(pygame.transform.scale(tree_image_1,(100,100)))#
tree_l.append(pygame.transform.scale(tree_image_2,(100,100)))


def bush_tree():
	
	if level_1:
		
		screen.blit(bush_l [0], (bush_x,bush_y))
		screen.blit(tree_l[0], (tree_x, tree_y))
		
	if level_2:
		
		screen.blit(bush_l [1], (bush_1_x, bush_1_y))
		screen.blit(tree_l[1], (tree_1_x,tree_1_y))
		
	if level_3:
		
		screen.blit(bush_l [2], (bush_2_x, bush_2_y))
		screen.blit(tree_l[2], (tree_2_x, tree_2_y))
	
	
level_landscape_l = [0,0,0]
bush_tree_coordinates= [0,0,0,0]
def change_landscape():
	#bush 0
	screen.blit(bush_l [0], (bush_tree_coordinates[0],bush_tree_coordinates[1]))
	
	screen.blit(tree_l[0], (bush_tree_coordinates[2],bush_tree_coordinates[3]))
#======= WEAPON UPGRADE =========
weapon_upgrader_x = 200
weapon_upgrader_y = 0
weapon_upgrader_velocity = 2
weapon_l =[]
weapon_upgrader_image = pygame.image.load("car_2.png")
weapon_upgrader_image_l = [pygame.transform.scale(weapon_upgrader_image,(80,80))]

def weapon_upgrader( weapon_upgrader_x, weapon_upgrader_y):
	if level_2 and weapon[0] == "gun":
		screen.blit(weapon_upgrader_image_l[0],(weapon_upgrader_x, weapon_upgrader_y))

#============ TURTLE =============
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
batteryimg= [pygame.image.load('battery_0.png'), pygame.image.load('battery_1.png')]
batteryx = 245 
batteryy = 550

battery_l.append(pygame.transform.scale(batteryimg[0],(80,80)))

battery_l.append(pygame.transform.scale(batteryimg[1],(80,80)))

#battery_l.append(pygame.transform.scale(batteryimg[2],(80,80)))

#========= BULLET and MISSIEL ========

bulletimg = pygame.image.load("bullet1.png")
bulletx = batteryx 
bullety = batteryy 
b_velocity_y = 10

missiel_velocity = 10
missiel_x = batteryx
missiel_y = batteryy
fired_missiel = False
weapon_upgraded = False
#missiel_img_l = []


missiel_img = pygame.image.load("missile_0.png")
missiel_img_rotate= pygame.transform.rotate(missiel_img, (-45))
missiel_img_l = [pygame.transform.scale(missiel_img_rotate,(100, 100)), pygame.transform.scale(missiel_img_rotate,(100, 100))]

def bullet():
	
	bullet_l = pygame.transform.scale(bulletimg,(20,50))
	if fired:# and weapon[0] == "gun":
		screen.blit(bullet_l,(bulletx + 30, bullety))
		
def fire_missiel(missiel_x,missiel_y):
	#if fired_missiel== True and weapon[0] =="missiel":
	if weapon_upgraded:
		screen.blit(missiel_img_l[0],(missiel_x - 30,missiel_y))
		screen.blit(missiel_img_l[1],(missiel_x + 20,missiel_y))
	
	
	
#=======TURTLE========
def battery (x,y,i):
	    if not fired:
	    	screen.blit(battery_l[i],(batteryx,batteryy))
	    else:
	    	screen.blit(battery_l[1],(batteryx,batteryy))

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
	
#======== SHOW HEARTS =========	
show_hearts_l = [True,True, True,True,True]
heart_l = []
heart = pygame.image.load("heart_0.png")
heart_l.append(pygame.transform.scale(heart,(50,50)))

def show_hearts():
	
	if show_hearts_l [0] == True:
		screen.blit(heart_l[0],(20,650))
	if show_hearts_l [1] == True:
		screen.blit(heart_l[0],(80,650))
	if show_hearts_l [2] == True:
		screen.blit(heart_l[0],(140,650))
	if show_hearts_l [3] == True:
		screen.blit(heart_l[0],(200,650))
	if show_hearts_l [4] == True:
		screen.blit(heart_l[0],(260,650))
	
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
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				
				#for i in range(5):
					#show_hearts_l[i] = True
		#	if event.type == pygame.KEYDOWN:
			#	if event.key == K_RIGHT:
				#	move_right = True
				#	move_left = False
		#	if event.type == pygame.KEYDOWN:
			#	if event.key == K_LEFT:
				#	move_right = False
					#move_left = True
			
			
			if event.type == pygame. MOUSEBUTTONDOWN:
				fired = True
				fired_missiel = True
				tank_firing_0.play()
				if game_over == True:
					game_over = False # reset game
					score = 0
					life = 5
																							
		#if score >= 0 and score < 10:
		if score >= 0 and score < 2:
			level_1 = True
			level_2 = False
			level_3 = False
			
		#if score >= 10 and score < 20:
		if score >= 2 and score < 4:
			level_1 = False
			level_2 = True
			level_3 = False
			
			
		#if score >= 20 and score < 30:
		if score >= 4 and score < 6:
			level_1 = False
			level_2 = False
			level_3 = True
			
		#if score >= 30: # to be deleyed at the end
		if score >= 6:
			level_1 = True
			level_2 = False
			level_3 = True
			
		if level_1:
			bg_index = 0
			turtle_velocity = 3
			
			
		if level_2:
			bg_index = 1
			turtle_velocity = 6
			
		if level_3:
			bg_index = 2
			turtle_velocity = 8
			
		
		screen.fill((205,0,0))
		background(bg_index)
		
		if level_1 and level_landscape_l[0] == 0:
			
			
			bush_tree_coordinates[0] = int(random.randint(0,300))
			bush_tree_coordinates[1] = int(random.randint(100,300))
			bush_tree_coordinates[2] = int(random.randint(300,600))
			bush_tree_coordinates[3] = int(random.randint(100,300))
			level_landscape_l[0] = 1
			
			
			
		if level_2 and level_landscape_l[1] == 0:
			
			#change_landscape(bush_x,bush_y,tree_x,tree_y)
			bush_tree_coordinates[0] = int(random.randint(0,300))
			bush_tree_coordinates[1] = int(random.randint(100,300))
			bush_tree_coordinates[2] = int(random.randint(300,600))
			bush_tree_coordinates[3] = int(random.randint(100,300))
		
			level_landscape_l[1] = 1
		if level_3 and level_landscape_l[2] == 0:
			bush_tree_coordinates[0] = int(random.randint(0,300))
			bush_tree_coordinates[1] = int(random.randint(100,300))
			bush_tree_coordinates[2] = int(random.randint(300,600))
			bush_tree_coordinates[3] = int(random.randint(100,300))
		
			#change_landscape(bush_x,bush_y,tree_x,tree_y)
			level_landscape_l[2] = 1
		
		bullet()  
		change_landscape()
		
				
		#battery(batteryx,batteryy,battery_index)
		
		# HORIZONTAL MOVEMENT
		if not game_over:
			if batteryx < 600 and forward == 1:
				# when going to the right
				batteryx += 6
				battery_step += 1 # costume change 
				battery_index =1 # for costume change
				
				if  fired == False:
				       bulletx = batteryx
				       missiel_x = batteryx
				       tank_fire_x = batteryx
				       bullets_fired += 1 # for shooting bullet
				
				
			else:
				forward = 0
				backward = 1
				#battery_index = 0
				
			if batteryx > 0 and backward == 1 :
				
				batteryx -= 6
				missiel_x = batteryx
				battery_step += 1
				if fired == False:
				#	missiel_x = batteryx
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
		
			
				if turtley > 600:
					turtlex = int(random.randint(0,600))
					turtley = 20
					car_explosion_x = turtlex
					car_explosion_y = turtley
					
			# spawn weapon_upgrader: 
			if weapon_upgrader_y < 700 and level_2:
					weapon_upgrader_y += 1
					
			weapon_upgrader(weapon_upgrader_x,weapon_upgrader_y)
			# upgrade weapon to missiel
			distance_with_upgrader  = int(math.sqrt((weapon_upgrader_x - bulletx)**2 + (weapon_upgrader_y - bullety)**2))
			if distance_with_upgrader > 0 and distance_with_upgrader <= 50:
					weapon[0] = "missiel"
					weapon_upgraded = True
					
					
					
					
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
				##### end of ]F GAME_OVER
	#--------------------------------------------------		
			
	# FIRE BULLET
	#	shoot_missed means bullet touched the top
	#TODO    ADD CODE FOR TRIGERING EVENT
		if fired == True :
			bullety -= 50
			
		
		if bullety <= top_screen:
				bulletx = batteryx
				bullety = batteryy  # remove 50 later
				fired = False
				#bullets_fired += 1
		
		
		if fired_missiel and weapon [0] == "missiel":
			missiel_y -= 20
		if missiel_y <= top_screen:
			missiel_y = batteryy
			missiel_x = batteryx  # to the left of the tank
			fired_missiel= False
		
	
			
			
	

	# RESET STER COUNTER AND BOX INDEX
		if battery_step >=0 and	battery_step < 30 :
			battery_index = 0
			#battery_step = 0
			
		if battery_step > 30 and battery_step <= 60:
			battery_index = 1
		
		if battery_step > 60:
			battery_step = 0
			
		battery(batteryx,batteryy,battery_index )
	
	
	#====== LIFE LOST COLLISION======
	
		d = int(math.sqrt((turtlex-batteryx)**2 + (turtley-batteryy)**2))
		
		if d > 100:
				turtle(turtlex, turtley,t_b)		
		else:
				###### CODE FOR TANK EXPLOSION GOES HERE
			
				
				hit_time[0] = pygame.time.get_ticks()
				car_explode_sound_0.play()
				
				
				life -= 1
				turtlex = int(random.randint(0,600))
				turtley = 20
				 # bleeding tirtle
				 #play hit sound
		#if	life == 0:
			
			#life = 5
		#global game_over
			#game_over = True
			#runnning = False
		
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
				
			scored = False
			
			if current_time - score_clock < 300:
				explode = True
				
			else:
				explode = False
				
			if explode == True:
				car_explosion(explode_coordinate[0], explode_coordinate[1])
			else:
				explode_coordinate.clear() # clear  the list so that we can add new collision coordinatex
			
		# CODE TO REDUCE THE HEARTS
		
		if life == 4:
			show_hearts_l[life] = False
		if life == 3:
			show_hearts_l[life] = False
		if life == 2:
			show_hearts_l[life] = False
		if life == 1:
			show_hearts_l[life] = False
		if life == 0:
			show_hearts_l[life] = False
			
			game_over = True
			runnning = False
			for i in range(5):
				show_hearts_l[i] = False
		
		# BLIT EXPL]SION ABOVE TANK		 
		if current_time - hit_time[0] < 200:
					explode_tank(batteryx, batteryy)	
		show_hearts()	
		game_life(life, score)
		
		# DROW BUSH AND TREE RANDOMELY
		#bush_tree()
		tank_fire(batteryx, batteryy)
		
		#missiel()
		fire_missiel(missiel_x ,missiel_y)
		pygame.display.update()
		
	pygame.quit()
else:
		
	background()
	
	


import pygame
import math
import time
import random
import csv
from os.path import exists as does_file_exist
pygame.init()

area_of_destruction_l = [-1]
pygame.time.Clock()

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("thomas kitaba")
running = True

velocity = 5
forward = 0
backward = 0
battery_index = 0
battery_step = 0
t_b = 80
life = 5
level = [0]
game_over = False

rand_score = []

gun_equiped = True
missiel_equiped = False
 # default
 
hit_tank_missiel = True
hit_by_tank_time = 0
hit_jet = True
tank_spawned_time = 0
hit_by_jet_time = 0
hit_by_tank = False
hit_by_jet = False
 
bush_l = []
tree_l = []

#==========GAME_ LEVEL ==========
level_0 = True
level_1 = True # when it starts it is LEVEL 1
level_2 = True
level_3 = True
level_4 = True
level_sound = True

#------MOVEMENT-------
move_right = False
move_left = False


bullets_fired = 0
fired = False
scored = False
score = 0
shoot_missed = 0
top_screen = 20
h_s_c = []

up = 0
down = 0
#=========== MUSIC ================
#Powerful Trap Beat | Strong by Alex-Productions | https://www.youtube.com/channel/UCx0_M61F81Nfb-BRXE-SeVA
#Music promoted by https://www.chosic.com/free-music/all/
#Creative Commons CC BY 3.0
#https://creativecommons.org/licenses/by/3.0/
 
 
# moving tank sound 
# car exploding 
#pygame.mixer.music.load("Powerful-Trap-.mp3")
pygame.mixer.music.load("battel_sound.mp3") #https://sounds-mp3.com/i-en-tank-movement

tank_firing_0 = pygame.mixer.Sound("12-Gauge-Pump-Action-Shotgun-Far-Gunshot-C-www.fesliyanstudios.com (1).mp3")

missiel_firing_0 = pygame.mixer.Sound("12-Gauge-Pump-Action-Shotgun-Far-Gunshot-C-www.fesliyanstudios.com (1).mp3")
car_explode_sound_0 = pygame.mixer.Sound("Big-Glass-Breaking-Combo-www.fesliyanstudios.com.mp3")


#Music from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6939">Pixabay</a>
tank_hit_sound_0 = pygame.mixer.Sound("Big-Glass-Breaking-Combo-www.fesliyanstudios.com.mp3")
#tank_hit_sound = pygame.mixer.sound()
#missiel_launch_sound = pygame.mixer.Sound("1911-reload-6248.mp3")

#Music from <a #href="https://pixabay.com/music/#?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6248">Pixabay</a>
weapon_upgrade_sound = pygame.mixer.Sound("Video-Game-Power-Level-Up-A1-www.fesliyanstudios.com.mp3") 
#https://www.fesliyanstudios.com/play-mp3/5255
level_change_sound = pygame.mixer.Sound("Video-Game-Power-Level-Up-A1-www.fesliyanstudios.com.mp3") 
#https://www.fesliyanstudios.com/play-mp3/5255

#===GET EXPLOSSION COORDINATE  ========
saved_coordinate = True

battery_coord = False
turtle_coord = False
jet_coord = False
ufo_coord = False



saved_battery_coord_l = [0,0]
saved_turtle_coord_l = [0,0]
saved_jet_coord_l = [0,0]
saved_ufo_coord_l = [0,0]

def save_coordinate(x,y):
  if battery_coord:
    saved_battery_coord_l[0] = x
    saved_battery_coord_l[1] = y
    #battery_coord = True
    
  if turtle_coord:
    saved_turtle_coord_l [0] = x
    saved_turtle_coord_l [1] = y
    
  if jet_coord:
    saved_jet_coord_l [0] = x
    saved_jet_coord_l [1] = y
    
  if ufo_coord:
    saved_ufo_coord_l [0] = x
    saved_ufo_coord_l [1] = y
  # display saved coordinate
  
#====== DISPLAY CHECK OUTPUT=====
x_coord = 0
y_coord = 0

myfont = pygame.font.SysFont("Comic Sans MS", 60)
# apply it to text on a label
lable  = myfont.render('X , Y:', 1, (250,0,0))

def display_result(x,y):
  x_coord = str(x)
  y_coord = str(y)
  
  lable_x_coord = myfont.render(x_coord, 1, (255,0,0))
  
  lable_y_coord = myfont.render(y_coord, 1, (255,0,0))
  
  screen.blit(lable_x_coord,(50, 50))
  screen.blit(lable_y_coord,(100, 100))
  
#=========== EXPOLISION ============
tank_fire_x = 0
tank_fire_y = 0
tank_fire_l = []
car_expload_l = []
car_explosion_x = 0
car_explosion_y = 0
tank_expload_l = []
blast = False
exploaded_on_x = 0#
exploaded_on_y = 0#
explode = False
explode_coordinate = []
hit_time = [0]
player_name = [""]
jet_explode_l = []

score_clock = 0
car_expload_image_1 = pygame.image.load("shockwave_1.png")

car_expload_image_2 = pygame.image.load("explosion_1.png")

tank_expload_image= pygame.image.load("shockwave_2.png")
tank_expload_l.append(pygame.transform.scale(tank_expload_image,(100,100)))


car_expload_l.append(pygame.transform.scale(car_expload_image_1,(70,70)))
car_expload_l.append(pygame.transform.scale(car_expload_image_2,(100,100)))

tank_fire_image = pygame.image.load("explosion_1.png")
tank_fire_l.append(pygame.transform.scale(tank_fire_image,(50,50)))

jet_explode_image = pygame.image.load("explosion_1.png")
jet_explode_l.append(pygame.transform.scale(jet_explode_image,(100,100)))

def tank_fire(i,j):
  if fired:
    screen.blit(tank_fire_l[0],(i+ 15,j -27))

def car_explosion(i,j):
  
    screen.blit(car_expload_l[0], (i,j))
def explode_tank(i,j):
  screen.blit(car_expload_l[1], (i,j))
  
def explode_tank_2(i,j):
  screen.blit(tank_expload_l[0], (i,j-20))	
  
def explode_jet(i,j):
  screen.blit(jet_explode_l[0], (i,j))
  

#=========== BACKGROUND ==========
back_image_l= []
bg_index = 0

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
weapon_upgrader_x = -200
weapon_upgrader_y = 0
weapon_upgrader_velocity = 2
weapon_upgrader_visible = False


weapon_upgrader_image = pygame.image.load("car_2.png")
weapon_upgrader_image_l = [pygame.transform.scale(weapon_upgrader_image,(80,80))]


def weapon_upgrader( weapon_upgrader_x, weapon_upgrader_y):
  #if score== 10 and  weapon[0] == "gun":+
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

#====== ENEMY TANK============= 
enemy_tank_image = pygame.image.load("enemy_tank_1.png")


enemy_tank_x = 50
enemy_tank_y = 50
enemy_tank_size = [0]
enemy_missiel_velocity = 0

def spawn_enemy_tank(x,y, size):
  enemy_tank_image_scaled = pygame.transform.scale(enemy_tank_image, (size,size))
  enemy_tank_image_rotated = pygame.transform.rotate(enemy_tank_image_scaled, (225))
  screen.blit(enemy_tank_image_rotated, (0,0))


#+++++++++++++++++++++++++++++
#====== ENEMY TANK============= 

#battery_l.append(pygame.transform.scale(batteryimg[2],(80,80)))

#=======JET JET JET JET JET JET =======
#=======JET JET JET JET JET JET =======
#=======JET JET JET JET JET JET =======

target = [0,0]
#===== GET X , Y COORDINATE =======
get_coordinate_l = [0] # 0 = NO     1 = YES
def get_tank_position(x_coordinate,  y_coordinate):
  if get_coordinate_l[0] == 1:
    
    target[0] = x_coordinate # indx 0 = x _cord
    target[1] = y_coordinate # indx 1 = y_cord
    
    get_coordinate_l[0] = 0
jet_image = pygame.image.load("jet_1.png")
j_i_t = pygame.transform.scale(jet_image, (100,100))

jet_angle = 0
jet_level = False
jet_target = [20,20]
rand_jet_x = 0
rand_jet_y = int(random.randint(10, 200))
get_target_coordinate_l = [0]

def spawn_jet(target_x , target_y, jet_x, jet_y, rotation):
  
  
  if target[0] <= 0:
    jet_angle =  0
  if target[0] > 0 and target[0] <= 100:
    jet_angle = 45 / 6
  if target[0] > 100 and target[0] <= 200:
    jet_angle = 45 / 5
  if target[0] > 200 and target[0] <= 300:
    jet_angle = 45 / 4
  if target[0] > 300 and target[0] <= 400:
    jet_angle = 45 / 3
  if target[0] > 400 and target[0] <= 500:
    jet_angle = 45 / 2
  if target[0] > 500 and target[0] <= 600:
    jet_angle = 45 / 1
  if target[0] > 600:
    jet_angle = 60
    
  jet_rotated = [pygame.transform.rotate(j_i_t,(jet_angle))]
  
  screen.blit(jet_rotated[0], (jet_x, jet_y))
  #screen.blit(jet_rotated[0], (jet_target[0],jet_target[1]))
  
def display_jet(x,y):
  screen.blit(jet_rotated[0], (x, y))
  
#==== JET STRAIGHT LINE JET JEY ======


tank_missiel_image= pygame.image.load("missile_1.png")
jet_cord_l = [0,0]
tank_missiel_image_l = [0,0]


def jet(x, y):
  tank_missiel_image_s= pygame.transform.scale(tank_missiel_image, (80,80))
  tank_missiel_image_l= pygame.transform.rotate(tank_missiel_image_s, (-90))
  screen.blit(tank_missiel_image_l,(x,y))
  


  
# ===== UFO UFO UFO UFO UFO UFO =====
ufo_image = pygame.image.load("ufo_1.png")
ufo_l = [0,0]

ufo_l[0] = 300
ufo_l[1] = 100
angle_1 = 0


def ufo(x, y):
  if level_3 or level_4:
    ufo_image_l = [pygame.transform.scale(ufo_image, (80,80))]
    screen.blit(ufo_image_l[0],(x*math.cos(angle_1) + 300, y*math.sin(angle_1) + 300))
    
#========= BULLET and MISSIEL ========

bulletimg = pygame.image.load("bullet1.png")
bulletx = batteryx 
bullety = batteryy 
b_velocity_y = 10

const_missiel_x = []
spawn_upgrader_l = [0]

missiel_velocity = 5
missiel_x = batteryx
missiel_y = batteryy

left_missiel_x = batteryx
left_missiel_y = batteryy

right_missiel_x = batteryx
right_missiel_y = batteryy

fired_missiel = False
weapon_upgraded_l = [0]
weapon_upgraded_l= [0]
weapon_upgraded = False
missiel_coordinate = []
weapon_l = ['gun']
#missiel_img_l = []

missiel_img = pygame.image.load("missile_0.png")
missiel_img_rotate= pygame.transform.rotate(missiel_img, (-45))
missiel_img_l = [pygame.transform.scale(missiel_img_rotate,(100, 100)), pygame.transform.scale(missiel_img_rotate,(100, 100))]

def bullet():
  
  bullet_l = pygame.transform.scale(bulletimg,(20,50))
  if fired:# and weapon[0] == "gun":
    screen.blit(bullet_l,(bulletx + 30, bullety))
      
def fire_missiel_2nd(left_missiel_x, right_missiel_x,missiel_y):

  if weapon_upgraded_l[0] == 1:
    screen.blit(missiel_img_l[0],( left_missiel_x ,missiel_y))
    screen.blit(missiel_img_l[1],(right_missiel_x,missiel_y))
    #-----------
    #----- launchs the missiel---
#=======TURTLE========
def battery (x,y,i):
      if not fired:
        screen.blit(battery_l[i],(batteryx,batteryy))
      else:
        screen.blit(battery_l[1],(batteryx,batteryy))

#==================================
#==================================
#==================================
#==================================
#=================================
#=====  SPLASH SCREEN  1=====
my_splash_screen_l = []
splash_start_time = pygame.time.get_ticks()

def splash_screen():
  my_splash_screen =	pygame.image.load("splash_tank.jpg")
  my_splash_screen_l.append(pygame.transform.scale(my_splash_screen,(700,700)))
  screen.blit(my_splash_screen_l[0],(0,0))
  
initializing = True
while initializing:
  splash_screen()
  pygame.mixer.music.load("Powerful-Trap-.mp3")
  pygame.mixer.music.play(-1)
  current_splash_time = pygame.time.get_ticks()
  if current_splash_time - splash_start_time >=1000:
    initializing = False
  pygame.display.update()

            

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#SCREEN 2-- SCREEN 2--SCREEN 2
#==================================
#==================================
#==================================
#==================================
#=====  PLAYERS AND HIGH SCORE  =======

# varables 
import csv
from os.path import exists as does_file_exist

def record_high_score (scorer_name, end_score):
  
  col_name =["name", "score"]
  default_rows= [['Thomas kitaba', 1000000], ['b', 9] , ['c', 8], ['d',7], ['e',6], ['f', 5], ['g', 4] , ['h', 3], ['i',2], ['j' ,1]]
  #print("if file does not exist fill this default_rows= [['a', 55], ['b', 50] , ['c', 45], ['d',35], ['e',30]] ")
  if does_file_exist("High_Score.csv"):
  
    with open("High_Score.csv", 'r') as game_high_score:
        high_score_csv= list(csv.reader(game_high_score))
        #print(high_score_csv)		
        
    high_score_csv.remove(high_score_csv[0])
  
    for scores in high_score_csv:
      scores[1] = int(scores[1])
  else:
    #print(high_score_csv)
    with open("High_Score.csv", 'w') as High_Score_file:
      high_score_csv =csv.writer(High_Score_file)
      high_score_csv.writerow(col_name)
      high_score_csv.writerows(default_rows)
    
    with open("High_Score.csv", 'r') as game_high_score:
      high_score_csv= list(csv.reader(game_high_score))
    high_score_csv.remove(high_score_csv[0])
    for i in range(len(high_score_csv)):
      high_score_csv[i][1] = int(high_score_csv[i][1])
        
  print(high_score_csv)
  
      #high_score_csv = high_score_csv.next()
    
  print("---------------------******")
  high_score_l = [ 55,50,45,35,30]
  
#	scorer_name = "tommy-0kit"
#	score = 40
  # from tje game itself
  #high_score_csv = [['tom', 55], ['kit', 50] , ['aba', 45], ['cat',35], ['dpg',30]]
  print(high_score_csv)
  #print(list(high_score_d[0].values()))
  insert_position = -1 # last posotion
  # find index to insert 
  
  print(insert_position)
  print(score)
  
  for i in range(len(high_score_csv)):
    if score >= high_score_csv[i][1]:
      insert_position = i 
      break
  print(insert_position)
  
  #insert_position = 1		
  
  print("______________________")
  
  for j in range(1,len(high_score_csv)):
    
    if score < high_score_csv[4][1]:
      break
    if insert_position == len(high_score_csv) - 1:
      high_score_csv[insert_position][0] = scorer_name
      high_score_csv[insert_position][1] = score
      
    else:
      high_score_csv[len( high_score_csv) - j][0] = high_score_csv[len( high_score_csv ) - j - 1][0]
      high_score_csv[len( high_score_csv) - j][1] = high_score_csv[len( high_score_csv ) - j - 1][1]
      
      if len(high_score_csv) - j-1 == insert_position:
        high_score_csv[insert_position][0] = scorer_name
        high_score_csv[insert_position][1] = score
      
        break
      
  print(high_score_csv)
  
  with open("High_Score.csv", 'w') as High_Score_file:
      new_high_score = csv.writer(High_Score_file)
      new_high_score.writerow(col_name)
      new_high_score.writerows(high_score_csv)
      
  with open("High_Score.csv", 'r') as game_high_score:
      high_score_csv = list(csv.reader(game_high_score))
  print(high_score_csv)	
  
  h_s_c = high_score_csv 	
  
  print("______________________")
  print("______________________")
  print("______________________")
  
#	game_over = True # TO BE DELETED LATTER

def display_high_score(h_score_w, h_score_h):
  
  
  if game_over:
    
    pygame.draw.rect(screen,(255,19,0), pygame.Rect(70,80, 560, 540), 4)
    high_score_bg= pygame.image.load("grass_1.jpg")
    #high_score_bg_l= [pygame.transform.scale(high_score_bg,(500,500))]
  #screen.blit(high_score_bg_l[0], (100,100))
    
    hs_font = pygame.font.SysFont("Comic Sans MS", 40)
    # rendere hs, player name,  rank
    lbl_hs = hs_font.render("High Score", 1,(255,0,0))
    lbl_plyr = hs_font.render("Player", 1,(0,0,0))
    lbl_scr = hs_font.render("Score", 1,(0,0,0))
    lbl_1 = hs_font.render("1", 1,(0,0,0))
    lbl_2 = hs_font.render("2", 1,(0,0,0))
    lbl_3 = hs_font.render("3", 1,(0,0,0))
    lbl_4 = hs_font.render("4", 1,(0,0,0))
    lbl_5 = hs_font.render("5", 1,(0,0,0))
    lbl_6 = hs_font.render("6", 1,(0,0,0))
    lbl_7 = hs_font.render("7", 1,(0,0,0))
    lbl_8 = hs_font.render("8", 1,(0,0,0))
    lbl_9 = hs_font.render("9", 1,(0,0,0))
    lbl_10 = hs_font.render("10", 1,(0,0,0))
    
    # blit rank
    screen.blit(lbl_hs, (250, 120))
    screen.blit(lbl_plyr, (150, 140))
    screen.blit(lbl_scr, (450, 140))
    screen.blit(lbl_1, (h_score_w - 490, 180))
    screen.blit(lbl_2, (h_score_w - 490, 220))
    screen.blit(lbl_3, (h_score_w - 490, 260))
    screen.blit(lbl_4, (h_score_w - 490, 300))
    screen.blit(lbl_5, (h_score_w - 490, 340))
    screen.blit(lbl_6, (h_score_w - 490, 380))
    screen.blit(lbl_7, (h_score_w - 490, 420))
    screen.blit(lbl_8, (h_score_w - 490, 460))
    screen.blit(lbl_9, (h_score_w - 490, 500))
    screen.blit(lbl_10, (h_score_w - 500, 540))
    
    #High_Score_csv 
    
    if does_file_exist:
      with open("High_Score.csv") as hs_file:
        h_s= list(csv.reader(hs_file))
        
      h_s.remove(h_s[0])
      nm_1 = hs_font.render(h_s[0][0], 1,(0,0,0))
      nm_2 = hs_font.render(h_s[1][0], 1,(0,0,0))
      nm_3 = hs_font.render(h_s[2][0], 1,(0,0,0))
      nm_4 = hs_font.render(h_s[3][0], 1,(0,0,0))
      nm_5 = hs_font.render(h_s[4][0], 1,(0,0,0))
      nm_6 = hs_font.render(h_s[5][0], 1,(0,0,0))
      nm_7 = hs_font.render(h_s[6][0], 1,(0,0,0))
      nm_8 = hs_font.render(h_s[7][0], 1,(0,0,0))
      nm_9 = hs_font.render(h_s[8][0], 1,(0,0,0))
      nm_10 = hs_font.render(h_s[9][0], 1,(0,0,0))
      
      val_1 = hs_font.render(h_s[0][1], 1,(0,0,0))
      val_2 = hs_font.render(h_s[1][1], 1,(0,0,0))
      val_3 = hs_font.render(h_s[2][1], 1,(0,0,0))
      val_4 = hs_font.render(h_s[3][1], 1,(0,0,0))
      val_5 = hs_font.render(h_s[4][1], 1,(0,0,0))
      val_6= hs_font.render(h_s[5][1], 1,(0,0,0))
      val_7= hs_font.render(h_s[6][1], 1,(0,0,0))
      val_8= hs_font.render(h_s[7][1], 1,(0,0,0))
      val_9 = hs_font.render(h_s[8][1], 1,(0,0,0))
      val_10 = hs_font.render(h_s[9][1], 1,(0,0,0))
      
      screen.blit(nm_1, (140, 180))
      screen.blit(nm_2, (140, 220))
      screen.blit(nm_3, (140, 260))
      screen.blit(nm_4, (140, 300))
      screen.blit(nm_5, (140, 340))
      screen.blit(nm_6, (140, 380))
      screen.blit(nm_7, (140, 420))
      screen.blit(nm_8, (140, 460))
      screen.blit(nm_9, (140, 500))
      screen.blit(nm_10, (140, 540))
      
      screen.blit(val_1, (h_score_w -100, 180))
      screen.blit(val_2, (h_score_w -100, 220 ))
      screen.blit(val_3, (h_score_w -100, 260 ))
      screen.blit(val_4,  (h_score_w -100, 300))
      screen.blit(val_5, (h_score_w -100, 340))
      screen.blit(val_6, (h_score_w -100, 380))
      screen.blit(val_7, (h_score_w -100, 420 ))
      screen.blit(val_8, (h_score_w -100, 460 ))
      screen.blit(val_9,  (h_score_w -100, 500))
      screen.blit(val_10, (h_score_w -100, 540))
    
    
#SCREEN 2-- SCREEN 2--SCREEN 2
#==================================
#==================================
#==================================
#==================================
#==================================
    
#++++++ END OF HIGH SCORE SCREEN+++++

player_name_l = []
player = " "
typing = True
#++++++++++  FONT FOR SCREEN 2 =======
my_small_font = pygame.font.SysFont("Comic Sans MS", 60)
my_medium_font = pygame.font.SysFont("Comic Sans MS", 70)

def display_screen_2():
  
  enter_name = my_medium_font.render(" PLAYER NAME ", 1,(125,0,0))
  screen.blit(enter_name,(100, 50))


def input_box():
  pygame.draw.rect(screen,(255,0,0),pygame.Rect(80,140,550,80), 2)

while typing:
  screen.fill((0,0,1))
  display_screen_2()
  input_box()
  
  for events in pygame.event.get():
      
    if events.type == pygame.KEYDOWN :
      if events.key == pygame.K_RETURN :
        typing = False
      if events.key== pygame.K_BACKSPACE:
        player = player[: -1]	
      else:
          
        player += events.unicode
        player_name_l.append(events.unicode)
        
      player_name = my_small_font.render(player, 1,(250,10,0))		
      screen.blit(player_name, (100, 150))
    pygame.display.update()
            
  # END OF WHILE LOOP 	
def player():
  
  display_name = my_small_font.render(str(player), 1, (0,0,0))
  
  screen.blit(player_name, (500, 30))
#==================================

def game_life(s,l, level):
  s = str(s)
  l = str(l)
  level = str(level)
  
  my_big_font = pygame.font.SysFont("Comic Sans MS", 100)
  myfont = pygame.font.SysFont("Comic Sans MS", 40)
# apply it to text on a label
  lable_life = myfont.render('LIFE:', 1, (250,0,0))
  lable_score = myfont.render('SCORE:', 1, (255,0,0))
# put the label object on the screen at point x=100, s
  mylife = myfont.render(s,1,(0,0,0))
  gameover = my_big_font.render("GAME OVER  ",1,(0,0,0))
  if game_over:
    screen.blit(gameover,(150,600))
  #level 
  label_level = myfont.render("LEVEL" ,1,(250,0,0))
  my_level = myfont.render(level, 1,(0,0,0))
  screen.blit(label_level,(450,660))
  screen.blit(my_level,(600,660))


  myscore = myfont.render(l,1,(0,0,0))
  screen.blit(lable_score,(500,0))
  screen.blit(myscore,(620,0))
  screen.blit(lable_life, (0, 0))	
  screen.blit(mylife,(80,0))   
  
# end of game life
  
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
    
            #############
            ## GAME DATA##
            #############
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
mini_turtle_l = []
mini_missile_l = []
mini_jet_l = []
mini_ufo_l = []


# integer value

turtle_shoot= 0
tank_missiel_shoot = 0
jet_shoot= 0
ufo_shoot= 0

turtle_missed= 0
tank_missiel_missed = 0
jet_missed = 0
ufo_missed = 0

turtle_shoot_l = [0]
tank_missiel_shoot_l = [0]
jet_shoot_l = [0]
ufo_shoot_l = [0]

turtle_missed_l = [0]
tank_missiel_missed_l = [0]
jet_missed_l = [0]
ufo_missed_l = [0]

total_enemies_distroyed_l = [0]
total_enemies_missed_l= [0]
total_enemies_l = [0]
shoot_accuracy_l = [0]


total_enemies_distroyed = 0
total_enemies_missed = 0
total_enemies = 0
shoot_accuracy = 0

#


shoot_statstics_l = [0]
 #[total_enemies_distroyed_l[0] + total_enemies_l[0]]

# convert to string to blit it on the screen
turtle_shoot = str(turtle_shoot_l[0])
tank_missiel_shoot = str(tank_missiel_shoot_l[0])
jet_shoot = str(jet_shoot_l[0])
ufo_shoot = str(ufo_shoot_l[0])

turtle_missed = str(turtle_missed_l[0])

tank_missile_missed = str(tank_missiel_missed_l[0])

jet_missed = str(jet_missed_l[0])
ufo_missed = str(ufo_missed_l[0])

total_enemies_distroyed = str(total_enemies_distroyed_l[0])

total_enemies_missed =str(total_enemies_missed_l[0])

total_enemies = str(total_enemies_l[0])

shoot_accuracy = str(shoot_accuracy_l[0])

#-----------------------------------------------
# blit jet,car, ufo,missiel on screen

mini_turtle = pygame.image.load("car_1.png")
mini_jet = pygame.image.load("jet_1.png")
mini_missile_1= pygame.image.load("missile_1.png")
mini_missile = pygame.transform.rotate(mini_missile_1,(45))

mini_ufo = pygame.image.load("ufo_1.png")
# SCALE IMAGES 
mini_turtle_l.append(pygame.transform.scale(mini_turtle, (40,40)))

mini_missile_l.append(pygame.transform.scale(mini_missile, (50,40)))
mini_jet_l.append(pygame.transform.scale(mini_jet, (50,40)))
mini_ufo_l.append(pygame.transform.scale(mini_ufo, (30,40)))

game_data_font = pygame.font.SysFont("Comic Sans MS", 30)
g_d_f = pygame.font.SysFont("Comic Sans MS", 30)
game_data_small_font = pygame.font.SysFont("Comic Sans MS", 25)
# left title


#   SHOW GAME DATA FUNCTION
#++++++++++++++++++++++++++++++++


def show_statistics():
  total_enemies_distroyed_l = [0]
  total_enemies_missed_l = [0]
  total_enemies_l = [0]
  shoot_accuracy_l = [0]
  
  total_enemies_distroyed_l[0] = turtle_shoot_l[0] + tank_missiel_shoot_l[0] +jet_shoot_l[0] + ufo_shoot_l[0] 
  
  total_enemies_missed_l[0] = turtle_missed_l[0] + tank_missiel_shoot_l[0] +jet_missed_l[0] + ufo_missed_l[0]
  
  
  total_enemies_l[0] =  total_enemies_distroyed_l[0] + total_enemies_missed_l[0]
  
  shoot_accuracy_l = total_enemies_distroyed_l[0] + total_enemies_l[0]
  
  
  if score > 0:
    
    shoot_statstics_l[0]  = round((turtle_shoot_l[0] /total_enemies_l[0] )) 
    
  #temp_stat_l[0] =f" {shoot_statstics_l[0] :.%}"	
  shoot_statstics = str(shoot_statstics_l[0]) + %
  shoot_statstics_r = game_data_small_font.render( shoot_statstics, 1, (0,0,255))
  screen.blit(shoot_statstics_r, (410,30))
  #screen.blit(total_enemies_r, (410,70))
  
  

def show_game_data():
  turtle_shoot = str(turtle_shoot_l[0])
  tank_missiel_shoot = str(tank_missiel_shoot_l[0])
  jet_shoot = str(jet_shoot_l[0])
  ufo_shoot = str(ufo_shoot_l[0])
  
  turtle_missed = str(turtle_missed_l[0])
  
  tank_missile_missed = str(tank_missiel_missed_l[0])
  
  jet_missed = str(jet_missed_l[0])
  ufo_missed = str(ufo_missed_l[0])
  
  total_enemies_distroyed = str(total_enemies_distroyed_l[0])
  
  total_enemies_missed =str(total_enemies_missed_l[0])
  
  total_enemies = str(total_enemies_l[0])
  
  shoot_accuracy = str(shoot_accuracy_l[0])
  
  lable_destroyed = game_data_font.render("hit", 1,(255,0,0))
  lable_missed = game_data_font.render("miss", 1, (255,0,0))
  
  lable_accuracy = game_data_small_font.render("ACCURACY",1, (255,0,0))
  lable_total_enemies = game_data_small_font.render("ENEMIES",1, (255,0,0))
  
  
  lbl_turtle_destroyed = game_data_font.render( turtle_shoot, 1, (255,0,0))
  lbl_tank_missile_destroyed = game_data_font.render( tank_missiel_shoot, 1, (255,0,0))
  lbl_jet_destroyed = game_data_font.render( jet_shoot, 1, (255,0,0))
  lbl_ufo_destroyed = game_data_font.render( ufo_shoot, 1, (255,0,0))
  
  #MISSED
  lbl_turtle_missed= game_data_font.render( turtle_missed, 1, (255,0,0))
  
  lbl_tank_missile_missed = game_data_font.render( tank_missile_missed, 1, (255,0,0))
  
  lbl_jet_missed = game_data_font.render( jet_missed, 1, (255,0,0))
  
  lbl_ufo_missed = game_data_font.render( ufo_missed, 1, (255,0,0))
  
  # STATISTICS
  #
  
  
  
  screen.blit(mini_turtle_l[0], (150,0))
  screen.blit(mini_missile_l[0], (200,0))
  screen.blit(mini_jet_l[0], (270,0))
  screen.blit(mini_ufo_l[0], (340,0))
  
  screen.blit(lable_accuracy, (380, 0))
  screen.blit(lable_total_enemies, (380, 55))

  screen.blit(lable_destroyed, (100, 50))
  screen.blit(lable_missed, (100, 70))
  
  #ACTUAL GAME DATA
  # RENDER VALUES FOR BLITING
  
  
  
  turtle_shoot_r = g_d_f.render( turtle_shoot, 1, (0,0,255))
  tank_missiel_shoot_r = g_d_f.render(tank_missiel_shoot, 1, (0,0,255))
  jet_shoot_r = g_d_f.render(jet_shoot, 1, (0,0,255))
  ufo_shoot_r = g_d_f.render(ufo_shoot, 1, (0,0,255))
  
  turtle_missed_r= g_d_f.render(turtle_missed, 1, (0,0,255))
  
  tank_missile_missed_r = g_d_f.render(tank_missile_missed, 1, (0,0,255))
  
  jet_missed_r = g_d_f.render(jet_missed, 1, (0,0,255))
  ufo_missed_r = g_d_f.render(ufo_missed, 1, (0,0,255))
  
  
  total_enemies_distroyed_r = g_d_f.render(total_enemies_distroyed, 1, (0,0,255))
  
  total_enemies_missed_r =g_d_f.render(total_enemies_missed, 1, (0,0,255))
  
  total_enemies_r = g_d_f.render(total_enemies, 1, (0,0,255))
  
  shoot_accuracy_r = g_d_f.render(shoot_accuracy, 1, (0,0,255))
  
  #### HIT - HIT - HIT
  screen.blit(turtle_shoot_r, (150,50))
  screen.blit(tank_missiel_shoot_r, (200,50))
  screen.blit(jet_shoot_r, (270,50))
  screen.blit(ufo_shoot_r, (340,50))
  
  ### MISSED - MISSID -MISSED
  screen.blit(turtle_missed_r, (150,70))
  screen.blit(tank_missile_missed_r, (200,70))
  screen.blit(jet_missed_r, (270,70))
  screen.blit(ufo_missed_r, (340,70))
  
  
  


             ###END OF### 
            ## GAME DATA##
            #############

#START=START=START=START=START=START=START=START=START=START=START=START=STAR
#START=START=START=START=START=START=START=START=START=START=START=START=STAR
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pygame.mixer.music.load("battel_sound.mp3")
pygame.mixer.music.play(-1)

running = True
if  game_over == False:
  while running:
    # Initialize timer
    # set level option 
    level_option_main = True
    level_option_test = False
    
    
    get_coordinate_l[0] = 1
    
    current_time = pygame.time.get_ticks()
    exploded_on_x = 0
    exploded_on_y = 0
    
    #  change BACKGROUND according to SCORE-
  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
      if event.type == pygame. MOUSEBUTTONDOWN:
        if not fired:
          tank_firing_0.play()
        fired = True
        
        # store x value of tank to fire the rocket along a constant  x axis
        if not fired_missiel:
          const_missiel_x.clear()
          const_missiel_x.append(batteryx)
        fired_missiel = True
        
        # make missiel move on a constant x axis
        # save missiel x coordinate in a list
        if game_over == True:
          # reset game_data to default
          turtle_shoot_l = [0]
          tank_missiel_shoot_l = [0]
          jet_shoot_l = [0]
          ufo_shoot_l = [0]
          
          turtle_missed_l = [0]
          tank_missiel_missed_l = [0]
          jet_missed_l = [0]
          ufo_missed_l = [0]
          
          # reset weapon to default
          weapon_upgraded_l[0] = 0
          
          fired_missiel = False
          fired = False
          weapon_l[0] = "gun"
          score = 0
          
          game_over = False # reset game

          if not game_over:
            get_coordinate_l[0] = 1
            for i in range(5):
              show_hearts_l[i] = True
          life = 5
          #score = 0
    if level_option_main:
      if score >= 0 and score < 10:
    #if score >= 0 and score < 3:
    
        level_0 = False	
        level_1 = True
        level_2 = False
        level_3 = False
        level_4 = False
        level[0] = 1 # show level on the bottom the screen
    
      if score >= 10 and score < 20:
      #if score >= 3 and score < 6:
        if level_1: 
          level_change_sound.play()
        
        level_1 = False
        level_2 = True
        level_3 = False
        level_4 = False
        level[0] = 2
        
        
      if score >= 20 and score < 30:
      #if score >= 6 and score < 11:
        if level_2: 
          level_change_sound.play()
          
        level_1 = False
        level_2 = False
        level_3 = True
        level_4 = False
        level[0] = 3
        
      if score >= 30: # to be deleyed at the end
      #if score >= 11:
        if level_3: 
          level_change_sound.play()
          
        level_1 = False
        level_2 = False
        level_3 = False
        level_4 = True
        level[0] = 4						
      
    if level_option_test:
      
      if score >= 0 and score < 3:
        level_0 = False	
        level_1 = True
        level_2 = False
        level_3 = False
        level_4 = False
        level[0] = 1 # show level on the bottom the screen
  
      if score >= 3 and score < 6:
        if level_1: 
          level_change_sound.play()
        
        level_1 = False
        level_2 = True
        level_3 = False
        level_4 = False
        level[0] = 2
        
      if score >= 6 and score < 11:
        if level_2: 
          level_change_sound.play()
          
        level_1 = False
        level_2 = False
        level_3 = True
        level_4 = False
        level[0] = 3
        
    
      if score >= 11:
        if level_3: 
          level_change_sound.play()
          
        level_1 = False
        level_2 = False
        level_3 = False
        level_4 = True
        level[0] = 4
  # _______________________________
    if level_1:
      bg_index = 0
      turtle_velocity = 2
      missiel_velocity = 20
      area_of_destruction_l  = [40]
      enemy_tank_level = False
      jet_level = False
      ufo_level = False
      # enable jet level
    #	jet_level = True

    if level_2:
      bg_index = 1
      turtle_velocity = 6
      missiel_velocity= 30
      area_of_destruction_l  = [50]
      enemy_tank_level = True
      jet_level = False
      ufo_level = False
      
    if level_3:
      bg_index = 2
      turtle_velocity = 13
      missiel_velocity = 45
      area_of_destruction_l  = [70]
      jet_level = True
      ufo_level = False
      
      #get_coordinate_l[0] = 1
    
    if level_4:
      bg_index = 1
      turtle_velocity = 13
      missiel_velocity = 50
      area_of_destruction_l  = [90]
      ufo_level = True
      #get_coordinate_l[0] = 1
      
#----------------------------------------------------	
    screen.fill((205,0,0)) 
    background(bg_index)
#----------------------------------------------------
    
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
#----------------------------------------------------
    change_landscape()
#----------------------------------------------------
  
    
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
        if turtley >= 600:
          turtlex = int(random.randint(0,600))
          turtle_missed_l[0]+= 1
          turtley = 20
          car_explosion_x = turtlex
          car_explosion_y = turtley
      
#============= JET LEVEL =============	
      jet_tank_d = int(math.sqrt((rand_jet_x - batteryx)**2 + (rand_jet_y - batteryy)**2))
      
      if jet_tank_d < 80:
        hit_by_jet = True
      else:
        hit_by_jet = False
        
      if hit_by_jet:
        life -= 1
        jet_missed_l[0] += 1
        hit_by_jet = False
        car_explode_sound_0.play()
        hit_by_jet_time = pygame.time.get_ticks()
        saved_jet_coord_l.clear()
        saved_jet_coord_l = [rand_jet_x, rand_jet_y]
        
  # WRITE THIS CODE AT THE END TO BLIT EXPLOSION ABOVE JET
    
        #if current_time - hit_by_jet_time < 3000:
          #explode_tank(saved_jet_coord_l[0], saved_jet_coord_l[1])
          
        rand_jet_x = 0 
        rand_jet_y = int(random.randint(0,100))
          
      if jet_level  :
      
        get_tank_position(batteryx,  batteryy)
        get_coordinate_l[0] = 0
        
        if rand_jet_x < 50 and batteryx < 100:
          
          rand_jet_x = 300
          
        if rand_jet_x == target[0]:
          rand_jet_x += 10
          start_jet_strike = pygame.time.get_ticks()
        rand_jet_x < 50
        # take jet to orignal position if out of screen
        if rand_jet_y < 0:
          rand_jet_y = int(random.randint(10,100))
          rand_jet_x = 0
          
        slope = (target[1] -rand_jet_y) / (target[0] - rand_jet_x)
          
        b = rand_jet_y - slope * rand_jet_x
      # movment 
        rand_jet_x += 1
        if rand_jet_x > 300:
          rand_jet_y += 5
        else:
          rand_jet_y = slope * rand_jet_x + b
        
        # ==== FIND ROTATION ===
        
        if rand_jet_y > 650:
          rand_jet_x = 0
          
          rand_jet_y =  int(random.randint(10, 200))
          jet_missed_l[0] += 1
        rotation_angle = 20	
        spawn_jet(batteryx,  batteryy, rand_jet_x, rand_jet_y, rotation_angle)
        
#===========  TANK LEVEL ============	
  ## TANK  ON STRAIGHT LINE  FROM (600, 0) ##
  # ----  LIFE LOST FOR BY TANK_MISSIEL ---  #
      missiel_tank_d = int(math.sqrt((tank_missiel_image_l[0] - batteryx)**2 + (tank_missiel_image_l[1]-batteryy)**2))
      
      if missiel_tank_d < 80:
        hit_by_tank = True
      else:
        hit_by_tank = False
        
      if hit_by_tank:
        life -= 1
        tank_missiel_missed_l[0] += 1
        hit_by_tank = False
        car_explode_sound_0.play()
        hit_by_tank_time = pygame.time.get_ticks()
        
        
        tank_missiel_image_l[0] = 0
        tank_missiel_image_l[1] = 0
      
      #=== ADD THIS AT THE END TO BLIT THE EXPLOSION ABOVE THE TANK
  #__if current_time - hit_by_tank_time  < 2000:
    
  #__			explode_tank(batteryx,batteryy)
        
  # END OF --   LIFE LOST FOR BY TANK_MISSIEL -
      if enemy_tank_level: # and ( level_2 or level_3 or level_4):
        # initialize velocity
        if level_2:
            enemy_missiel_velocity = 4
        if level_3:
            enemy_missiel_velocity = 7
        if level_4:
            enemy_missiel_velocity = 10
            
    # enlarge tank at the top left corner
        if enemy_tank_size[0] >= 0 and enemy_tank_size[0] <= 90: # tank size
          enemy_tank_size[0] += 1
#---------------------------------------------------
        spawn_enemy_tank(0,0, enemy_tank_size[0])		
#---------------------------------------------------
        
        if enemy_tank_size[0] > 85 and enemy_tank_size[0] <= 89:
            tank_spawned_time = pygame.time.get_ticks()
# after enemy tank rechs its full size fire missiel
        if enemy_tank_size[0] >= 90:	
          if current_time - tank_spawned_time >= 2000:
          
            battery_coord = True
            if saved_coordinate:
              save_coordinate(batteryx, batteryy)
              saved_coordinate = False
          
            tank_x = 600
            tank_y = 600
            m = (tank_y - tank_missiel_image_l[1])/(tank_x - tank_missiel_image_l[1])
            b = tank_missiel_image_l[1] - m * tank_missiel_image_l[0]
            tank_missiel_image_l[0] += enemy_missiel_velocity
            tank_missiel_image_l[1] = m* tank_missiel_image_l[0] + b
            jet(tank_missiel_image_l[0],tank_missiel_image_l[1])
          
            if tank_missiel_image_l[0] > 590 or tank_missiel_image_l[1] > 590:
              tank_missiel_missed_l[0] += 1
              tank_missiel_image_l[0] = 0
              tank_missiel_image_l[1] = 0
              
              # to use the coordinayes
              saved_battery_coord_l[0] = 0
              saved_battery_coord_l[1] = 0
                      

#======== UFO UFO UFO UFO UFO =======
      if ufo_level:
        angle_1 += 0.01
#---------------------------------------------------
        ufo(ufo_l[0], ufo_l[1])
#---------------------------------------------------

      
#======= WEAPON   UPGRDE ============		
      # spawn weapon_upgrader: 
      #++++++++++++++
      #for i in range(0,100,)
      if score >= 3 and weapon_upgraded_l[0] == 0:
        weapon_upgrader_y += 5
        weapon_upgrader(weapon_upgrader_x,weapon_upgrader_y)
      if weapon_upgrader_y >= 600:
          weapon_upgrader_y = 0
          #weapon_upgrader_x= -100
          weapon_upgrader_x= int(random.randint(0,600))
      
      # upgrade weapon to missiel
      distance_with_upgrader  = int(math.sqrt((weapon_upgrader_x - bulletx)**2 + (weapon_upgrader_y - bullety)**2))
    #	distance_with_upgrader = 30
    
      if distance_with_upgrader >= 0 and distance_with_upgrader <= 50 and fired :
        weapon_upgrade_sound.play()
        weapon_l[0] = "missiel"
        weapon_upgrader_x= -100
        weapon_upgraded_l[0] = 1
            # take upgrader out to right or left of the screen
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
    
    if fired_missiel:
      missiel_y -= missiel_velocity
      missiel_coordinate.clear()
      missiel_coordinate.append(batteryx)
    if missiel_y <= top_screen:
      #missiel_coordinate.clear()
      missiel_y = batteryy
      missiel_x = batteryx  # to the left of the tank
      fired_missiel= False
    
  # RESET STER COUNTER AND BOX INDEX
    if battery_step >=0 and battery_step < 30 :
      battery_index = 0
      #battery_step = 0
      
    if battery_step > 30 and battery_step <= 60:
      battery_index = 1
    
    if battery_step > 60:
      battery_step = 0
#---------------------------------------------------
    battery(batteryx,batteryy,battery_index )
#---------------------------------------------------
  
  #====== LIFE LOST COLLISION======
  
    d = int(math.sqrt((turtlex-batteryx)**2 + (turtley-batteryy)**2))
    
    # when hit by jet
    jet_d = int(math.sqrt((batteryx -rand_jet_x)**2 + (batteryy - rand_jet_y)**2))
    # HIT BY JET JET JEYLT
    if jet_d <= 50:
      car_explode_sound_0.play()
      rand_jet_x = 0
      rand_jet_y =  int(random.randint(10,100))
      life -= 1
      
    if d > 100 :
        turtle(turtlex, turtley,t_b)		
    else:
        ###### CODE FOR TANK EXPLOSION GOES HERE
        hit_time[0] = pygame.time.get_ticks()
        #tank_hit_sound.play()
        car_explode_sound_0.play()
        life -= 1
        turtle_missed_l[0] +=  1
        turtlex = int(random.randint(0,600))
        
        turtley = 20
    #check collision for SCORE OR HIT POINTS
    # hit by left missiel
#------------------------------------------------	
    missiel_1_on_target = int(math.sqrt((turtlex-left_missiel_x)**2 + (turtley - missiel_y)**2))
    #hit by right missiel
    missiel_2_on_target = int(math.sqrt((turtlex-right_missiel_x)**2 + (turtley-missiel_y)**2))
    
    missiel_1_on_tank_missiel = int(math.sqrt((tank_missiel_image_l[0] -left_missiel_x)**2 + (tank_missiel_image_l[1] - missiel_y)**2))
    #hit by right missiel
    missiel_2_on_tank_missiel = int(math.sqrt((tank_missiel_image_l[0] - right_missiel_x)**2 + (tank_missiel_image_l[1] - missiel_y)**2))
    
    bullet_on_tank_missiel = int(math.sqrt((tank_missiel_image_l[0] -bulletx)**2 + (tank_missiel_image_l[1] - bullety)**2))
    
    missiel_1_on_jet = int(math.sqrt((rand_jet_x -left_missiel_x)**2 + (rand_jet_y - missiel_y)**2))
    #hit by right missiel
    missiel_2_on_jet = int(math.sqrt((rand_jet_x - right_missiel_x)**2 + (rand_jet_y - missiel_y)**2))
    bullet_on_jet = int(math.sqrt((rand_jet_x -bulletx)**2 + (rand_jet_y - bullety)**2))
    
    
# ----- ENABLE and  DISABLE BULLETS HITING CAPABILITY
    if tank_missiel_image_l[1] > 0 and tank_missiel_image_l[1] <=500:
      hit_tank_missiel = True
    else:
      hit_tank_missiel = False
      
    
#------------------------------------------------
# TANK MISSIEL HIT BY MISSIEL OR BULLET
    if ((missiel_1_on_tank_missiel > 0 and missiel_1_on_tank_missiel < 50) or (missiel_2_on_tank_missiel > 0 and missiel_2_on_tank_missiel < 50) or (bullet_on_tank_missiel > 0 and bullet_on_tank_missiel < 50) ) and hit_tank_missiel == True:
      score += 1
      tank_missiel_shoot_l[0] += 1
      tank_missiel_hit_time = pygame.time.get_ticks()
      # save coordinate for explosion 
      saved_ufo_coord_l.clear()
      saved_ufo_coord_l.append(tank_missiel_image_l[0])
      saved_ufo_coord_l.append(tank_missiel_image_l[0])
      
      if current_time - tank_missiel_hit_time < 300:
        car_explosion(saved_ufo_coord_l[0], saved_ufo_coord_l[1])
        #explosion(saved_ufo_coord_l[0], saved_ufo_coord_l[1])
      
      # resawn tank missiel to its orignal position
      tank_missiel_image_l[0] = 0
      tank_missiel_image_l[1] = 0
#	------- JET HIT BY MISSIEL -----
    if ((missiel_1_on_jet > 0 and missiel_1_on_jet < 50) or (missiel_2_on_jet > 0 and missiel_2_on_jet < 50) or (bullet_on_jet > 0 and bullet_on_jet < 50) ) and hit_jet== True and (level_3 or level_4):
          score += 1
          jet_shoot_l[0] += 1
          car_explosion(rand_jet_x, rand_jet_y)
          rand_jet_x = 0
          rand_jet_y =  int(random.randint(10, 200))
          
          car_explode_sound_0.play()
          
      
      # ADD HIT SOUND
    
    #hit by tank bullet 
    hit_distance = int(math.sqrt((turtlex-bulletx)**2 + (turtley-bullety)**2))
    
    if (hit_distance >= 0 and hit_distance <=50) or (missiel_1_on_target>= 0 and missiel_1_on_target <=50) or (missiel_2_on_target>= 0 and missiel_2_on_target <=50):
      scored = True
      
      explode_coordinate.append(turtlex)
      explode_coordinate.append(turtley)
      
      turtlex = int(random.randint(0,600))
      turtley = 20
      score_clock = pygame.time.get_ticks()
    else:			
    # record SCORE
      if scored == True and life != 0 and not game_over:
           score += 1
           turtle_shoot_l[0] += 1
           blast = True
           car_explode_sound_0.play()
        
      scored = False
      
      if current_time - score_clock < 300:
        explode = True
        
      else:
        explode = False
        
      if explode == True:
#---------------------------------------------------
        car_explosion(explode_coordinate[0], explode_coordinate[1])
#---------------------------------------------------
      else:
        explode_coordinate.clear() # clear  the list so that we can add new collision coordinatex
      
    # CODE TO REDUCE THE HEARTS
    for i in range(5):
      if life == i:
        show_hearts_l[i] = False
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
      
      if not game_over:
        record_high_score(scorer_name,score)
      game_over = True
      saved_battery_coord_l[0] = 0
      saved_battery_coord_l[1] = 0
      level[0] = 0
      
      for i in range(5):
        show_hearts_l[i] = False
      
  #---------------------------------------------------
    show_hearts()	
  #---------------------------------------------------

#--------------------------------------------------
    tank_fire(batteryx, batteryy)
#--------------------------------------------------
    
    #missiel()
    if not fired_missiel:
      left_missiel_x =  missiel_x- 40
      right_missiel_x =  missiel_x + 30
      
    if weapon_upgraded_l[0] == 1 or weapon_upgraded_l[0] == 0:
      
      if fired_missiel:
          
        left_missiel_x =  const_missiel_x[0] - area_of_destruction_l[0]
        right_missiel_x =  const_missiel_x[0] + area_of_destruction_l[0]
        
        if left_missiel_x <= 0:
          left_missiel_x = 5
        if right_missiel_x > 600:
          right_missiel_x = 630
          
#--------------------------------------------------
    fire_missiel_2nd(left_missiel_x, right_missiel_x,missiel_y)
#--------------------------------------------------
    # record high score when game ends
    
    scorer_name = ""
    #player_name_l.remove(player_name_l[len(player_name_l) - 1])
    for j in range(len(player_name_l) ):
      scorer_name += player_name_l[j]
    #if game_over and not running
#--------------------------------------------------		
    #WHEN HIT BY CAR  BLIT EXPLOSION ABOVE TANK		 
    if current_time - hit_time[0] < 200:
  
          explode_tank(batteryx, batteryy)
    #WHEN HIT BY MISSIEL  BLIT EXPLOSION ABOVE TANK		 			
    if current_time - hit_by_tank_time  < 200:
      explode_tank_2(batteryx,batteryy)
    #WHEN HIT BY MISSIEL  BLIT EXPLOSION ABOVE JET FOR 1 SEC				
    if current_time - hit_by_jet_time < 800:
          explode_jet(saved_jet_coord_l[0], saved_jet_coord_l[1])
    else:
      saved_jet_coord_l.clear()
      saved_jet_coord_l = [900,900]
      
    display_high_score(600, 600)
    game_life(life, score,level[0])
    player()
    
    #display_result(saved_jet_coord_l[0],saved_jet_coord_l[1])
    
    show_game_data()
    show_statistics()
    
  #	display_result(batteryx,batteryy)
#--------------------------------------------------
    
    pygame.display.update()
  


    
  

      
  

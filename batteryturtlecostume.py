import pygame
import math
import time
import random
pygame.init()
battery_l = []
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("thomas kitaba")
running = True

velocity = 5
forward = 0
backward = 0
battery_index = 0
battery_step = 0
t_b = 80
life = 10

up = 0
down = 0

turtleimg0= pygame.image.load("turtle.png")
turtlex = 300
turtley = 0


batyeryimg = []
batteryimg= [pygame.image.load('battery1.png'), pygame.image.load('battery2.png')]
batteryx = 245 
batteryy = 550

battery_l.append(pygame.transform.scale(batteryimg[0],(80,80)))
battery_l.append(pygame.transform.scale(batteryimg[1],(80,80)))

def turtle(m,n,t):
  turtle = pygame.transform.scale(turtleimg0, (80,t_b))
  screen.blit(turtle,(turtlex,turtley))
  

def battery (x,y,i):
      screen.blit(battery_l[i],(batteryx,batteryy))

            
def game_score(s):
  s = str(s)

  myfont = pygame.font.SysFont("Comic Sans MS", 100)
# apply it to text on a label
  lable = myfont.render('LIFE:', 4, (0,130,120))
# put the label object on the screen at point x=100, 
  myscore = myfont.render(s,1,(0,0,0))
  
  screen.blit(lable, (100, 0))	
  screen.blit(myscore,(160,50))   
running = True
while running:
  screen.fill((205,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  #battery(batteryx,batteryy,battery_index)
  
  # HORIZONTAL MOVEMENT
  
  if batteryx < 600 and forward == 1:
    batteryx += 1
    battery_step += 1 # costume change 
    battery_index =1
    
  else:
    forward = 0
    backward = 1
    #battery_index = 0
    
  if batteryx > 0 and backward == 1 :
    
    batteryx -= 1
    battery_step += 1
    
  else:
    forward = 1
    backward = 0
    #batteryy -= 1
  
  # VERTICAL MOVEMENT
  
  if turtley < 600 and down == 1:
    
    turtley += 6
  else:
    up = 1
    down = 0
    
    
  if turtley > 0 and up == 1:
    turtley -= 6
  else:
    up = 0
    down = 1

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

# check collision

  d = int(math.sqrt((turtlex-batteryx)**2 + (turtley-batteryy)**2))
  
  if d > 100:
      turtle(turtlex, turtley,t_b)		
  else:
      life -= 1
      turtlex = int(random.randint(0,600))
      turtley = 20
      #t_b = 300 # bleeding tirtle
  game_score(life)
      
  if life == 0:
    running = False
    
    
  
  pygame.display.update()
  

import pygame 

from pygame import Color, draw, display, time 


# constant Variables 

SCREEN_WIDTH = 600 
SCREEN_HEIGHT = 400 
RADIUS = 30 

# postion of Ball 

center_x = 250 
center_y = 250 

# Direction of ball 

horizontal_pixle_movement = 1
vertical_pixle_movement = 1 

# Inilialize pygame modules 

pygame.init()
clock = time.Clock()

# Get surface for graphics display 

gameDisplay = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True: 
    # set white background 
    gameDisplay.fill(Color('white'))
    # draw ball 
    draw.circle(gameDisplay, Color('purple'), (center_x, center_y), RADIUS)
    
    # show graphics on display 
    display.flip()
   
   # check if edge touches sides, change direction 
    if center_x + RADIUS > SCREEN_WIDTH or center_y - RADIUS < 0:
     horizontal_pixle_movement = -horizontal_pixle_movment  
  
    if center_x + RADIUS > SCREEN_HEIGHT or center_y - RADIUS < 0:
       vertical_pixle_movement = -vertical_pixle_movement 
   
    
    center_x = center_x + 1 
    center_y = center_y + 1 
    clock.tick(45)
    
    
    

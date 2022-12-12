# Import pygame and pygame objects 
import pygame 
from pygame import Color, draw, display, time 


# variables 

center_ball_x = 50 
center_ball_y = 50 

# Initialize pygame modules 

pygame.init()

# create a clock to delay loop 
clock = time.Clock()

# create a surface to display objects 
gameDisplay = display.set_mode((600, 400))


while True: 
    # Make white background 
    gameDisplay.fill(Color('white'))
    
    #draw a ball 
    draw.circle(gameDisplay, Color('purple'), (center_ball_x, center_ball_y), 30)
    # change location of ball 
    center_ball_y = center_ball_y + 80
    center_ball_x = center_ball_x + 45
    # Delay the program 
    clock.tick(45)
    
    
    # show graphics on display 
    display.flip()

# wait for user input before cosing window 
#input("press key to exit")
# Uninitialize pygame 
#pygame.quit()
# exit python 
#quit()
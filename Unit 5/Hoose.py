import pygame 
from pygame import display 
from pygame import Color 
from pygame import Rect 
from pygame import draw 


# initialize pygame modules 
pygame.init()

# dimension of the window frame 
SIZE = (500,500)

# get a surface for graphics display 
gameDisplay = display.set_mode(SIZE)
# set background - color of the sky 
gameDisplay.fill(Color('lightblue'))
# Draw a house bttom 
draw.rect(gameDisplay, Color('brown'), Rect(100, 200, 300, 200))
# Draw a roof
point1 = (100, 200)
point2 = (400, 200)
point3 = (250, 50)
draw.polygon(gameDisplay, Color('black'), [point1, point2, point3])
# draw a sun 
centerCircle = (50, 50)
radius = 50 
draw.circle(gameDisplay, Color('yellow'), centerCircle, radius)
# draw grass 
draw.rect(gameDisplay, Color('green'), Rect(0, 400, 500, 100))


# show the gameDisplay on the screen 
display .flip()

# wait for user input before closing window 
input("Press enter to exit game.")

# Uninitilaize pygame 
pygame.quit()

#Exit Python 
quit()
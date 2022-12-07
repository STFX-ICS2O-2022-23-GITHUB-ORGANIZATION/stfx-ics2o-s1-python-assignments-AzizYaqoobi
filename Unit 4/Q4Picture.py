import pygame 
from pygame import display 
from pygame import Color 
from pygame import Rect 
from pygame import draw 

pygame.init()

SIZE = (500,500)

gameDisplay = display.set_mode(SIZE)

gameDisplay.fill(Color('lightblue'))

draw.rect(gameDisplay, Color('coral4'), Rect(150, 300, 300, 200))

point1 = (300, 300)
point2 = (400, 300)
point3 = (150, 50)
draw.polygon(gameDisplay, Color('gray100'), [point1, point2, point3])

centerCircle = (50, 50)
radius = 50 
draw.circle(gameDisplay, Color('yellow'), centerCircle, radius)

draw.rect(gameDisplay, Color('dodgerblue2'), Rect(0, 400, 500, 100))

display .flip()

input("Press enter to exit game.")

pygame.quit()

quit()
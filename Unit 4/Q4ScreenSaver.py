import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
screen_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(screen_size)

# Set the title of the window
pygame.display.set_caption("Screensaver")

# Set the background color
bg_color = (0, 0, 0)

# Create a list to store the circles
circles = []

# Create a number of circles and add them to the list
for i in range(10):
    x = random.randint(0, screen_size[0])
    y = random.randint(0, screen_size[1])
    radius = random.randint(10, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    circles.append((x, y, radius, color))

# Set the speed of the circles
speed = 2

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the circles
    for i, (x, y, radius, color) in enumerate(circles):
        x += random.randint(-speed, speed)
        y += random.randint(-speed, speed)

        # Keep the circles within the screen
        if x - radius < 0:
            x = radius
        elif x + radius > screen_size[0]:
            x = screen_size[0] - radius
        if y - radius < 0:
            y = radius
        elif y + radius > screen_size[1]:
            y = screen_size[1] - radius

        # Update the position of the circle
        circles[i] = (x, y, radius, color)

    # Draw the circles
    screen.fill(bg_color)
    for x, y, radius, color in circles:
        pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()

# Quit pygame
pygame.quit()

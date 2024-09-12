import pygame
import math
import random
# import pygame from mixer

# Initalise pygame
pygame.init()

# Create screen - using standard width and height
res = (800, 600)

screen = pygame.display.set_mode(res)


# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
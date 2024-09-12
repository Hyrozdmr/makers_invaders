import pygame
import math
import random
# import pygame from mixer

# Initalise pygame
pygame.init()

# Create screen - using standard width and height
res = (800, 600)

screen = pygame.display.set_mode(res)

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

start_button_rect = pygame.Rect(300, 250, 200, 100)

# Define the game states
MAIN_MENU = 0
GAMEPLAY = 1
game_state = MAIN_MENU


# Variable to keep our game loop running 
running = True
   
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == MAIN_MENU:
                # Check if the user clicked on the start button
                if start_button_rect.collidepoint(event.pos):
                    game_state = GAMEPLAY  # Transition to the gameplay screen
    # Check current game state
    if game_state == MAIN_MENU:
        # Draw the start button (a simple blue rectangle)
        pygame.draw.rect(screen, BLUE, start_button_rect)

    elif game_state == GAMEPLAY:
    # Clear the screen with a new color to indicate the new screen
        screen.fill((0, 100, 200))

            # Add some text for the button
        font = pygame.font.Font(None, 74)
        text = font.render("START", True, WHITE)
        screen.blit(text, (start_button_rect.x + 40, start_button_rect.y + 20))
        # Update the display
    pygame.display.flip()


# Create a surface for the button
button_surface = pygame.Surface((150, 50))


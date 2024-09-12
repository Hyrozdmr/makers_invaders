import pygame
import pygame.freetype
import subprocess

# Initalise pygame
pygame.init()

# Define the background image
background = pygame.image.load("data/background.png")

# Create screen - using standard width and height
res = (800, 600)
screen = pygame.display.set_mode(res)

# Set the title of the screen 
pygame.display.set_caption('Title') 

# Initalise font module
pygame.font.init()

# Create a font object and render text for the main menu
font = pygame.font.Font('freesansbold.ttf', 80)
text = font.render('Makers Invaders', False, (255, 255, 25))

# Load the start button image and get its rect
img = pygame.image.load('data/start_button.png').convert_alpha()
start_button_rect = img.get_rect(topleft=(270, 300))

# Set the size for the image
DEFAULT_IMAGE_SIZE = (250, 100)
img = pygame.transform.scale(img, DEFAULT_IMAGE_SIZE)

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define the game states
MAIN_MENU = 0
GAMEPLAY = 1
game_state = MAIN_MENU

# Variable to keep our game loop running
running = True

# Main game loop
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN and game_state == MAIN_MENU:
            # Check if the user clicked on the start button
            if start_button_rect.collidepoint(event.pos):
                # game_state = GAMEPLAY  # Transition to the gameplay screen
                subprocess.run(['python', 'game.py'])
                running = False  # Close the main menu after launching gameplay

    # Check the current game state
    if game_state == MAIN_MENU:
        # Draw the main menu screen
        screen.blit(background, (0, 0))
        screen.blit(text, (85, 200))
        screen.blit(img, start_button_rect)
    
    elif game_state == GAMEPLAY:
        # Clear the screen with a new color to indicate the new screen
        screen.fill((0, 100, 200))
        
        # Add some text for the gameplay screen
        font = pygame.font.Font(None, 74)
        gameplay_text = font.render("GAMEPLAY", True, WHITE)
        screen.blit(gameplay_text, (250, 250))

    # Update the display
    pygame.display.flip()
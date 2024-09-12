import pygame
import pygame.freetype

# Define the background colour 
# using RGB color coding. 
# background_colour = (255, 255, 255) 
background = pygame.image.load("data/background.png")

# Initalise pygame
pygame.init()

# Create screen - using standard width and height
res = (800, 600)

screen = pygame.display.set_mode(res)

# Fill the background colour to the screen 
# screen.fill(background_colour) 

# Set the title of the screen 
pygame.display.set_caption('Title') 

#Initalise font module
pygame.font.init()

# create a font object.
font = pygame.font.Font('freesansbold.ttf', 80)

# create a text surface object,
# on which text is drawn on it.
text = font.render('Makers Invaders', False, (255, 255, 255))

img = pygame.image.load('data/start_button.png').convert_alpha()

# Set the size for the image
DEFAULT_IMAGE_SIZE = (250, 100)
 
# Scale the image to your needed size
img = pygame.transform.scale(img, DEFAULT_IMAGE_SIZE)

class Button:
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback
 
    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback(self)
 
# # Define and create button
# button = Button(your_image, (10, 10), push_button_goodbye)
# # In event loop. Under pygame.MOUSEBUTTONDOWN.
# button.on_click(event)
# In main loop draw area.

screen.blit(background, (0,0))

screen.blit(text, (85,200))

screen.blit(img, (270,300))

# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
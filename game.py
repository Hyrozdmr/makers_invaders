import pygame
import math
import random
# import pygame from mixer

# Initalise pygame
pygame.init()

# Create screen - using standard width and height
res = (800, 600)

screen = pygame.display.set_mode(res)

# caption and icon 
pygame.display.set_caption("Space Invaders Game")

# score 
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 32)

# game over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("points: " + str(score_val), True,(255,255,255))
    screen.blit(score, (x, y ))

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_text, (190, 250))

# Background sound 
mixer.music.load('data/background.wav')
mixer.music.play(-1)

# background image
background = pygame.image.load('data/background.png')

# player
playerImage = pygame.image.load('data/spaceship.png')
player_X = 370
player_Y = 523
player_Xchange = 0
player_Ychange = 0 # Vertical movement

# Invader
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load('data/alien.png'))
    invader_X.append(random.randint(64, 737))
    invader_Y.append(random.randint(30, 180))
    invader_Xchange.append(2)
    invader_Ychange.append(40)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = pygame.image.load('data/bullet.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 6 # bullet speed
bullet_state = "rest"
 
# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) +
                         (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False
 
def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))
 
def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))
 
def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"
 
# game loop
running = True
while running:

    # Control frame rate (FPS)
    clock.tick(60)


    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        # Controlling the player movement
        # from the arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -3.5 # player speed
            if event.key == pygame.K_RIGHT:
                player_Xchange = 3.5
            if event.key == pygame.K_DOWN:
                player_Ychange = 3.5
            if event.key == pygame.K_UP:
                player_Ychange = -3.5
            if event.key == pygame.K_SPACE:
               
                # Fixing the change of direction of bullet
                if bullet_state == "rest":
                    bullet_X = player_X
                    bullet(bullet_X, bullet_Y)
                    bullet_sound = mixer.Sound('data/bullet.wav')
                    bullet_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_Xchange = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_Ychange = 0
 
    # adding the change in the player position
    player_X += player_Xchange
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]
    
     # Update player position
    player_X += player_Xchange
    player_Y += player_Ychange

    # Restrict player movement within screen boundaries
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750
    if player_Y <= 0:
        player_Y = 0
    elif player_Y >= 550:
        player_Y = 550

    # bullet movement
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange
 
    # movement of the invader
    for i in range(no_of_invaders):
         
        if invader_Y[i] >= 450:
            if abs(player_X-invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    # explosion_sound = mixer.Sound('data/explosion.wav')
                    # explosion_sound.play()
                game_over()
                break

  # Change direction of invaders when they hit the screen boundary
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]

        # Collision
        collision = isCollision(bullet_X, invader_X[i],
                                bullet_Y, invader_Y[i])
        if collision:
            score_val += 1
            bullet_Y = 600
            bullet_state = "rest"
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            invader_Xchange[i] *= -1
 
        invader(invader_X[i], invader_Y[i], i)
 
 
    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    pygame.display.update()

    # Update the screen
    pygame.display.update()
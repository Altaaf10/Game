# Task 15

import pygame # Imports pygame module from Python
import random # Imports random module from Python

pygame.init() # Initialize the pygame modules 

# Sets a width and a height for screen that will be created 
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # Creates Screen

# Creates Characters
player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.jpg")
pacman = pygame.image.load("pacman.jpg")
monster = pygame.image.load("monster.jpg")

# Creates width and height of the images
image_height = player.get_height()
image_width =player.get_width()
enemy_heigth = enemy.get_height()
enemy_width = enemy.get_width()
prize_width = prize.get_width()
prize_height = prize.get_height()
pacman_height = pacman.get_height()
pacman_width = pacman.get_width()
monster_height = monster.get_height()
monster_width = monster.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: "+str(image_width))
print("This is the height of the enemy image: " +str(enemy_heigth))
print("This is the width of the enemy image: "+str(enemy_width))

# Store the positions of the characters
playerXPosition = 100
playerYPosition = 50

enemyXPosition = random.randint(0,screen_width)
enemyYPosition = random.randint(0, screen_height - enemy_heigth)

prizeXPosition = random.randint(0,screen_width)
prizeYPosition = random.randint (0, screen_height - prize_height)

pacmanXPosition = screen_width
pacmanYPosition = random.randint (0, screen_height - pacman_height)

monsterXPosition = screen_width
monsterYPosition = random.randint(0, screen_height - monster_height)

#Set variables as False for later use with key arrows
keyUp = False
keyDown = False
keyRight = False
keyLeft = False

# Loop
while 1:#while loop is True
    screen.fill(0) # Clear the screen
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    screen.blit(pacman, (pacmanXPosition, pacmanYPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    
    pygame.display.flip()# Updates screen

    # Event Loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:# Exit program if user exits program
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN: #if statement to see if the corresponding key is held down

            if event.key == pygame.K_UP:# Checks if user presss the up arrow
                keyUp = True
            if event.key == pygame.K_DOWN:# Checks if user presss the down arrow
                keyDown = True
            if event.key == pygame.K_RIGHT:# Checks if user presss the right arrow
                keyRight = True
            if event.key == pygame.K_LEFT:# Checks if user presss the left arrow
                keyLeft = True
                
        if event.type == pygame.KEYUP:#if statement to see if the corresponding key is released

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1# Prevents the player from going above the screen

    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1# Prevents the player from going below the screen

    if keyRight == True:
        if playerXPosition > 0:
            playerXPosition += 1# Prevents the player from going beyond the screen width when going left
            
    if keyLeft == True:
        if playerXPosition  < screen_width - image_width:
            playerXPosition -= 1 # Prevents the player from going beyond the screen width when going left
            
    # Create Box

    playerBox = pygame.Rect(player.get_rect())


    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    prizeBox = pygame.Rect(enemy.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    pacmanBox = pygame.Rect(pacman.get_rect())
    pacmanBox.top = pacmanYPosition
    pacmanBox.left = pacmanXPosition

    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition
# Check for collision between Boxes

    if playerBox.colliderect(enemyBox):

        print("You lose!")

        pygame.quit()
        exit(0)

    if enemyXPosition < 0 - enemy_width:

        print("You Win!")

        pygame.quit()
        exit(0)
        
    if playerBox.colliderect (prizeBox):

        print("You Win!")

        pygame.quit()
        exit(0)

    if playerBox.colliderect(pacmanBox):
        print ("You Lose!")

        pygame.quit()
        exit(0)

    if pacmanXPosition < 0 - pacman_width:
        print("You Win!")

        pygame.quit()
        exit(0)

    if playerBox.colliderect(monsterBox):
        print("You Lose!")

        pygame.quit()
        exit(0)

    if monsterXPosition < 0 - monster_width:
        print("You Win!")

        pygame.quit()
        exit(0)

        #Move rest of characters

    enemyXPosition -= 0.15
    enemyYPosition -= random.uniform(-.15,0.15)
    prizeXPosition -= 0.15
    pacmanXPosition -= 0.15
    monsterXPosition -= 0.15

        


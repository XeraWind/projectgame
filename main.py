import pygame
import time



pygame.init()

# Time
deltaTime = (0.1)


# This is display
screen = pygame.display.set_mode((480, 360))


# This is display (title, icon)
pygame.display.set_caption("Jet Run")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)


# This is the player img
playerImg = pygame.image.load('assets/Individual-Jet-Sprites/Blue_Jet.png')
playerX = 230
playerY = 280



def player():
    screen.blit(playerImg, (playerX, playerY))



running = True
while running:
    screen.fill((0, 0 ,0))
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    

    player()
    pygame.display.update()


    

   
   
   

    

import pygame, os, sys
from pygame.locals import *
pygame.init
humanimage = pygame.image.load("images/human1.png")

#Create the screen.
size = (400,600)
screen = pygame.display.set_mode(size)
#Create a background
background = pygame.Surface(size)
background.fill((66, 0, 66))

done = False
while not done:
	#Draw the background
    screen.blit(background, (0, 0))
    screen.blit(humanimage, (50, 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()
        elif event.type == KEYDOWN:
        	if event.key == K_ESCAPE:
        		pygame.quit()
        		



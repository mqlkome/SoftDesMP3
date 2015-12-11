import pygame
from pygame.locals import *

class PyGameWindowView:
    ##Render our starting screen
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        ##Draw the background
        self.model.background.draw(self.screen)
        ##Draw the player
        self.model.player.draw(self.screen)
        
        ##Draw the ground
        pygame.draw.rect(self.screen, pygame.Color(self.model.ground.color[0],self.model.ground.color[1],self.model.ground.color[2]),pygame.Rect(self.model.ground.x,self.model.ground.y,self.model.ground.width,self.model.ground.height))	 

        ##Draw the sun [change to model draw function] 
        self.screen.blit(self.model.sun.image,(self.model.sun.x,self.model.sun.y))

        ##Draw the obstacle[change to model draw function]
        self.model.obstacle.draw(self.screen)
        
        ##Draw the item
        self.model.item.draw(self.screen)
        
        pygame.display.update()

    def show(self, picture):
        picture.draw(self.screen)
        pygame.display.update()

    def show_popup(self, popup):
        self.screen.blit(pygame.image.load(popup), (200,100))

    def show_speech(self, bubble):
        self.screen.blit(pygame.image.load(bubble), (540, 50))


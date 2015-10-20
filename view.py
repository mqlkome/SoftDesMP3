# -*- coding: utf-8 -*-
"""


@author: Jake, Mimi
"""


import pygame
from pygame.locals import *



class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen

        
    def draw(self):
        
        pygame.draw.rect(self.screen, pygame.Color(self.model.ground.color[0],self.model.ground.color[1],self.model.ground.color[2]),pygame.Rect(self.model.ground.x,self.model.ground.y,self.model.ground.width,self.model.ground.height))     
        self.screen.blit(self.model.sun.image,(self.model.sun.x,self.model.sun.y))
        pygame.display.update()


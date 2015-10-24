# -*- coding: utf-8 -*-
"""


@author: Jake, Mimi
"""


import pygame
from pygame.locals import *
import sys


class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen

        
    def draw(self):
        
        pygame.draw.rect(self.screen, pygame.Color(self.model.ground.color[0],self.model.ground.color[1],self.model.ground.color[2]),pygame.Rect(self.model.ground.x,self.model.ground.y,self.model.ground.width,self.model.ground.height))     
        self.screen.blit(self.model.sun.image,(self.model.sun.x,self.model.sun.y))
        self.screen.blit(self.model.player.image,(self.model.player.x,self.model.player.y))

       
        self.screen.blit(self.model.obstacle.image,(self.model.obstacle.x,self.model.obstacle.y))
        self.screen.blit(self.model.item.image,(self.model.item.x,self.model.item.y))


        pygame.display.update()

    def show_popup(self):
        self.screen.blit(self.model.popup.image,(self.model.popup.x,self.model.popup.y))


    def make_popup(self):

        BASICFONT=pygame.font.SysFont(None,42)
        width=100
        height=70
        popupSurf = pygame.Surface((width, height))
        options = ['Attack', 'Talk', 'Item']

        for i in range(len(options)):

            textSurf = BASICFONT.render(options[i], 1,(0,0,255))
            textRect = textSurf.get_rect()
            
            #textRect.top=popupSurf.height
            
            textRect.top += pygame.font.Font.get_linesize(BASICFONT)
            popupSurf.fill((255,0,0))
            popupSurf.blit(textSurf, textRect)
        

            # for i in range(len(options)):
            #     textSurf = BASICFONT.render(options[i], 1,(0,0,255))
            #     textRect = textSurf.get_rect()
            #     textRect.top = self.top
            #     textRect.left = self.left
            #     self.top += pygame.font.Font.get_linesize(BASICFONT)
            #     popupSurf.blit(textSurf, textRect)
            popupRect = popupSurf.get_rect()
            popupRect.centerx = 500#SCREENWIDTH/2
            popupRect.centery = 150 + 80*i#SCREENHEIGHT/2
            self.screen.blit(popupSurf, popupRect)
            pygame.display.update()

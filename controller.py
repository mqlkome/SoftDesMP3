# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 2015

@author: Amon Millner, building upon Paul Ruvolo’s Spring 2014 SoftDes example
"""


import pygame
from pygame.locals import *

class PyGameMouseController:
    def __init__(self,model):
        self.model = model
    
    def handle_mouse_event(self,event):
        if event.type == MOUSEMOTION:
            self.model.paddle.x = event.pos[0] - self.model.paddle.width/2.0


class PyGameKeyboardController:
    def __init__(self,model):
        self.model = model

    def handle_key_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == K_ESCAPE:
            pygame.quit()
        if event.key == pygame.K_LEFT:
            self.model.player.x += -30
        if event.key == pygame.K_RIGHT:
            self.model.player.x += 30
        ##if popup comes out
        ## press a to attack
        
        # if event.key ==pygame.K_a:
        #     view.rspgame #rock scissor paper game
        # if event.key==pygame.K_i:
        #     # you used the wrong item





# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 2015
@author: Jake and Mimi, building upon Amon Millner's, building upon Paul Ruvolo’s Spring 2014 SoftDes example
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
            self.model.player.moveleft()
        if event.key == pygame.K_RIGHT:
            self.model.player.moveright()


# -*- coding: utf-8 -*-
"""


@author: Jake, Mimi
"""


import pygame
from pygame.locals import *


green1=(77,153,0)

class MapsolvingModel:
    """ Encodes the game state """
    def __init__(self):
        # self.bricks = []
        # for x in range(20,620,150):
        #     brick = Brick((0,255,0),20,100,x,120)
        #     self.bricks.append(brick)
        self.ground = Ground(green1,140,640,0,360)
        #self.ground=Sun()
class Ground:
    """ Encodes the state of a brick in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Sun:
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y


class Obstacles:
    """ Encodes the state of the paddle in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Items:
    """ Encodes the state of the paddle in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y




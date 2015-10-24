# -*- coding: utf-8 -*-
"""


@author: Jake, Mimi
"""


import pygame
from pygame.locals import *


green1=(77,153,0)

# pop-up menu

class MapsolvingModel:
    """ Encodes the game state """
    def __init__(self):
        # self.bricks = []
        # for x in range(20,620,150):
        #     brick = Brick((0,255,0),20,100,x,120)
        #     self.bricks.append(brick)
        self.ground = Ground(green1,140,640,0,360)
        self.sun=Sun(540,20)
        self.player=Player(0,204,0)
        self.obstacle=Obstacle(550,200,1)
        self.item=Item(220,280,1)
        self.popup=Popup(400,150)


class Ground:
    """ Encodes the state of a brick in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

# player class , don't know how to randomly generate the player charactor
# now, just do it with view-->randint
class Player:
    def __init__(self,x,y,assign_int):
        players=["images/human1.png", "images/human2.PNG"]
        self.assign_int=assign_int
        self.image=pygame.image.load(players[self.assign_int])
        #player's default position
        self.x = x
        self.y = y

class Obstacle:
    def __init__(self,x,y,assign_int):
        obstacles=["images/tree.PNG","images/bug.png","images/cat.PNG"]
        
        ##Use to generate random numbers
        self.assign_int=assign_int
        print self.assign_int
        self.image=pygame.image.load(obstacles[self.assign_int])
        print self.image
        self.x = x
        self.y = y


class Sun:
    def __init__(self,x,y):
        self.image=pygame.image.load("images/sun.png")
        
        self.x = x
        self.y = y


class Item:
    """ Encodes the state of the paddle in the game """
    def __init__(self,x,y,assign_int):
        items=["images/camera.png","images/eggplant.png","images/flower.png","images/mushroom.png","images/mysteriousblueorb.png","images/sword.png"]
        
        ##Use to generate random numbers
        self.assign_int=assign_int
        self.image=pygame.image.load(items[assign_int])
        #player's default position
        self.x = x
        self.y = y

class Popup:

    def __init__(self,x,y):
        popups=["images/popup.png"]
        
        
        self.image=pygame.image.load(popups[0])
        #player's default position
        self.x = x
        self.y = y


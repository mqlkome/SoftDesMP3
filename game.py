# -*- coding: utf-8 -*-
"""
Created on Oct 19, 2015

@author: Jake, Mimi
"""

import pygame
from pygame.locals import *
import os, sys

import model
from model import *
import view
from view import *
import random
from random import randint
import math
import time

class Player(pygame.sprite.Sprite):  
    def __init__(self):
        #choose and load a random player
        pygame.sprite.Sprite.__init__(self)
        players=["images/person1anim.gif", "images/human2.PNG"]
        self.image = pygame.image.load(players[randint(0,1)])
        self.xposition = 0
        #self.rect = self.image.get_rect()
        #self.rect = self.rect.move(some_position)

    def moveright(self):
        self.xposition += 20
    def moveleft(self):
        self.xposition += -20

    def draw(self, screen):
        screen.blit(self.image, (self.xposition,204))
    
class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        items=["images/camera.png","images/eggplant.png","images/flower.png","images/mushroom.png","images/mysteriousblueorb.png","images/sword.png"]
        self.image = pygame.image.load(items[randint(0,5)])
        #self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image,(220,280))
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        obstacles=["images/tree.PNG","images/bug.png","images/cat.PNG"]
        self.image = pygame.image.load(obstacles[randint(0,2)])
        #self.rect = self.image.get_rect()
    def draw(self, screen):
        screen1.blit(self.image,(550,200))

class Princess(pygame.sprite.Sprite):
    def __init__(self):
        pass

if __name__ == '__main__':
    #initialize pygame
    pygame.init()

    #create a screen of some "size" and load background
    size = (640,480)
    screen1 = pygame.display.set_mode(size)
    background=pygame.image.load("image2.jpg").convert()
    sun=pygame.image.load("images/sun.png")

    #load the sprites and put them in groups
    player = Player()
    players = pygame.sprite.Group()
    players.add(player)

    item = Item()
    items = pygame.sprite.Group()
    items.add(item)

    obstacle = Obstacle()
    obstacles = pygame.sprite.Group()
    obstacles.add(obstacle)


    #instantiate the model and view classes
    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)

    # we didn't include the controller yet
    #controller = PyGameMouseController(model)
    #controller = PyGameKeyboardController(model)

    running = True
    while running:
        screen1.blit(background,(0,0))
        player.draw(screen1)
        item.draw(screen1)
        obstacle.draw(screen1)
        screen1.blit(sun,(540,20))

        # if pygame.sprite.spritecollide(players, items):
        #     print "you found an item!"
           
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                #controls
                if event.key == K_RIGHT:
                    player.moveright()
                if event.key == K_LEFT:
                    player.moveleft()
              
#            if event.type == MOUSEMOTION:
#                controller.handle_mouse_event(event)


        view.draw()
        time.sleep(.001)
    sys.exit()
    pygame.quit()

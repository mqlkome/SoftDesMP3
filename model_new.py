# -*- coding: utf-8 -*-

"""





@author: Jake, Mimi

"""



from random import randint

import pygame

from pygame.locals import *





green1=(77,153,0)



class MapsolvingModel:

    """ Encodes the game state """

    def __init__(self):

        # self.bricks = []

        # for x in range(20,620,150):

        # 	brick = Brick((0,255,0),20,100,x,120)

        # 	self.bricks.append(brick)

        self.ground = Ground(green1,140,640,0,360)

        self.sun=Sun(540,20)

        self.player=Player(0,204)

        self.obstacle=Obstacle(550,200,1)

        self.item=Item(220,280,1)
        self.attack=Attack(200,100)

        self.popup=Popup(400,100)

        ###making rockscissorpaper class
        self.rock=Rockscissorpaper(400,100,0)
        self.scissor=Rockscissorpaper(400,100,1)
        self.paper=Rockscissorpaper(400,100,2)

        ##making obstacles's rockscissorpaper class
        self.rock_obs=Rockscissorpaper_obs(520,100,0)
        self.scissor_obs=Rockscissorpaper_obs(520,100,1)
        self.paper_obs=Rockscissorpaper_obs(520,100,2)

class Ground:

    """ Encodes the state of a brick in the game """

    def __init__(self,color,height,width,x,y):

        self.color = color

        self.height = height

        self.width = width

        self.x = x

        self.y = y



class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):

        pygame.sprite.Sprite.__init__(self)

        players=["images/human1.png", "images/human2.PNG"]

        self.image = pygame.image.load(players[randint(0,1)])

        self.xposition = x

        self.yposition=y

        self.rect = self.image.get_rect()

        self.rect.x = self.xposition

        self.rect.y = y



    def moveright(self):

        self.previousx = self.xposition

        self.xposition += 30

        self.rect.x = self.xposition



    def moveleft(self):

        self.previousx = self.xposition

        self.xposition += -30

        self.rect.x = self.xposition

   	 

    def draw(self, screen):

        screen.blit(self.image, (self.xposition,self.yposition))    









#self.assign_int=assign_int

    	#self.image=pygame.image.load(players[self.assign_int])

    	#player's default position









class Princess(pygame.sprite.Sprite):

    def __init__(self):

        pass







class Obstacle(pygame.sprite.Sprite):

    def __init__(self,x,y,assign_int):

        pygame.sprite.Sprite.__init__(self)

        obstacles=["images/tree.PNG","images/bug.png","images/cat.PNG"]

         

        ##Use to generate random numbers

        self.assign_int=assign_int

         

        self.image=pygame.image.load(obstacles[self.assign_int])

        self.x = x

        self.y = y

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y



    def draw(self, screen):

        screen1.blit(self.image,(self.x,self.y))



class Sun:

    def __init__(self,x,y):

        self.image=pygame.image.load("images/sun.png")

         

        self.x = x

        self.y = y





class Item(pygame.sprite.Sprite):

    def __init__(self,x,y,assign_int):

        pygame.sprite.Sprite.__init__(self)

        items=["images/camera.png","images/eggplant.png","images/flower.png","images/mushroom.png","images/mysteriousblueorb.png","images/sword.png"]





        ##Use to generate random numbers

        self.assign_int=assign_int

        self.image=pygame.image.load(items[assign_int])

        self.x = x

        self.y = y

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

   	 

    def draw(self, screen):

        screen.blit(self.image,(self.x,self.y))   

###from here newthings comeout
class Attack(pygame.sprite.Sprite):

    def __init__(self,x,y):

        

        attacks=["images/rps.jpg"]

     

        ##Use to generate random numbers

        

        self.image=pygame.image.load(attacks[0])

        self.x = x

        self.y = y

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))   

        



class Popup:



    def __init__(self,x,y):

        popups=["images/popup_obstacle.png"]

        self.image=pygame.image.load(popups[0])

        self.x = x

        self.y = y

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))  

class Rockscissorpaper:

    def __init__(self,x,y,assign_int):

       

        rsp=["images/rock.jpg","images/scissor.jpg","images/paper.jpg"]

         

        ##Use to generate random numbers

        self.assign_int=assign_int

         

        self.image=pygame.image.load(rsp[self.assign_int])

        self.x = x

        self.y = y


    def draw(self, screen):

        screen.blit(self.image, (self.x,self.y))   

class Rockscissorpaper_obs:

    def __init__(self,x,y,assign_int):

       

        rsp=["images/rock.jpg","images/scissor.jpg","images/paper.jpg"]

         

        ##Use to generate random numbers

        self.assign_int=assign_int

         

        self.image=pygame.image.load(rsp[self.assign_int])

        self.x = x

        self.y = y


    def draw(self, screen):

        screen.blit(self.image, (self.x,self.y))   


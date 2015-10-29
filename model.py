
from random import randint
import pygame
from pygame.locals import *

##ground color
green1=(77,153,0)

class MapsolvingModel:
    """ Encodes the game state """
    def __init__(self):
        ##call start screen objects, give positions
        self.background=Background(0,0,0)
        self.ground = Ground(green1,140,640,0,360)
        self.sun=Sun(540,20)
        self.player=Player(0,204)
        self.obstacle=Obstacle(550,200,0)
        self.item=Item(220,280,0)
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
        self.counter=1

    def change_background(self):
        self.background=Background(0,0,self.counter)
        self.sun=Sun(540-200*self.counter,10+self.counter/2*20)
    

    def change_item(self):
        self.item=Item(220,280,self.counter)
    def change_player_position(self):
        self.player.xposition=0
        self.player.yposition=204
    def change_obstacle(self):
        #change obstacle and reset position
        #counter goes up in every cycle
        self.obstacle=Obstacle(550,200,self.counter)
        self.counter+=1
    def reset(self):
        # self.item=Item(220,280,0)
        # self.player.xposition=0
        # self.player.yposition=204
        self.counter=0
        self.change_background()
        self.change_item()
        self.change_player_position()
        self.change_obstacle()
    def make_princess(self):
        #place the obstacle out of the screen
        self.obstacle=Obstacle(500,150,self.counter)
        self.background=Background(0,0,self.counter)
        self.sun=Sun(320,5)
        self.change_player_position()
        self.change_item()
        self.counter+=1

class Background:
    def __init__(self,x,y,assign_int):
        
        backgrounds=["images/bluesky.png","images/mountain.png","images/fire.png","images/castle.png"]

        ##Use to load random item
        self.xposition=x
        self.yposition=y
        self.assign_int=assign_int
        self.image=pygame.image.load(backgrounds[assign_int])

    def draw(self, screen):
        screen.blit(self.image, (self.xposition,self.yposition)) 

class Ground:
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
        self.previousx = self.xposition
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
    def stepback(self):
        self.xposition = self.previousx
        self.rect.x = self.xposition
        print "stepback"

    def draw(self, screen):
        screen.blit(self.image, (self.xposition,self.yposition))    


    def pick_up_item(self, player, item):        
        item.x = self.xposition
        item.y = self.yposition - 70
        item.rect.x = item.x
        item.rect.y = item.y

        #self.assign_int=assign_int
    	#self.image=pygame.image.load(players[self.assign_int])
    	#player's default position

class Princess(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        princessimage="images/princess.png"     
        self.image=pygame.image.load(princessimage)

        #Princess position
        
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen1.blit(self.image,(self.x,self.y))

class Obstacle(pygame.sprite.Sprite):
    ###The obstacle characters
    def __init__(self,x,y,assign_int):
        pygame.sprite.Sprite.__init__(self)
        obstacles=["images/tree.PNG","images/bug.png","images/cat.PNG","images/princess.png"]

        ##Use to load random obstacle
        self.assign_int=assign_int
        self.image=pygame.image.load(obstacles[self.assign_int])

        #Obstacle position
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.wanted_item = Item(x,y,randint(0,5))
    def move(self):
        self.x = self.x-2000
        self.rect.x = self.rect.x-2000
                    
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
        
        ##Use to load random item
        self.assign_int=assign_int
        self.image_path = items[assign_int]
        self.image=pygame.image.load(self.image_path)
        
        ##item position
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.x = self.x-2000
        self.rect.x = self.rect.x-2000
   	
    def draw(self, screen):
        screen.blit(self.image,(self.x,self.y))   

class Popup:
    ##When you meet obstacle character, this displays press F or I
    def __init__(self,x,y):
        popups=["images/popup_obstacle.png"]

        self.image=pygame.image.load(popups[0])
        self.x = x
        self.y = y

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y)) 
 
class Attack(pygame.sprite.Sprite):
    ##when you press F, this comes up (Press R,P, or S) 
    def __init__(self,x,y):
        attacks=["images/rps.jpg"]

        ##load and position RSP menu
        self.image=pygame.image.load(attacks[0])
        self.x = x
        self.y = y

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y)) 

class Rockscissorpaper:
    def __init__(self,x,y,assign_int):
        rsp=["images/rock.jpg","images/scissor.jpg","images/paper.jpg"]

        ##load player's pick (r/s/p)
        self.assign_int=assign_int
        self.image=pygame.image.load(rsp[self.assign_int])
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))   

class Rockscissorpaper_obs:
    def __init__(self,x,y,assign_int):
        rsp=["images/rock.jpg","images/scissor.jpg","images/paper.jpg"]

        ##Load computer's pick (r/s/p)
        self.assign_int=assign_int
        self.image=pygame.image.load(rsp[self.assign_int])
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))   



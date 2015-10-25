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

        self.model.player.draw(self.screen)



        pygame.draw.rect(self.screen, pygame.Color(self.model.ground.color[0],self.model.ground.color[1],self.model.ground.color[2]),pygame.Rect(self.model.ground.x,self.model.ground.y,self.model.ground.width,self.model.ground.height))	 

        self.screen.blit(self.model.sun.image,(self.model.sun.x,self.model.sun.y))

        #self.screen.blit(self.model.player.image,(self.model.player.x,self.model.player.y))



        self.screen.blit(self.model.obstacle.image,(self.model.obstacle.x,self.model.obstacle.y))

        self.model.item.draw(self.screen)
        #self.screen.blit(self.model.item.image,(self.model.item.x,self.model.item.y))



        pygame.display.update()



    def show_popup(self):

        self.model.popup.draw(self.screen)
        pygame.display.update()


    def show_attack(self):
        self.model.attack.draw(self.screen)
        pygame.display.update()

    def show_rock(self):
        self.model.rock.draw(self.screen)
        pygame.display.update()

    def show_scissor(self):
        self.model.scissor.draw(self.screen)
        pygame.display.update()
    def show_paper(self):
        self.model.paper.draw(self.screen)
        pygame.display.update()

    def show_rock_obs(self):
        self.model.rock_obs.draw(self.screen)
        pygame.display.update()
    def show_scissor_obs(self):
        self.model.scissor_obs.draw(self.screen)
        pygame.display.update()
    def show_paper_obs(self):
        self.model.paper_obs.draw(self.screen)
        pygame.display.update()
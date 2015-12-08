import pygame
from pygame.locals import *

class PyGameWindowView:
    ##Render our starting screen
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        ##Draw the background
        self.model.background.draw(self.screen)
        ##Draw the player
        self.model.player.draw(self.screen)
        
        ##Draw the ground
        pygame.draw.rect(self.screen, pygame.Color(self.model.ground.color[0],self.model.ground.color[1],self.model.ground.color[2]),pygame.Rect(self.model.ground.x,self.model.ground.y,self.model.ground.width,self.model.ground.height))	 

        ##Draw the sun [change to model draw function] 
        self.screen.blit(self.model.sun.image,(self.model.sun.x,self.model.sun.y))

        ##Draw the obstacle[change to model draw function]
        self.model.obstacle.draw(self.screen)
        
        ##Draw the item
        self.model.item.draw(self.screen)
        
        pygame.display.update()

    # I feel like there could have been a less copy-paste way to
    # have it draw different combinations of these things
    # for example, something like a list of all possible things, each one being marked
    # as "draw" or "don't draw" true/false flag, and call the draw method
    # of each one of them.  then, you only need one function instead of a new
    # one every time you create a new object. 

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

    def show_win_popup(self):
        self.image1=pygame.image.load("images/win_popup.jpg")
        self.screen.blit(self.image1,(200,100))

    def show_draw_popup(self):
        self.image2=pygame.image.load("images/draw_popup.jpg")
        self.screen.blit(self.image2,(200,100))

    def show_lost_popup(self):
        self.image3=pygame.image.load("images/lost_popup.jpg")
        self.screen.blit(self.image3,(200,100))


    def show_thanks_popup(self):
        self.image4 = pygame.image.load("images/thanks_popup.png")
        self.screen.blit(self.image4, (540, 50))

    def show_nothanks_popup(self):
        self.image5 = pygame.image.load("images/nothanks_popup.png")
        self.screen.blit(self.image5, (540, 50))
    def show_final_popup(self):
        self.image6=pygame.image.load("images/final_popup.png")
        self.screen.blit(self.image6, (200, 100))

import pygame
from pygame.locals import *

class PyGameWindowView:
    ##Render our starting screen
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        # self.background1=pygame.image.load("images/bluesky.png").convert()
        # self.background2=pygame.image.load("images/mountain.png").convert()
        # self.background3=pygame.image.load("images/fire.png").convert()
        # self.background4=pygame.image.load("images/castle.png").convert()

    def draw(self):
        ##Draw the background
        #self.screen.blit(self.background1,(0,0))
        self.model.background.draw(self.screen)
        ##Draw the player
        self.model.player.draw(self.screen)
        
        ##Draw the ground
        pygame.draw.rect(self.screen, pygame.Color(self.model.ground.color[0],self.model.ground.color[1],self.model.ground.color[2]),pygame.Rect(self.model.ground.x,self.model.ground.y,self.model.ground.width,self.model.ground.height))	 

        ##Draw the sun [change to model draw function] 
        self.screen.blit(self.model.sun.image,(self.model.sun.x,self.model.sun.y))

        ##Draw the obstacle[change to model draw function]
        self.screen.blit(self.model.obstacle.image,(self.model.obstacle.x,self.model.obstacle.y))

        ##Draw princess
        self.model.princess.draw(self.screen)
        ##Draw the item
        self.model.item.draw(self.screen)
        
        pygame.display.update()



    def show_popup(self):
        self.model.popup.draw(self.screen)
        print "show_popup"
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
        self.image1=pygame.image.load("images/win_popup.png")
        self.screen.blit(self.image1,(400,2))

    def show_draw_popup(self):
        self.image2=pygame.image.load("images/draw_popup.png")
        self.screen.blit(self.image2,(400,2))

    def show_lost_popup(self):
        self.image3=pygame.image.load("images/lost_popup.png")
        self.screen.blit(self.image3,(400,2))


    def show_thanks_popup(self):
        self.image4 = pygame.image.load("images/thanks_popup.png")
        self.screen.blit(self.image4, (540, 50))
        
    def show_nothanks_popup(self):
        self.image5 = pygame.image.load("images/nothanks_popup.png")
        self.screen.blit(self.image5, (540, 50))


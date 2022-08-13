import pygame as pg
import Sprites as spr
import SystemVariabes as sv
from Input import inputHandling
from random import randint


class Level():
    def __init__(self,screen):
        self.state = "menu"
        self.screen = screen

        self.points = 0 #points before update of everything, used mostly for spikes and other objects

        #sprite groups
        self.spriteWall = pg.sprite.Group()
        self.spritePlayer = pg.sprite.GroupSingle()
        self.spriteSpikes = pg.sprite.Group()
        self.spriteGroupHandle()



    def spikesHandling(self):
        if self.points != sv.points and self.state != "restart": #one time check
            self.spriteSpikes = pg.sprite.Group()

            if sv.playerDir <0:
                self.createSpikes(sv.points, sv.windowWidth / 10)
            elif sv.playerDir>0:
                self.createSpikes(sv.points, sv.windowWidth / 10*9)

        elif self.state == "restart":
            self.spriteSpikes = pg.sprite.Group()


        self.points = sv.points


    def createSpikes(self, level,xPos):

        if level > 29:
            heightOfSpikes = 20  # determines how small are y spikes sizes, the bigger the smaller
            for x in range(7):
                self.spriteSpikes.add(spr.Spikes((sv.windowWidth / 40, sv.widnowHeight / heightOfSpikes), \
                                                 (xPos, randint(50, sv.widnowHeight - 50))))
        elif level >24:
            heightOfSpikes = 13
            for x in range(4):
                self.spriteSpikes.add(spr.Spikes((sv.windowWidth / 40, sv.widnowHeight / heightOfSpikes), \
                                                     (xPos, randint(50, sv.widnowHeight - 50))))
        elif level > 14:
            heightOfSpikes = 8
            for x in range(3):
                self.spriteSpikes.add(spr.Spikes((sv.windowWidth/40 , sv.widnowHeight/heightOfSpikes),\
                                                 (xPos,randint(50, sv.widnowHeight-50))))
        elif level > 4:
            heightOfSpikes = 6
            for x in range(2):
                self.spriteSpikes.add(spr.Spikes((sv.windowWidth/40 , sv.widnowHeight/heightOfSpikes),\
                                                 (xPos,randint(50, sv.widnowHeight-50))))
        elif level > 0:
            heightOfSpikes = 5
            self.spriteSpikes.add(spr.Spikes((sv.windowWidth / 40, sv.widnowHeight / heightOfSpikes), \
                                             (xPos, randint(50, sv.widnowHeight - 50))))


    def spriteGroupHandle(self):
        self.spriteWall.add(spr.Borders(sv.windowWidth,sv.widnowHeight,"Right"))    #prawa sciana
        self.spriteWall.add(spr.Borders(sv.windowWidth, sv.widnowHeight, "Left"))   #lewa sciana

        self.spritePlayer.add(spr.Player(sv.windowWidth, sv.widnowHeight, self.spriteWall,self.spriteSpikes))#player


    def backgroundHandling(self,justColor):
        self.screen.fill(justColor)

    def stateHandling(self):
        if self.state == "menu":
            self.backgroundHandling(sv.screenWelcomeColor)
            spr.Text(self.screen, int(sv.widnowHeight/15), (sv.windowWidth/2, sv.widnowHeight/4), (255, 0, 0), "Click space to play")
            spr.Text(self.screen, int(sv.widnowHeight / 30), (sv.windowWidth / 8, sv.widnowHeight / 10*9), (255, 0, 0), "Press escape to quit")
            if inputHandling(pg.K_SPACE):
                self.state = "gameLoop"



        elif self.state == "gameLoop":
            self.backgroundHandling((40,40,40)) #pozniej bedzie zmieniajacy sie

            self.spriteWall.update()
            self.spikesHandling()
            self.spritePlayer.update(self.spriteSpikes)

            spr.Text(self.screen, int(sv.widnowHeight), (sv.windowWidth / 2, sv.widnowHeight / 2), (70, 70, 70), str(sv.points))
            self.spriteWall.draw(self.screen)
            self.spriteSpikes.draw(self.screen)
            self.spritePlayer.draw(self.screen)

            if (len(self.spritePlayer)) == 0:
                self.state = "restart"




        elif self.state == "restart":
            self.backgroundHandling((255,40,40))

            self.spikesHandling()
            sv.points = 0
            self.points = 0
            spr.Text(self.screen, int(sv.widnowHeight/15), (sv.windowWidth / 2, sv.widnowHeight / 4), (0, 0, 0),"Press 'r' to fix your mistakes")
            if inputHandling(pg.K_r):
                self.spritePlayer.add(spr.Player(sv.windowWidth, sv.widnowHeight, self.spriteWall, self.spriteSpikes))
                self.state = "gameLoop"


    def update(self):
        self.stateHandling()




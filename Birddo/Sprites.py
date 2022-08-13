import pygame as pg
import SystemVariabes as sv
from Input import inputHandling
from random import randint


class Borders(pg.sprite.Sprite):
    def __init__(self,windowX,windowY,side = "Left",color = (0,0,0)):
        super().__init__()
        self.image = None
        self.rect = None

        if side =="Left":
            self.image = pg.Surface((windowX / 10, windowY*2))
            self.image.fill(sv.borderColor)
            self.rect = self.image.get_rect(center = (windowX/20, windowY/2))
        elif side == "Right":
            self.image = pg.Surface((windowX / 10, windowY*2))
            self.image.fill(sv.borderColor)
            self.rect = self.image.get_rect(center = (windowX/20*19, windowY/2))


class Player(pg.sprite.Sprite):
    def __init__(self,windowX,windowY,collideBlocks,spikesBlocks):
        super().__init__()
        self.image = pg.Surface((windowX/15,windowY/10)).convert_alpha()
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center= (windowX/2,windowY/2))


        #rotation variables
        self.angle = 0
        self.maxAngle = 25
        self.angSpeed = 1
        self.imgOrg = self.image

        #movement variables
        if randint(0,1):
            self.inputVec = pg.math.Vector2(1,0)
        else:
            self.inputVec = pg.math.Vector2(-1, 0)
        self.movVec = pg.math.Vector2()
        self.speed = 5

        #collide variables
        self.blocks = collideBlocks.sprites()

        #jump variables
        self.gravityStrenght = sv.widnowHeight/700
        self.maxGravity = sv.widnowHeight/48
        self.yMove = 0
        self.jumpStr = -sv.widnowHeight/48

    def rotateHandling(self):
        #fuck yeah, i still remember how to do it
        if self.inputVec.x >0: #prawo

            if self.yMove < 0: #w gore
                self.angle += self.angSpeed*3
                if self.angle > self.maxAngle:
                    self.angle = self.maxAngle
            elif self.yMove >0: # w dol
                self.angle -= self.angSpeed*2
                if self.angle < -self.maxAngle:
                    self.angle = -self.maxAngle

        elif self.inputVec.x <0: #lewo
            if self.yMove < 0: #w gore
                self.angle -= self.angSpeed*3
                if self.angle < -self.maxAngle:
                    self.angle = -self.maxAngle
            elif self.yMove>0: # dol
                self.angle += self.angSpeed*2
                if self.angle > self.maxAngle:
                    self.angle = self.maxAngle


        self.image = pg.transform.rotozoom(self.imgOrg, self.angle, 1)

    def xAxisMovementHandling(self):
        self.movVec = self.inputVec * self.speed
        self.rect.x += self.movVec.x

    def collidngHandling(self):
        for wall in self.blocks:
            if wall.rect.colliderect(self.rect):
                self.angle = 0

                if wall.rect.collidepoint(self.rect.right, self.rect.y): #prawe
                    self.rect.right = wall.rect.left
                    self.inputVec.x *= -1
                    sv.points += 1
                elif wall.rect.collidepoint(self.rect.left, self.rect.y): #lewe
                    self.rect.left = wall.rect.right
                    self.inputVec.x *= -1
                    sv.points += 1

    def collideSpike(self,spikes): #fuck, to bylo ciezsze i duzo narzucalem przy tym
        for spike in spikes:
            if spike.rect.colliderect(self.rect):
                self.kill()


    def jumpHandling(self):
        if inputHandling(pg.K_SPACE) and (self.yMove>self.maxGravity/2):
            self.yMove = self.jumpStr

    def gravityHandling(self):
        self.yMove += self.gravityStrenght
        if self.yMove >= self.maxGravity:
            self.yMove = self.maxGravity

    def yAxisMovementHandling(self):
        self.gravityHandling()
        self.jumpHandling()
        self.rect.y += self.yMove

    def outOfBounds(self):
        if (self.rect.bottom <0) or (self.rect.top >sv.widnowHeight):
            self.kill()

    def update(self, spikes):
        self.xAxisMovementHandling()
        self.yAxisMovementHandling()
        self.collidngHandling()
        self.collideSpike(spikes)
        self.rotateHandling()
        self.outOfBounds()
        sv.playerDir = self.inputVec.x


class Text():
    def __init__(self,screen,size,pos,color,text):
        pg.font.init()
        self.screen = screen
        self.size = size
        self.pos = pos
        self.color = color
        self.text = str(text)

        self.font = None
        self.label = None
        self.createFont(self.screen,self.size,self.text, self.color, self.pos)

    def createFont(self,screen,size,text, color,pos):
        self.font = pg.font.Font('freesansbold.ttf', size)
        self.label = self.font.render(text,False,color)
        self.labelRect = self.label.get_rect(center = pos)
        screen.blit(self.label,self.labelRect)


class Spikes(pg.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = pos)











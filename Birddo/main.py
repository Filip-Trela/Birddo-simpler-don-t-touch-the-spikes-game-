import pygame as pg
import SystemVariabes as sv
import Level



#space to jump
#r to restart after death
#esc to quit
#there is no in game tutorial or somethin, cause it is a small project to check my skills



class Game():
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((sv.windowWidth,sv.widnowHeight),pg.SCALED | pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Birddo")

        self.levelLogic = Level.Level(self.screen)

    def update(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            self.levelLogic.update()

            pg.display.update()
            self.clock.tick(60)

Game().update()















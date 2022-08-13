import pygame as pg


def inputHandling(key):
    keys = pg.key.get_pressed()  # only space needed
    if keys[pg.K_ESCAPE]:
        pg.quit()
    if keys[key]:
        return True
    else:
        return False

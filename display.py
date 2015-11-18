import pygame as pg
from pygame.locals import *
import units as U
import random as rd
import time, sys
import math as m

def window():
    bigSize,width,height,rSize=900,1280,640,100
    screen = pg.display.set_mode((width,height),HWSURFACE|DOUBLEBUF)
    pg.display.set_caption("TBSG")
    rect1,rect2,rect3=pg.display.get_surface().get_rect(),pg.display.get_surface().get_rect(),pg.display.get_surface().get_rect()
    rect1.width=bigSize
    rect2.left,rect3.left=bigSize,bigSize
    rect2.width,rect3.width=width-bigSize,width-bigSize
    rect2.height,rect3.height=(height/2)+rSize,(height/2)-rSize
    rect3.top=(height/2)+rSize
    mapDisplay=screen.subsurface(rect1)
    unitInfo=screen.subsurface(rect2)
    turnInfo=screen.subsurface(rect3)
    #pg.display.set_icon(pg.image.load("rocket_ship.png"))
    return screen,mapDisplay,unitInfo,turnInfo


screen,mapDisplay,unitInfo,turnInfo=window()
tank=U.unit("tank")
soldier=U.unit("soldier")
soldier.rectangle.top=32
sniper=U.unit("sniper")
sniper.rectangle.top=64
fond=U.imageLoader("textures/terrain.jpg")
mapDisplay.fill((0,255,255))
unitInfo.fill((255,0,255))
turnInfo.fill((255,255,0))
while(1):
    for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.display.quit()
    mapDisplay.blit(fond,fond.get_rect())
    mapDisplay.blit(tank.texture,tank.rectangle)
    mapDisplay.blit(soldier.texture,soldier.rectangle)
    mapDisplay.blit(sniper.texture,sniper.rectangle)
    pg.display.flip()
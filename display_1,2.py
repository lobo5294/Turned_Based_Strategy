import pygame as pg
from pygame.locals import *
import units as U
import random as rd
import time, sys
import math as m
import movement as mov

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
sniper=U.unit("sniper")
fond=U.imageLoader("textures/terrain.jpg")
mapDisplay.fill((0,255,255))
unitInfo.fill((255,0,255))
turnInfo.fill((255,255,0))

#############################################################################################################
pas=48
click=0


soldier.rectangle=pg.Rect(19+3*pas,19+3*pas,32,32)
sniper.rectangle=pg.Rect(19+5*pas,19+5*pas,32,32)
tank.rectangle=pg.Rect(19+7*pas,19+3*pas,32,32)



unit=0
        
#######################################################################################

while(1):

    list_units_coord=[tank,sniper,soldier]
    
    
    for event in pg.event.get():
        
        #movement fonction
        if event.type == MOUSEBUTTONDOWN :
            

            if click==1:
                    mov.movement(unit,mapDisplay,pas,pg.mouse.get_pos())
                    

            if mov.choose_unit(list_units_coord,pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],48)!=False:
                click=1
                unit= mov.choose_unit(list_units_coord,pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],48)
                mov.zone_mov(mapDisplay,unit.rectangle[0],unit.rectangle[1],unit.movmentPoints,pas,(255,0,0))

            if click==1 and not(mov.test_coords(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],unit.rectangle[0],unit.rectangle[1],unit.movmentPoints,pas)):
                click=0

            

        if event.type == pg.QUIT:
              pg.display.quit()

    #display          
    if click==0:
        mapDisplay.blit(fond,fond.get_rect())
        mov.grid(mapDisplay,fond.get_rect().size[0],fond.get_rect().size[1],48)

        
        
    mapDisplay.blit(tank.texture,tank.rectangle)
    mapDisplay.blit(soldier.texture,soldier.rectangle)
    mapDisplay.blit(sniper.texture,sniper.rectangle)
    pg.display.flip()

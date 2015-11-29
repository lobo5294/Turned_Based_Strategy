import pygame, sys
from pygame.locals import *



def grid(name_surface,x,y,pas):
    
    for i in range(x//(pas+2)):
        for j in range(y//(pas+2)):
            pygame.draw.rect(name_surface, (0,0,0),(10+i*pas,10+j*pas,pas,pas),1)
    

def zone_mov(name_surface,x_pers,y_pers,player_moves,pas,color):

    coords=[]
    for i in range(player_moves+1):
        for j in range(player_moves+1):

            coords.append((x_pers-10+i*pas,y_pers-10+j*pas))
            coords.append((x_pers-10-i*pas,y_pers-10-j*pas))
            coords.append((x_pers-10+j*pas,y_pers-10-i*pas))
            coords.append((x_pers-10-j*pas,y_pers-10+i*pas))
            
    for i in coords:
        pygame.draw.rect(name_surface, color,(i[0],i[1],pas,pas),1)

    
    return coords

def pos_diff(x_mouse,y_mouse,x_pos,y_pos,pas):

    a=(x_mouse-x_pos)//pas #horizontal diff 
    b=(y_mouse-y_pos)//pas #vertical diff

    return a,b

def test_coords(x_mouse,y_mouse,x_player,y_player,player_moves,pas):
    
    if (abs(x_mouse-x_player)+10)**2+(abs(y_mouse-y_player)+10)**2<=(pas*(player_moves+1))**2:  
        return  True
    else:
        return False

def choose_unit(list_unit_coords,x_mouse,y_mouse,pas):

    for i in list_unit_coords:
        
        if abs((x_mouse-i.rectangle[0]))**2+abs((y_mouse-i.rectangle[1]))**2<pas**2:
            return i
        
    return False


def movement(unit,screen,pas,mouse_coords):

    if unit.Turnstatus()==False:
    
        if  test_coords(mouse_coords[0],mouse_coords[1],unit.rectangle[0],unit.rectangle[1],unit.movmentPoints,pas):
            
            move=pos_diff(mouse_coords[0],mouse_coords[1],unit.rectangle[0],unit.rectangle[1],pas)
            
            unit.rectangle.move_ip(move[0]*48,move[1]*48)
            zone_mov(screen,unit.rectangle[0],unit.rectangle[1],2,pas,(0,0,0))

            unit.move(unit.rectangle.centerx,unit.rectangle.centery)

    else:
        print("You don't have anymore movement points")

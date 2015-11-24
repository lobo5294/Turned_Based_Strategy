import pygame, sys
from pygame.locals import *



screen_dimensions= (1000, 1000)
pas = 48


player_moves=2
    



pygame.init()

DISPLAYSURF = pygame.display.set_mode(screen_dimensions, 0, 32)
pygame.display.set_caption('Movement')

player = pygame.image.load("ball.png")


player_coords=(19+3*pas,19+3*pas)

player_icon_center=(player.get_rect().size[0]/2,player.get_rect().size[1]/2)


DISPLAYSURF.fill((255,255,255))



i=0

def grid(name_surface,screen_dimesions,pas):
    for i in range(screen_dimensions[0]//(pas+2)):
        for j in range(screen_dimensions[1]//(pas+2)):
            pygame.draw.rect(name_surface, (0,0,0),(10+i*pas,10+j*pas,pas,pas),1)
    

def zone_mov(x_pers,y_pers,player_moves,pas):

    coords=[]

    for i in range(player_moves+1):
        for j in range(player_moves+1):

            coords.append((x_pers-10+i*pas,y_pers-10+j*pas))
            coords.append((x_pers-10-i*pas,y_pers-10-j*pas))
            coords.append((x_pers-10+j*pas,y_pers-10-i*pas))
            coords.append((x_pers-10-j*pas,y_pers-10+i*pas))
    return coords

def pos_diff(x_mouse,y_mouse,x_pos,y_pos,pas):

    a=(x_mouse-x_pos)//pas #horizontal diff 
    b=(y_mouse-y_pos)//pas #vertical diff

    return a,b

grid(DISPLAYSURF,screen_dimensions,pas)


while True:
    
    
    DISPLAYSURF.blit(player, player_coords)
    
    for event in pygame.event.get():
        
        if pygame.mouse.get_pressed()[0]==True :
            #print(pygame.mouse.get_pos())

            

            if i==1:
                if (abs(pygame.mouse.get_pos()[0]-player_coords[0])+10)**2+(abs(pygame.mouse.get_pos()[1]-player_coords[1])+10)**2<=(pas*player_moves+1)**2:

                    #clear movement zone
                    pygame.draw.rect(DISPLAYSURF, (255,255,255),(player_coords[0]-10,player_coords[1]-10,pas,pas),0)
                    for i in zone_mov(player_coords[0],player_coords[1],player_moves,pas):
                        pygame.draw.rect(DISPLAYSURF, (0,0,0),(i[0],i[1],pas,pas),1)
                        

                    # player movement    
                    move=pos_diff(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],player_coords[0],player_coords[1],pas)
                    player_coords=(player_coords[0]+pas*move[0],player_coords[1]+pas*move[1])
                    
                    
                    

                else:
                    i=0
                    for i in zone_mov(player_coords[0],player_coords[1],player_moves,pas):
                        pygame.draw.rect(DISPLAYSURF, (0,0,0),(i[0],i[1],pas,pas),1)
                        #clear movement zone
                    
            if (abs(pygame.mouse.get_pos()[0]-player_coords[0]))**2+(abs(pygame.mouse.get_pos()[1]-player_coords[1]))**2<pas**2:

                for i in zone_mov(player_coords[0],player_coords[1],player_moves,pas):
                    
                    pygame.draw.rect(DISPLAYSURF, (255,0,0),(i[0],i[1],pas,pas),1)
                    #draw movement zone  

                    i=1
                       
                        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

            
    pygame.display.update()


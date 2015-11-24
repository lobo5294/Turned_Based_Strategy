import pygame as pg
import math as m

class unit(object):
    def __init__(self,name):
        self.__stats=unitStatReader(name)
        self.__hp=self.__stats[0]
        self.__movmentPoints=self.__stats[1]
        self.__attackPoints=self.__stats[2]
        self.texture=imageLoader("./units/"+name+"/"+name+".png")
        self.__rectangle=self.texture.get_rect()
        self.coordinates=[self.__rectangle.x, self.__rectangle.y]
        self.isTurnOver=False
        self.__isDead=False

    def move(self,dx,dy):
        self.__rectangle.centerx= dx
        self.__rectangle.centery= dy
        self.__movmentPoints-=m.sqrt(((self.__coordinates[0]-dx)**2)+((self.__coordinates[1]-dy)**2))
        self.coordinates=[self.__rectangle.centerx, self.__rectangle.centery]
        if self.__movmentPoints<=0:
            self.__movmentPoints=self.__stats[1]
            self.__isTurnOver=True

    def takeDamage(self,damage):
        self.__hp-=damage
        if self.__hp <= 0:
            self.__hp=0
        self.__isDead=True

    def giveDamage(self,target):
        if self.__movmentPoints>=2:
            target.takeDamage(self.__damageCalculus__(target))
            self.__movmentPoints=0
            self.__isTurnOver=True
        else:
            print("Ceci est un message de DEV, ya pas assez de PM couillon...")
            print("T'es censé vérifier avant mais je prend pas de risques")

    def passTurn(self):
        self.__isTurnOver=True

    def __damageCalculus__(self,enemy):
        #Pour l'instant je fais un truc ultra basique, apres on verra pour complexifier)
        return(self.__attackPoints)

    def newTurn(self):
        self.__movmentPoints=self.__stats[1]
        self.__isTurnOver=False



def imageLoader(fichier):
    image = pg.image.load(fichier)
    return(image)

def unitStatReader(unitName):
    path="./units/"+unitName+"/"+unitName+".cz"
    file = open(path,"r")
    stats=file.readline().strip().split(';')
    file.close()
    return(stats)
import pygame as pg
import math as m

class unit(object):
    def __init__(self,name):
        self.__stats=unitStatReader(name)
        self.__hp=self.__stats[0]
        self.movmentPoints=int(self.__stats[1])
        self.__attackPoints=self.__stats[2]
        self.texture=imageLoader("./units/"+name+"/"+name+".png")
        self.rectangle=self.texture.get_rect()
        self.coordinates=[self.rectangle.centerx, self.rectangle.centery]
        self.__isTurnOver=False
        self.__isDead=False

    def move(self,dx,dy):
        if self.coordinates==[dx,dy]:
            pass
        self.coordinates=[dx,dy]
        
        if self.movmentPoints > 0:
            self.movmentPoints -= 1
        else:
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

    def Turnstatus(self):
        return self.__isTurnOver

def imageLoader(fichier):
    image = pg.image.load(fichier)
    return(image)

def unitStatReader(unitName):
    path="./units/"+unitName+"/"+unitName+".cz"
    file = open(path,"r")
    stats=file.readline().strip().split(';')
    file.close()
    return(stats)

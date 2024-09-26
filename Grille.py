import numpy as np
import random
import copy
import matplotlib.pyplot as plt
from Bateau import *

class Grille:

    def __init__(self):
        self.grille=np.zeros((10,10))
    
    def peut_placer(self,Bateau,pos,direction):
            longueur_bateau = Bateau.get_long()

            x, y = pos
            if direction == 1:  
                if y + longueur_bateau > 10:
                    return False
            
                for i in range(longueur_bateau):
                    if self.grille[x][y + i] != 0:
                        return False
            
            elif direction == 2:  
                if x + longueur_bateau > 10:
                    return False
            
                for i in range(longueur_bateau):
                    if self.grille[x + i][y] != 0:
                        return False
            return True
    
    def place(self,bateau,pos,direction):
        if(self.peut_placer(bateau,pos,direction)):
            x,y=pos
            if(direction==1):
                for i in range(bateau.get_long()):
                    self.grille[x][y+i]=bateau.get_id()
            if(direction==2):
                for i in range(bateau.get_long()):
                    self.grille[x + i][y]=bateau.get_id() 
            
        

    

    def place_alea(self, bateau):
        directions = [1, 2]  # 1 = horizontale, 2 = verticale
        placed = False
        
        while not placed:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            direction = random.choice(directions)
            
            if (self.peut_placer( bateau, (x, y), direction)):
                self.place(bateau, (x, y), direction)
                placed = True

        return self.grille
    def affiche(self):
        plt.imshow(self.grille, cmap='Greys', interpolation='none')
        plt.title("Grille de jeu")
        plt.colorbar(label="0 = Vide, 1 = Bateau")
        plt.show()

    
    def genere_grille():
        grille = Grille()  # Crée une nouvelle instance de Grille
        for i in range(5):
            b = Bateau(i + 1)
            grille.place_alea(b)  # Utilise la méthode d'instance
        return grille
            
    def nb_poss_bateau(self,bateau):
        cpt=0
        for i in range(10):
            for j in range(10):
                for k in [1,2]:
                    if (self.peut_placer(bateau,(i,j),k)) :
                        cpt+=1
        return cpt
    def nb_poss_list_bateau(self,list):
        if(list==[]):
            return 1
        bateau=list[0]
        res =0
        for i in range(10):
            for j in range(10):
                for k in [1,2]:
                    if (self.peut_placer(bateau,(i,j),k)) :
                        
                        copygrille=copy.deepcopy(self)
                        copygrille.place(bateau,(i,j),k)
                        res+=copygrille.nb_poss_list_bateau(list[1:])
        return res
                        
    def eq(self, grilleB):
        return np.array_equal(self, grilleB)
      
    def equigrille(self):
        gtest = Grille()
        cpt=0
        while(self.eq(gtest.genere_grille)==False):
            
            cpt+=1
        return cpt
            
            


    

                    

    

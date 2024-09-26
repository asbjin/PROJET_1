from Grille import *
from Bateau import *
from Bataille import *

if __name__ == "__main__":
    g1 = Grille.genere_grille() 
    b1 = Bateau(1)
    b2 = Bateau(2)
    b3 = Bateau(3)
    b4 = Bateau(4)

    g2=Grille.genere_grille() 



    print(g2)
    #g2.affiche()

    #print(g1)
    #g1.affiche()
    #print("nb possibilite", g1.nb_poss_bateau(b3))
    #print("nb possibilite", g1.nb_poss_list_bateau([b1,b2]))
    #print("nb possibilite", g2.eq(g2))
    #print("nb possibilite", g2.equigrille())


    #bataille 1

    b1= Bataille()

    b1.grille_bataille.grille.affiche()
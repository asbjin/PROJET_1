from Grille import *
class Bataille :
    
    def __init__(self):
        grille_bataille=Grille.genere_grille()

    def joue(self, position):
        x, y = position
        if self.grille.grille[x][y] > 0:  # Si on touche un bateau
            self.grille.grille[x][y] = -1  

    def victoire(self):
        for i in range(10):
            for j in range(10):
                    if (grille_bataille[x][y]!=-1 or grille_bataille[x][y]!=0 ) :
                        return False
        return True

    def reset(self):
        grille_bataille.genere_grille()

    def simulation_aleatoire(nb_simulations):
        resultats = []
        
        for _ in range(nb_simulations):
            bataille = Bataille()
            joueur = JoueurAleatoire(bataille)
            coups = joueur.jouer()
            resultats.append(coups)

        return resultats

        # Nombre de simulations
        nb_simulations = 1000
        resultats = simulation_aleatoire(nb_simulations)

        # Calcul de l'espérance
        esperance = np.mean(resultats)
        print(f"Espérance du nombre de coups: {esperance}")

        # Tracer la distribution
        plt.hist(resultats, bins=30, alpha=0.7, color='blue')
        plt.title("Distribution du nombre de coups joués")
        plt.xlabel("Nombre de coups")
        plt.ylabel("Fréquence")
        plt.show()
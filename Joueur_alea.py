import numpy as np
import random

class JoueurAleatoire:
    def __init__(self, bataille):
        self.bataille = bataille
        self.coups_tires = set()

    def jouer(self):
        coups_joues = 0
        taille_grille = 10

        while not self.bataille.victoire():
            x = random.randint(0, taille_grille - 1)
            y = random.randint(0, taille_grille - 1)
            position = (x, y)

            if position not in self.coups_tires:
                self.coups_tires.add(position)
                self.bataille.joue(position)
                coups_joues += 1

        return coups_joues

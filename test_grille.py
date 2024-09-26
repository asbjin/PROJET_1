import unittest
import numpy as np
from Grille import peut_placer, place, place_alea, affiche, eq, genere_grille

class TestGrille(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test"""
        self.grille = np.zeros((10, 10), dtype=int)

    def test_peut_placer(self):
        """Test pour vérifier si un bateau peut être placé"""
        bateau = 1  # Porte-avions (5 cases)
        position = (0, 0)
        direction = 1 
        longueur_bateau = 5
        self.assertTrue(peut_placer(self.grille, bateau, position, direction, longueur_bateau))

        position = (0, 6)
        self.assertFalse(peut_placer(self.grille, bateau, position, direction, longueur_bateau))

    def test_place(self):
        """Test pour vérifier si un bateau est correctement placé"""
        bateau = 2  
        position = (0, 0)
        direction = 1  
        longueur_bateau = 4
        grille_modifiee = place(self.grille, bateau, position, direction, longueur_bateau)
        expected_grille = np.zeros((10, 10), dtype=int)
        expected_grille[0, 0:4] = bateau
        self.assertTrue(np.array_equal(grille_modifiee, expected_grille))

    def test_place_alea(self):
        """Test pour vérifier si un bateau est placé aléatoirement"""
        bateau = 3 
        longueur_bateau = 3
        grille_modifiee = place_alea(self.grille, bateau, longueur_bateau)
        self.assertIn(bateau, grille_modifiee)

    def test_eq(self):
        """Test pour vérifier l'égalité entre deux grilles"""
        grilleA = genere_grille()
        grilleB = np.copy(grilleA)
        self.assertTrue(eq(grilleA, grilleB))

        grilleB[0, 0] = 9  
        self.assertFalse(eq(grilleA, grilleB))

    def test_genere_grille(self):
        """Test pour vérifier la génération d'une grille complète"""
        grille = genere_grille()
        bateaux_ids = [1, 2, 3, 4, 5]
        for bateau in bateaux_ids:
            self.assertTrue(np.any(grille == bateau))

if __name__ == '__main__':
    unittest.main()

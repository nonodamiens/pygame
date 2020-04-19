"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""
# pygame initialisation
pygame.init()
# ouverture de la fenetre pygame (carré)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Affichage d'un icone
icone = pygame.image.load(image_icone)
pygame.display.set_icone(icone)
# Titre
pygame.display.set_caption(titre_fenetre)
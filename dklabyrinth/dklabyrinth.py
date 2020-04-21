"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""
import pygame
from pygame.locals  import *

from constantes import *
from classes import *

# pygame initialisation
pygame.init()
# ouverture de la fenetre pygame (carré)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Affichage d'un icone
# icone = pygame.image.load(image_icone)
# pygame.display.set_icone(icone)
# Titre
# pygame.display.set_caption(titre_fenetre)

# load images
accueil = pygame.image.load(image_accueil)
fond = pygame.image.load(image_fond).convert()
personnage = Perso()
sprite = pygame.image.load(personnage.sprite).convert_alpha()
position_perso = sprite.get_rect(topleft=(0, 0))

# Boucle principale
while continuer:
    while title:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                title = False
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    title = False
                    game = True
                if event.key == K_F2:
                    title = False
                    game = True
        fenetre.blit(accueil, (0,0))
        pygame.display.flip()
    while game:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    personnage.position = personnage.mouv("B")
                    position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
                if event.key == K_UP:
                    personnage.position = personnage.mouv("H")
                    position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
                if event.key == K_LEFT:
                    personnage.position = personnage.mouv("G")
                    position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
                if event.key == K_RIGHT:
                    personnage.position = personnage.mouv("D")
                    position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
        sprite = pygame.image.load(personnage.sprite).convert_alpha()
        fenetre.blit(fond, (0,0))
        fenetre.blit(sprite, position_perso)
        pygame.display.flip()

    # Boucle menu
    # limitation de vitesse de la boucle (30 frames per secondes)
    pygame.time.Clock().tick(30)
    # Boucle jeu
    # pygame.time.Clock().tick(30)

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
start = pygame.image.load("depart.png").convert()
end = pygame.image.load("arrivee.png").convert()
mur = pygame.image.load("mur.png").convert()

# Test de colision
def colision(direction):
    if direction == "B":
        return laby.walls[personnage.position[1] + 1][personnage.position[0]] != "m"
    elif direction == "H":
        return laby.walls[personnage.position[1] - 1][personnage.position[0]] != "m"
    elif direction == "G":
        return laby.walls[personnage.position[1]][personnage.position[0] - 1] != "m"
    elif direction == "D":
        return laby.walls[personnage.position[1]][personnage.position[0] + 1] != "m"

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
                    laby = Niveau(1)
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
                    if colision("B"):
                        personnage.position = personnage.mouv("B")
                        position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
                if event.key == K_UP:
                    if colision("H"):
                        personnage.position = personnage.mouv("H")
                        position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
                if event.key == K_LEFT:
                    if colision("G"):
                        personnage.position = personnage.mouv("G")
                        position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
                if event.key == K_RIGHT:
                    if colision("D"):
                        personnage.position = personnage.mouv("D")
                        position_perso = (personnage.position[0] * 30, personnage.position[1] * 30)
        sprite = pygame.image.load(personnage.sprite).convert_alpha()
        fenetre.blit(fond, (0,0))
        for row in range(15):
            for i, p in enumerate(laby.walls[row]):
                print(row, i, p)
                if p == "d":
                    fenetre.blit(start, (0,0))
                elif p == "a":
                    fenetre.blit(end, (14 * 30, 14 * 30))
                elif p == "m":
                    fenetre.blit(mur, (i * 30, row * 30))
        fenetre.blit(sprite, position_perso)
        pygame.display.flip()

    # Boucle menu
    # limitation de vitesse de la boucle (30 frames per secondes)
    pygame.time.Clock().tick(30)
    # Boucle jeu
    # pygame.time.Clock().tick(30)

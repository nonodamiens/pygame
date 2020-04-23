"""
Ce fichier python sert à tester la gestion du joystick avec pygame
"""

import pygame
from pygame.locals import *

# Initialisation de pygame
pygame.init()

# compter le nombre de joystick
nb_joystick = pygame.joystick.get_count()
print("Il y a {} joystick de branche".format(nb_joystick))

# si y'en a au moins un on le crée avec son numéro de branchement (commençant par 0) et on l'initialise
if nb_joystick > 0:
    mon_joystick = pygame.joystick.Joystick(0)
    mon_joystick.init()

    # Maintenant on va compter les boutons qu'on a de dispo
    print("axes: ", mon_joystick.get_numaxes())
    print("boutons: ", mon_joystick.get_numbuttons())
    print("trackballs: ", mon_joystick.get_numballs())
    print("hats: ", mon_joystick.get_numhats())

    # Faudrait récupérer les numéro des boutons -> nous pouvons les tester
    if mon_joystick.get_numbuttons() > 1:
        # on génère une boucle
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == JOYBUTTONDOWN:
                    print(event.button)
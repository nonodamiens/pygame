"""
Comment gérer les sons / musiques avec pygame

Il y a 2 modules à connaitre pour ça :
MIXER
MUSIC (sous module de mixer pour gérer la musique étonnament ;) )

MUSIC permet de streamer les gros fichier et lancer des sons/musique avec un buffer avant donc d'avoir tout chargé
"""

import pygame
from pygame.locals import *

# 0 - pygame init
pygame.init()
fenetre = pygame.display.set_mode((200,200))

# 1 - créer un objet son
son = pygame.mixer.Sound("coq.wav")

# jouer le son
son.play()

# pour stopper le son on utilisera la methode STOP (cf dans boucle)
# pour agir sur tous les son en même temps :
# pygame.mixer.pause()
# pygame.mixer.unpause()
# pygame.mixer.stop()

# 2 - boucle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            # stopper le son
            son.stop()
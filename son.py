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
music = pygame.mixer.Sound("music.wav")

# jouer le son
son.play()

# pour stopper le son on utilisera la methode STOP (cf dans boucle)
# pour agir sur tous les son en même temps :
# pygame.mixer.pause()
# pygame.mixer.unpause()
# pygame.mixer.stop()
# Quelques autres fonctions
# son.fadeout(300) #Fondu à 300ms de la fin de l'objet "son"
# pygame.mixer.fadeout(300) #Fondu à 300ms de la fin de tous les objets Sound

# En ce qui concerne le module music :
# pygame.mixer.music.load("musique.wav") #Charge musique dans la playlist
# pygame.mixer.music.queue("musique2.wav") #positionne la musique2 à la fin de la playlist
# pygame.mixer.music.start()
# pygame.mixer.music.stop()
# pygame.mixer.music.pause()
# pygame.mixer.music.unpause()
# pygame.mixer.music.fadeout(300)
# volume = pygame.mixer.music.get_volume() #Retourne la valeur du volume, entre 0 et 1
# pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)

# 2 - boucle
# variable de vérification du premier lancement de la musique
start = True
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if start:
                    music.play()
                    start = False
                else:
                    pygame.mixer.unpause()
        if event.type == KEYUP:
            if event.key == K_SPACE:
                pygame.mixer.pause()
        if event.type == KEYDOWN and event.key == K_RETURN:
            music.stop()
            start = True
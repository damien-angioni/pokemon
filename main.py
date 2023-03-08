#Importation de librairies et des fichiers python.
import pygame
import random
import time

#Fonctions secondaires.
def menu():#Menu principal du jeu.
    pygame.mixer.music.load(ost_main_menu)
    pygame.mixer.music.play(loops = -1)
    etat_menu=True
    while(etat_menu==True):
        fenetre.blit(BG_menu,(0,0))
        fenetre.blit(button01,(870,100))
        fenetre.blit(font_style.render("Jouer", True, [255,215,0]),(900,101))
        fenetre.blit(button01,(870,200))
        fenetre.blit(font_style.render("Quitter", True, [255,215,0]),(887,201))
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and 870 <= pygame.mouse.get_pos()[0] <= 1140 and 100 <= pygame.mouse.get_pos()[1] <= 150:
                etat_menu=False
            if pygame.mouse.get_pressed()[0] and 870 <= pygame.mouse.get_pos()[0] <= 1140 and 200 <= pygame.mouse.get_pos()[1] <= 250:
                quit()
        pygame.display.update()
    intro()

def intro():#"Cinématique" d'intro du jeu.
    pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.mixer.music.load(ost_intro)
    pygame.mixer.music.play(loops = -1)
    fenetre.blit(BG_intro,(0,0))
    pygame.display.update()
    time.sleep(2.5)
    fenetre.blit(mismagius,(150,150))
    pygame.display.update()
    time.sleep(2.5)
    fenetre.blit(dialbox,(130,570))
    pygame.display.update()
    time.sleep(10.5)
    fenetre.blit(mismagius,(150,150))
    pygame.display.update()

#--- | Programme principal | ---#

#Ouverture et définition de la fenètre du jeu.
pygame.init()
pygame.font.init()
font_style = pygame.font.Font("Resources/font_cl.ttf", 35)
fenetre=pygame.display.set_mode((1080,720))
pygame.display.set_caption("Pokémon Heroes")
pygame.display.set_icon(pygame.image.load("Resources/Frame_image/icon.png"))

#Définiton des sons & musiques.
ost_main_menu="Resources/OST/main_menu.mp3"
ost_intro="Resources/OST/intro.mp3"
ost_calm="Resources/OST/calm.mp3"
ost_battle="Resources/OST/to_battle.mp3"

#Définition des images structurelles.
BG_menu = pygame.image.load("Resources/Frame_image/menu.png").convert()
BG_menu = pygame.transform.scale(BG_menu,(1080,720))
BG_intro = pygame.image.load("Resources/Frame_image/awakening.png").convert()
BG_intro = pygame.transform.scale(BG_intro,(1080,720))
button01 = pygame.image.load("Resources/Frame_image/button.png")
button01 = pygame.transform.scale(button01,(150,50))
dialbox = pygame.image.load("Resources/Frame_image/dialbox.png")
dialbox = pygame.transform.scale(dialbox,(820,150))

#Déinition des sprites.
mismagius = pygame.image.load("Resources/Sprites/mismagius.png")
mismagius = pygame.transform.scale(mismagius,(500,500))

menu()#Lancement du menu du jeu.
quit()#Ferme la page si jamais sortie de toute les boucles et sous-programmes.

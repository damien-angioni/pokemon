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
        fenetre.blit(menu_button_font.render("Jouer", True, [255,215,0]),(900,101))
        fenetre.blit(button01,(870,200))
        fenetre.blit(menu_button_font.render("Quitter", True, [255,215,0]),(887,201))
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and 870 <= pygame.mouse.get_pos()[0] <= 1140 and 100 <= pygame.mouse.get_pos()[1] <= 150:
                etat_menu=False
            if pygame.mouse.get_pressed()[0] and 870 <= pygame.mouse.get_pos()[0] <= 1140 and 200 <= pygame.mouse.get_pos()[1] <= 250:
                quit()
        pygame.display.update()
    intro()
def clic_to_continue():
    time.sleep(0.5)
    click_to_continue=True
    while(click_to_continue==True):
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                click_to_continue=False
    time.sleep(0.5)

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
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("Salut à toi l'ami bienvenue dans le monde des pokémons! Tu dois être nouveaux ici, non?", True, [0,0,0]),(150,590))
    fenetre.blit(dialog_font.render("Nous sommes des Pokémons et nous vivons en harmonie avec les humains, qui nous aident", True, [0,0,0]),(150,615))
    fenetre.blit(dialog_font.render("dansnous taches et travaux! Certains pokémons dressent des humains et les font combattre ", True, [0,0,0]),(150,640))
    fenetre.blit(dialog_font.render("entre eux. Ces humains sont appelés les Héros, mais vaut mieux que tu essaie toi même...", True, [0,0,0]),(150,665))
    pygame.display.update()
    clic_to_continue()
    fenetre.blit(dialbox,(130,570))
    fenetre.blit(orbe,(880,310))
    fenetre.blit(menu_button_font.render("Touche l'Orbe!", True, [255,215,0]),(900,101))
    pygame.display.update()
    clickorb=False
    while(clickorb==False):
        print("dedan")
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and 880 <= pygame.mouse.get_pos()[0] <= 980 and 310 <= pygame.mouse.get_pos()[1] <= 410:
                clickorb=True
        pygame.display.update()
    time.sleep(0.5)
    pygame.display.flip()
    fenetre.blit(BG_intro,(0,0))
    fenetre.blit(runes,(290,110))
    time.sleep(0.5)
    
    clic_to_continue()



#--- | Programme principal | ---#

#Ouverture et définition de la fenètre du jeu.
pygame.init()
pygame.font.init()
fenetre=pygame.display.set_mode((1080,720))
pygame.display.set_caption("Pokémon Heroes")
pygame.display.set_icon(pygame.image.load("Resources/Frame_image/icon.png"))

#Définiton des sons & musiques.
ost_main_menu="Resources/OST/main_menu.mp3"
ost_intro="Resources/OST/intro.mp3"
ost_calm="Resources/OST/calm.mp3"
ost_battle="Resources/OST/to_battle.mp3"

#Définitions des textes.
menu_button_font = pygame.font.Font("Resources/font_cl.ttf", 35)
dialog_font = pygame.font.Font("Resources/font_cl.ttf", 18)

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
orbe = pygame.image.load("Resources/Sprites/orb.png")
orbe = pygame.transform.scale(orbe,(100,100))
runes = pygame.image.load("Resources/Sprites/orb.png")
runes = pygame.transform.scale(runes,(500,500))

menu()#Lancement du menu du jeu.
quit()#Ferme la page si jamais sortie de toute les boucles et sous-programmes.

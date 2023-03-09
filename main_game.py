#Importation de librairies et des fichiers python.
import pygame
import random
import time
from definitions import *

#--- | Main Game | ---#

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
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("Nous sommes des Pokémons et nous vivons en harmonie avec les humains, qui nous aident", True, [0,0,0]),(150,615))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("dans nos taches et travaux! Certains pokémons dressent des humains et les font combattre ", True, [0,0,0]),(150,640))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("entre eux. Ces humains sont appelés les Héros, mais vaut mieux que tu essaie toi même...", True, [0,0,0]),(150,665))
    pygame.display.update()
    clic_to_continue()
    fenetre.blit(dialbox,(130,570))
    fenetre.blit(orbe,(880,310))
    fenetre.blit(menu_button_font.render("Touche l'Orbe!", True, [255,215,0]),(630,335))
    pygame.display.update()
    clickorb=False
    while(clickorb==False):
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and 880 <= pygame.mouse.get_pos()[0] <= 980 and 310 <= pygame.mouse.get_pos()[1] <= 410:
                clickorb=True
        pygame.display.update()
    pygame.display.flip()
    fenetre.blit(BG_intro,(0,0))
    fenetre.blit(runes,(290,110))
    pygame.display.update()
    time.sleep(1.5)
    pygame.display.flip()
    fenetre.blit(BG_intro,(0,0))
    fenetre.blit(marthintro,(315,60))
    pygame.display.update()
    time.sleep(0.5)
    pygame.mixer.Sound.play(pygame.mixer.Sound(sfx_marth))
    fenetre.blit(dialbox,(130,570))
    fenetre.blit(dialog_font.render("Je suis Marth!", True, [0,0,0]),(150,590))
    pygame.display.update()
    clic_to_continue()
    pygame.display.flip()
    fenetre.blit(BG_intro,(0,0))
    fenetre.blit(mismagius,(150,150))
    fenetre.blit(dialbox,(130,570))
    fenetre.blit(dialog_font.render("Il s'appelle Marth, est c'est un Héros de type épée. Chaque héros possède un type qui", True, [0,0,0]),(150,590))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("définissent leur forces et leur faiblesses au combat. Par exemple, l'épée bat la hache", True, [0,0,0]),(150,615))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("mais la hache bat la lance, et la lance bat l'épée. C'est comme papier/ciseaux/caillou!", True, [0,0,0]),(150,640))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("Biensur, il existe d'autres types de Héros avec des fonctionnement différents, tu verra!", True, [0,0,0]),(150,665))
    pygame.display.update()
    clic_to_continue()
    fenetre.blit(dialbox,(130,570))
    fenetre.blit(dialog_font.render("Les Héros sont liés à des orbes, ils acceptent de la donner aux dresseurs qu'ils jugent", True, [0,0,0]),(150,590))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("digne de leur pouvoir. A ce sujet, j'aurai un tâche à te confier, et pas des moindres...", True, [0,0,0]),(150,615))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("Je suis le professeur Mismagius, et j'étudie les Héros, c'est la raison pour laquelle", True, [0,0,0]),(150,640))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("J'aimerai que tu classe tous les Héros dans une encyclopédie, en parcourant le monde!", True, [0,0,0]),(150,665))
    pygame.display.update()
    clic_to_continue()
    fenetre.blit(dialbox,(130,570))
    fenetre.blit(dialog_font.render("Je sais que c'est une tâche hardue et fastidieuse, vue que c'était la mienne, mais tu verras", True, [0,0,0]),(150,590))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("a quel point c'est amusant! Biensur, je ne suis pas ingrate, je te laisserai partir avec", True, [0,0,0]),(150,615))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("l'un de mes héros.. Mais pas Marth, il est trop précieux pour moi...", True, [0,0,0]),(150,640))
    pygame.display.update()
    time.sleep(0.5)
    fenetre.blit(dialog_font.render("L'un de ces trois devrait faire l'affaire, fais donc ton choix, dresseur, et tu pars à l'aventure!", True, [0,0,0]),(150,665))
    pygame.display.update()
    clic_to_continue()
    pygame.display.flip()
    fenetre.blit(BG_intro,(0,0))
    fenetre.blit(menu_button_font.render("Touche l'Orbe de ton futur meilleur ami!", True, [255,215,0]),(220,150))
    fenetre.blit(redorbe,(140,310))
    fenetre.blit(sword_ico,(140,310))
    fenetre.blit(blueorbe,(500,310))
    fenetre.blit(lance_ico,(500,310))
    fenetre.blit(greenorbe,(860,310))
    fenetre.blit(axe_ico,(860,310))
    fenetre.blit(alfonse_sp,(120,420))
    fenetre.blit(sharena_sp,(480,420))
    fenetre.blit(anna_sp,(840,420))
    pygame.display.update()
    time.sleep(1)
    clickorb=False
    while(clickorb==False):
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] and 140 <= pygame.mouse.get_pos()[0] <= 240 and 310 <= pygame.mouse.get_pos()[1] <= 410:
                fenetre.blit(BG_intro,(0,0))
                fenetre.blit(alfonse_splash,(275,60))
                pygame.display.update()
                time.sleep(3)
                game_loop()
            if pygame.mouse.get_pressed()[0] and 500 <= pygame.mouse.get_pos()[0] <= 600 and 310 <= pygame.mouse.get_pos()[1] <= 410:
                fenetre.blit(BG_intro,(0,0))
                fenetre.blit(sharena_splash,(275,60))
                pygame.display.update()
                time.sleep(3)
                game_loop()
            if pygame.mouse.get_pressed()[0] and 860 <= pygame.mouse.get_pos()[0] <= 960 and 310 <= pygame.mouse.get_pos()[1] <= 410:
                fenetre.blit(BG_intro,(0,0))
                fenetre.blit(anna_splash,(275,60))
                pygame.display.update()
                time.sleep(3)
                game_loop()
        pygame.display.update()
def game_loop():#Boucle principale du jeu.
    game_over=False
    while(game_over==False):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(ost_calm)
        pygame.mixer.music.play(loops = -1)
        fenetre.blit(BG_castle,(0,0))
        pygame.display.update()
        clic_to_continue()
    quit()

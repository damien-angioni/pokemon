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
sfx_marth="Resources/SFX/marthintro.mp3"

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
redorbe = pygame.image.load("Resources/Sprites/redorb.png")
redorbe = pygame.transform.scale(redorbe,(100,100))
blueorbe = pygame.image.load("Resources/Sprites/blueorb.png")
blueorbe = pygame.transform.scale(blueorbe,(100,100))
greenorbe = pygame.image.load("Resources/Sprites/greenorb.png")
greenorbe = pygame.transform.scale(greenorbe,(100,100))
runes = pygame.image.load("Resources/Sprites/magic.png")
runes = pygame.transform.scale(runes,(500,500))
marthintro = pygame.image.load("Resources/Sprites/marth.png")
marthintro = pygame.transform.scale(marthintro,(450,600))

#définition des sprites des types
astra_ico = pygame.image.load("Resources/Types/astra.png")
astra_ico = pygame.transform.scale(astra_ico,(350,350))
axe_ico = pygame.image.load("Resources/Types/axe.png")
axe_ico = pygame.transform.scale(axe_ico,(350,350))
bow_ico = pygame.image.load("Resources/Types/bow.png")
bow_ico = pygame.transform.scale(bow_ico,(350,350))
dagger_ico = pygame.image.load("Resources/Types/dagger.png")
dagger_ico = pygame.transform.scale(dagger_ico,(350,350))
earth_ico = pygame.image.load("Resources/Types/earth.png")
earth_ico = pygame.transform.scale(earth_ico,(350,350))
fire_ico = pygame.image.load("Resources/Types/fire.png")
fire_ico = pygame.transform.scale(fire_ico,(350,350))
ice_ico = pygame.image.load("Resources/Types/ice.png")
ice_ico = pygame.transform.scale(ice_ico,(350,350))
lance_ico = pygame.image.load("Resources/Types/lance.png")
lance_ico = pygame.transform.scale(lance_ico,(350,350))
light_ico = pygame.image.load("Resources/Types/light.png")
light_ico = pygame.transform.scale(light_ico,(350,350))
no_weapon_ico = pygame.image.load("Resources/Types/no_weapon.png")
no_weapon_ico = pygame.transform.scale(no_weapon_ico,(350,350))
shadow_ico = pygame.image.load("Resources/Types/shadow.png")
shadow_ico = pygame.transform.scale(shadow_ico,(350,350))
sword_ico = pygame.image.load("Resources/Types/sword.png")
sword_ico = pygame.transform.scale(sword_ico,(350,350))
thunder_ico = pygame.image.load("Resources/Types/thunder.png")
thunder_ico = pygame.transform.scale(thunder_ico,(350,350))
water_ico = pygame.image.load("Resources/Types/water.png")
water_ico = pygame.transform.scale(water_ico,(350,350))
wind_ico = pygame.image.load("Resources/Types/wind.png")
wind_ico = pygame.transform.scale(wind_ico,(350,350))

#Définition des sprites personnage.
alphonse_sp = pygame.image.load("Resources/Sprites/Character/alphonse.png")
alphonse_sp = pygame.transform.scale(alphonse_sp,(350,350))
sharena_sp = pygame.image.load("Resources/Sprites/Character/sharena.png")
sharena_sp = pygame.transform.scale(sharena_sp,(350,350))
anna_sp = pygame.image.load("Resources/Sprites/Character/anna.png")
anna_sp = pygame.transform.scale(anna_sp,(350,350))

menu()#Lancement du menu du jeu.
quit()#Ferme la page si jamais sortie de toute les boucles et sous-programmes.

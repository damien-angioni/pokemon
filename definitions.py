#Importation de librairies et des fichiers python.
import pygame

#--- | Définitions variables | ---#

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
BG_castle = pygame.image.load("Resources/Frame_image/castle.png")
BG_castle = pygame.transform.scale(BG_castle,(1080,720))

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
alfonse_splash = pygame.image.load("Resources/Sprites/alfonse.png")
alfonse_splash = pygame.transform.scale(alfonse_splash,(530,600))
sharena_splash = pygame.image.load("Resources/Sprites/sharena.png")
sharena_splash = pygame.transform.scale(sharena_splash,(530,600))
anna_splash = pygame.image.load("Resources/Sprites/anna.png")
anna_splash = pygame.transform.scale(anna_splash,(530,600))


#définition des sprites des types
astra_ico = pygame.image.load("Resources/Types/astra.png")
astra_ico = pygame.transform.scale(astra_ico,(35,35))
axe_ico = pygame.image.load("Resources/Types/axe.png")
axe_ico = pygame.transform.scale(axe_ico,(35,35))
bow_ico = pygame.image.load("Resources/Types/bow.png")
bow_ico = pygame.transform.scale(bow_ico,(35,35))
dagger_ico = pygame.image.load("Resources/Types/dagger.png")
dagger_ico = pygame.transform.scale(dagger_ico,(35,35))
earth_ico = pygame.image.load("Resources/Types/earth.png")
earth_ico = pygame.transform.scale(earth_ico,(35,35))
fire_ico = pygame.image.load("Resources/Types/fire.png")
fire_ico = pygame.transform.scale(fire_ico,(35,35))
ice_ico = pygame.image.load("Resources/Types/ice.png")
ice_ico = pygame.transform.scale(ice_ico,(35,35))
lance_ico = pygame.image.load("Resources/Types/lance.png")
lance_ico = pygame.transform.scale(lance_ico,(35,35))
light_ico = pygame.image.load("Resources/Types/light.png")
light_ico = pygame.transform.scale(light_ico,(35,35))
no_weapon_ico = pygame.image.load("Resources/Types/no_weapon.png")
no_weapon_ico = pygame.transform.scale(no_weapon_ico,(35,35))
shadow_ico = pygame.image.load("Resources/Types/shadow.png")
shadow_ico = pygame.transform.scale(shadow_ico,(35,35))
sword_ico = pygame.image.load("Resources/Types/sword.png")
sword_ico = pygame.transform.scale(sword_ico,(35,35))
thunder_ico = pygame.image.load("Resources/Types/thunder.png")
thunder_ico = pygame.transform.scale(thunder_ico,(35,35))
water_ico = pygame.image.load("Resources/Types/water.png")
water_ico = pygame.transform.scale(water_ico,(35,35))
wind_ico = pygame.image.load("Resources/Types/wind.png")
wind_ico = pygame.transform.scale(wind_ico,(35,35))

#Définition des sprites personnage.
alfonse_sp = pygame.image.load("Resources/Sprites/Character/alphonse.png")
alfonse_sp = pygame.transform.scale(alfonse_sp,(150,150))
sharena_sp = pygame.image.load("Resources/Sprites/Character/sharena.png")
sharena_sp = pygame.transform.scale(sharena_sp,(150,150))
anna_sp = pygame.image.load("Resources/Sprites/Character/anna.png")
anna_sp = pygame.transform.scale(anna_sp,(150,150))

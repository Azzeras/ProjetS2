# GAME OPTIONS
import pygame as pg
pg.init()
c= pg.display.Info()

WIDTH = int(c.current_w)-100
HEIGHT = int(c.current_h)-100
FPS = 60
TAILLE_SERPENT=20
TITLE = 'ok'
# IMAGES DES SERPENTS


# OPTONS DU PLAYER
SERPENT_IMG='Serpent.png'
PLAYER_ACC=0.8
PLAYER_FRIC=-0.1
PLAYER_SPEED=5
PLAYER_ROT_SPEED =5
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
SERPENT_BODY = 'mapTile_022.png'
# COULEURS

WHITE =(255,255,255)
LIGHTGREY = (100,100,100)
BLACK =(0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)
BROWN = (87,41,14)

BGCOLOR = BROWN
#BONBONS
CANDY1_IMG = 'Candy1.png'
CANDY2_IMG = 'Candy2.png'
CANDY3_IMG = 'Candy3.png'
CANDY4_IMG = 'Candy4.png'
CANDY5_IMG = 'Candy5.png'
CANDY6_IMG = 'Candy6.png'
CANDY7_IMG = 'Candy7.png'
CANDY8_IMG = 'Candy8.png'
CANDY9_IMG = 'Candy9.png'
CANDY10_IMG = 'Candy10.png'
CANDY11_IMG = 'Candy11.png'
CANDY12_IMG = 'Candy12.png'
CANDY13_IMG = 'Candy13.png'
CANDY14_IMG = 'Candy14.png'
CANDY15_IMG = 'Candy15.png'
COOLDOWN_SPAWN_BONBON = 1


# OPTION DES ARTIFICIAL INTELLIGNECE

COOLDOWN_SPAWN_AI = 5
SERPENT_AI_SPEED = 30


# SOUNDS
TITANIC = 'Titanic_Flute.wav'
GUILE_THEME = 'Guile_Theme.wav'
CODE_MUSIC = 'CODE_AVEC_LE_CUL.wav'
EAT_CANDY_SOUND = ['Wololo.wav','Zbeub.wav','Chewbacca.wav','Bruh.wav','AH.wav','BarrelRoll.wav','Cest_Pas_Faux.wav','Eddy_Malou.wav','Nope.wav','Shoryuken.wav','Skype.wav','Trap.wav','Tuturu.wav','Yasuo.wav']

GAME_OVER_SOUND = ['Noooo.wav','Motus_Boule_Noir.wav','Illidan.wav','Jack.wav','No_God_Plz.wav','Really_Nigga.wav','Sad_Violon.wav']

KILL_AI_SNAKE_SOUND = ['MLG.wav','Headshot.wav','Combo_Breaker.wav','Demacia.wav','Il_Est_Fort.wav','Julien_Lepers.wav','Leroyyyyyyyy.wav','Quickshot.wav','Pentakill.wav']


#  OPTION MENUES DIVERS ET VARIES

TAILLE_ECRIT_NORMAL = 100
TAILLE_ECRIT_GRAND = 250

FLECHE_UP  = 'Fleche_UP.jpg'
FLECHE_DROITE = 'Fleche_Droite.png'
FLECHE_GAUCHE = 'Fleche_Gauche.png'

FLECHE_UP_PAUSED  = 'Fleche_UP_Paused.png'
FLECHE_DROITE_PAUSED = 'Fleche_Droite_Paused.png'
FLECHE_GAUCHE_PAUSED = 'Fleche_Gauche_Paused.png'








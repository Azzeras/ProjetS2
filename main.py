import pygame as pg
import random
from os import path, environ
from settings import *
from sprites import *
from tilemap import *
from time import *

x, y = 50, 50
environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(x,y)
class Game():
    def __init__(self):
        # INITIALIZE ( game window .... )
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.load_data()
        self.running = True
        self.last_time_candy = time()
        self.last_time_serpent = time()
        self.candy_List =[]

    def draw_text(self, text, font_name, size, color, x, y, align="Nord_Ouest"):
        f = open(font_name,'r')
        font = pg.font.Font(font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "Nord_Ouest":
            text_rect.topleft = (x, y)
        if align == "Nord_Est":
            text_rect.topright = (x, y)
        if align == "Suc_Ouest":
            text_rect.bottomleft = (x, y)
        if align == "Sud_Est":
            text_rect.bottomright = (x, y)
        if align == "Nord":
            text_rect.midtop = (x, y)
        if align == "Sud":
            text_rect.midbottom = (x, y)
        if align == "Est":
            text_rect.midright = (x, y)
        if align == "Ouest":
            text_rect.midleft = (x, y)
        if align == "Middle":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Images')
        self.sound_folder = path.join(game_folder, 'Sounds')

        self.fontJP = path.join(img_folder, 'Jurassic_Park.TTF')

        self.color_paused = pg.Surface(self.screen.get_size()).convert_alpha()
        self.color_paused.fill((0,0,0,140))

        self.fleche_up = pg.image.load(path.join(img_folder, FLECHE_UP)).convert_alpha()
        self.fleche_up = pg.transform.scale(self.fleche_up , (TAILLE_ECRIT_NORMAL,TAILLE_ECRIT_NORMAL))

        self.fleche_gauche = pg.image.load(path.join(img_folder, FLECHE_GAUCHE)).convert_alpha()
        self.fleche_gauche = pg.transform.scale(self.fleche_gauche , (TAILLE_ECRIT_NORMAL,TAILLE_ECRIT_NORMAL))

        self.fleche_droite = pg.image.load(path.join(img_folder, FLECHE_DROITE)).convert_alpha()
        self.fleche_droite = pg.transform.scale(self.fleche_droite , (TAILLE_ECRIT_NORMAL,TAILLE_ECRIT_NORMAL))

        self.fleche_up_paused = pg.image.load(path.join(img_folder, FLECHE_UP_PAUSED)).convert_alpha()
        self.fleche_up_paused = pg.transform.scale(self.fleche_up_paused , (TAILLE_ECRIT_NORMAL,TAILLE_ECRIT_NORMAL))

        self.fleche_gauche_paused = pg.image.load(path.join(img_folder, FLECHE_GAUCHE_PAUSED)).convert_alpha()
        self.fleche_gauche_paused = pg.transform.scale(self.fleche_gauche_paused , (TAILLE_ECRIT_NORMAL,TAILLE_ECRIT_NORMAL))

        self.fleche_droite_paused = pg.image.load(path.join(img_folder, FLECHE_DROITE_PAUSED)).convert_alpha()
        self.fleche_droite_paused = pg.transform.scale(self.fleche_droite_paused , (TAILLE_ECRIT_NORMAL,TAILLE_ECRIT_NORMAL))

        self.serpent_img = pg.image.load(path.join(img_folder, SERPENT_IMG)).convert_alpha()
        self.serpent_img = pg.transform.scale(self.serpent_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.serpent_img_body = pg.image.load(path.join(img_folder, SERPENT_BODY)).convert_alpha()
        self.serpent_img_body = pg.transform.scale(self.serpent_img_body, (TAILLE_SERPENT+5,TAILLE_SERPENT+5))

        self.candy1_img = pg.image.load(path.join(img_folder, CANDY1_IMG)).convert_alpha()
        self.candy1_img = pg.transform.scale(self.candy1_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy2_img = pg.image.load(path.join(img_folder, CANDY2_IMG)).convert_alpha()
        self.candy2_img = pg.transform.scale(self.candy2_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy3_img = pg.image.load(path.join(img_folder, CANDY3_IMG)).convert_alpha()
        self.candy3_img = pg.transform.scale(self.candy3_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy4_img = pg.image.load(path.join(img_folder, CANDY4_IMG)).convert_alpha()
        self.candy4_img = pg.transform.scale(self.candy4_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy5_img = pg.image.load(path.join(img_folder, CANDY5_IMG)).convert_alpha()
        self.candy5_img = pg.transform.scale(self.candy5_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy6_img = pg.image.load(path.join(img_folder, CANDY6_IMG)).convert_alpha()
        self.candy6_img = pg.transform.scale(self.candy6_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy7_img = pg.image.load(path.join(img_folder, CANDY7_IMG)).convert_alpha()
        self.candy7_img = pg.transform.scale(self.candy7_img, (TAILLE_SERPENT, TAILLE_SERPENT))

        self.candy8_img = pg.image.load(path.join(img_folder, CANDY8_IMG)).convert_alpha()
        self.candy8_img = pg.transform.scale(self.candy8_img, (TAILLE_SERPENT, TAILLE_SERPENT))

        self.candy9_img = pg.image.load(path.join(img_folder, CANDY9_IMG)).convert_alpha()
        self.candy9_img = pg.transform.scale(self.candy9_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy10_img = pg.image.load(path.join(img_folder, CANDY10_IMG)).convert_alpha()
        self.candy10_img = pg.transform.scale(self.candy10_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy11_img = pg.image.load(path.join(img_folder, CANDY11_IMG)).convert_alpha()
        self.candy11_img = pg.transform.scale(self.candy11_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy12_img = pg.image.load(path.join(img_folder, CANDY12_IMG)).convert_alpha()
        self.candy12_img = pg.transform.scale(self.candy12_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy13_img = pg.image.load(path.join(img_folder, CANDY13_IMG)).convert_alpha()
        self.candy13_img = pg.transform.scale(self.candy13_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy14_img = pg.image.load(path.join(img_folder, CANDY14_IMG)).convert_alpha()
        self.candy14_img = pg.transform.scale(self.candy14_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.candy15_img = pg.image.load(path.join(img_folder, CANDY15_IMG)).convert_alpha()
        self.candy15_img = pg.transform.scale(self.candy15_img, (TAILLE_SERPENT,TAILLE_SERPENT))

        self.eat_candy_sound=[]
        for sound in EAT_CANDY_SOUND:
            self.eat_candy_sound.append(pg.mixer.Sound(path.join(self.sound_folder, sound)))

        self.kill_ai_sound=[]
        for sound in KILL_AI_SNAKE_SOUND:
            self.kill_ai_sound.append(pg.mixer.Sound(path.join(self.sound_folder, sound)))

        self.game_over_sound=[]
        for sound in GAME_OVER_SOUND:
            self.game_over_sound.append(pg.mixer.Sound(path.join(self.sound_folder, sound)))

    def new(self):

        # START A NEW GAME
        self.all_sprites = pg.sprite.Group()
        self.candies = pg.sprite.Group()
        self.bodies = pg.sprite.Group()
        self.snakeAIs = pg.sprite.Group()
        self.bodies_ai = pg.sprite.Group()

        self.player = Player(self, WIDTH//2, HEIGHT//2)
        self.all_sprites.add(self.player)
        self.camera = Camera(WIDTH, HEIGHT)
        self.pause = False
        self.option_pause = False
        self.raccpause = False
        self.musique_fond = True
        self.sond_ambiant= True

        pg.mixer.music.load(path.join(self.sound_folder, CODE_MUSIC))
        pg.mixer.music.set_volume(0.03)


        self.run()

    def run(self):
        # GAMELOOP

        self.playing=True
        self.start_screen()
        if self.musique_fond:
            pg.mixer.music.play(loops=-1)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            if not self.pause:
                self.update()
            self.draw()

    def update(self):
        # GAMELOOP -- UPDATE
        self.all_sprites.update()
        self.camera.update(self.player)
        self.candies.update()


    def events(self):
        # GAMELOOP -- EVENTS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.pause = not self.pause

        self.candy_tmp = []
        self.candyList_Compteur=-1
        if time() - self.last_time_candy > COOLDOWN_SPAWN_BONBON and not self.pause:
            self.rand_bonbon_X_Time = random.randrange(int(self.player.pos.x) - int(WIDTH/2),int(self.player.pos.x )+ int(WIDTH/2))
            self.rand_bonbon_Y_Time = random.randrange(int(self.player.pos.y) - int(HEIGHT/2),int(self.player.pos.y )+ int(HEIGHT/2))
            self.last_time_candy = time()
            self.candy_List.append((self.rand_bonbon_X_Time, self.rand_bonbon_Y_Time))
            Candy(self, self.rand_bonbon_X_Time, self.rand_bonbon_Y_Time)

        if time() - self.last_time_serpent > COOLDOWN_SPAWN_AI and not self.pause:
            self.rand_AI_x = random.randrange(int(self.player.pos.x) - int(WIDTH/2),int(self.player.pos.x )+ int(WIDTH/2))
            self.rand_AI_y = random.randrange(int(self.player.pos.y) - int(HEIGHT/2),int(self.player.pos.y )+ int(HEIGHT/2))
            self.last_time_serpent = time()
            Snake_AI(self,self.rand_AI_x, self.rand_AI_y)


    def draw(self):
        # GAMELOOP -- DRAW
        pg.display.set_caption("{:0.2f}".format(self.clock.get_fps()))
        self.screen.fill(BROWN)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        score = "Score "
        score2=':'+str(self.player.snake_longueur)
        self.draw_text(score, self.fontJP, 40, BLACK ,10,10, align="Nord_Ouest")
        self.draw_text(score2, self.fontJP, 40, BLACK ,70,10, align="Nord_Ouest")

        if self.pause :
            if self.option_pause:
                self.option_screen(True)
            elif self.raccpause :
                self.raccourcis_screen(True)
            self.pause_screen()
        pg.display.flip()

    def pause_screen(self):
        self.screen.blit(self.color_paused, (0, 0))
        self.draw_text("Game Paused", self.fontJP, 105, RED, WIDTH / 2, WIDTH / 20, align="Middle")
        self.draw_text("Sliter IO ",self.fontJP, TAILLE_ECRIT_GRAND, WHITE, WIDTH/2, HEIGHT/4, align="Middle")
        self.draw_text("Press   O   for   Options",self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+55, HEIGHT/2, align="Middle")
        self.draw_text("Press  R  pour  acceder  aux  Raccourcis", self.fontJP,TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+200, HEIGHT/2+100, align="Middle")
        self.draw_text("Press  ENTREE  pour  REcommencer  une  partie",self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+310, HEIGHT/2+200, align="Middle")
        self.keys_pause_screen()

    def keys_pause_screen(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_o:
                    self.option_pause = True
                elif event.key == pg.K_r:
                    self.raccpause = True
                elif event.key == pg.K_ESCAPE:
                    self.pause = not self.pause


    def start_screen(self):
        # AFFICHE ECRAN DE DEBUT
        self.screen.fill(BGCOLOR)
        self.draw_text("Sliter IO ",self.fontJP, TAILLE_ECRIT_GRAND, WHITE, WIDTH/2, HEIGHT/4, align="Middle")
        self.draw_text("Press   O   for   Options",self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+55, HEIGHT/2, align="Middle")
        self.draw_text("Press   I   for   l Introduction",self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+119, HEIGHT/2+100, align="Middle")
        self.draw_text("Press  R  pour  acceder  aux  Raccourcis", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+200 ,HEIGHT / 2 + 200, align="Middle")
        self.draw_text("Press  ESPACE  pour  commencer  la  partie",self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+TAILLE_ECRIT_GRAND, HEIGHT/2+300, align="Middle")
        pg.display.flip()
        self.waiting_start_screens()

    def waiting_start_screens(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.playing = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        waiting = False
                        self.playing = False
                    elif event.key == pg.K_SPACE:
                        waiting = False
                    elif event.key == pg.K_o:
                        self.option_screen(False)
                    elif event.key == pg.K_i:
                        self.intro_screen()
                    elif event.key == pg.K_r:
                        self.raccourcis_screen(False)

    def option_screen(self, viapause):
        if viapause :
            self.screen.blit(self.color_paused, (0, 0))
            self.draw_text("Game Paused", self.fontJP, 105, RED, WIDTH / 2, WIDTH / 20, align="Middle")
        else :
            self.screen.fill(BGCOLOR)
        self.draw_text("Sliter IO ",self.fontJP, TAILLE_ECRIT_GRAND, WHITE, WIDTH/2, HEIGHT/4, align="Middle")
        self.draw_text("Press  M  pour  activer  desactiver   la   musique  de  fond ", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+325, HEIGHT/2, align="Middle")
        self.draw_text("Press  S  pour  activer  desactiver   les   sonds  ", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+200, HEIGHT /2+100, align="Middle")
        self.draw_text("Press  Echap pour revenir en arriere ", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4+115,HEIGHT / 2 + 200, align="Middle")
        pg.display.flip()
        self.waiting_option_screens()
        if viapause:
            self.option_pause = False
        else:
            self.start_screen()


    def waiting_option_screens(self, ):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                print(self.musique_fond, self.sond_ambiant)
                if event.type == pg.QUIT:
                    waiting = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE and not self.option_pause:
                        waiting = False
                    elif event.key == pg.K_ESCAPE and  self.option_pause:
                        self.option_pause = not self.option_pause
                        waiting = False
                    elif event.key == pg.K_SEMICOLON:
                        self.musique_fond = not self.musique_fond
                    elif event.key == pg.K_SEMICOLON and self.option_pause:
                        pg.mixer.music.stop()
                        self.musique_fond = not self.musique_fond
                    elif event.key == pg.K_s:
                        self.sond_ambiant = not self.sond_ambiant

    def raccourcis_screen(self, viapause):
        if viapause :
            self.screen.blit(self.color_paused, (0, 0))
            self.draw_text("Game Paused", self.fontJP, 105, RED, WIDTH / 2, WIDTH / 20, align="Middle")

            self.image1 = self.fleche_up_paused
            self.screen.blit(self.image1, (WIDTH / 4 - 65, HEIGHT / 2 - 75))

            self.image2 = self.fleche_gauche_paused
            self.screen.blit(self.image2, (WIDTH / 4 - 65, HEIGHT / 2 + 35))

            self.image3 = self.fleche_droite_paused
            self.screen.blit(self.image3, (WIDTH / 4 - 65, HEIGHT / 2 + 135))

        else :
            self.screen.fill(BGCOLOR)

            self.image1 = self.fleche_up
            self.screen.blit(self.image1, (WIDTH / 4 - 65, HEIGHT / 2 - 75))

            self.image2 = self.fleche_gauche
            self.screen.blit(self.image2, (WIDTH / 4 - 65, HEIGHT / 2 + 35))

            self.image3 = self.fleche_droite
            self.screen.blit(self.image3, (WIDTH / 4 - 65, HEIGHT / 2 + 135))

        self.draw_text("Sliter IO ",self.fontJP, TAILLE_ECRIT_GRAND, WHITE, WIDTH/2, HEIGHT/4, align="Middle")

        self.draw_text("Z ou", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4-125, HEIGHT/2, align="Middle")
        self.draw_text("pour avancer", self.fontJP,TAILLE_ECRIT_NORMAL, WHITE, WIDTH/3+35, HEIGHT/2, align="Middle")

        self.draw_text("Q ou", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4-125, HEIGHT/2+100, align="Middle")
        self.draw_text("pour tourner vers la gauche ", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/3+200, HEIGHT/2+100, align="Middle")

        self.draw_text("D ou", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/4-125, HEIGHT/2+200, align="Middle")
        self.draw_text("pour tourner vers la droite", self.fontJP, TAILLE_ECRIT_NORMAL, WHITE, WIDTH/3+195, HEIGHT/2+200, align="Middle")

        pg.display.flip()
        self.waiting_racc_screens()
        if viapause:
            self.raccpause  = False
        else:
            self.start_screen()

    def waiting_racc_screens(self,):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE and not self.raccpause :
                        waiting = False
                    elif event.key == pg.K_ESCAPE and  self.raccpause :
                        self.raccpause = not self.raccpause
                        waiting = False

    def intro_screen(self):
        pass

    def end_screen(self):
        # AFFICHE ECRAN DE FIN
        pass

g = Game()
while g.running:
    g.new()
    g.end_screen()

pg.quit()

import pygame as pg
import random
from os import path, getcwd, environ
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

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Images')
        self.sound_folder = path.join(game_folder, 'Sounds')

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
        pg.mixer.music.load(path.join(self.sound_folder,CODE_MUSIC))
        pg.mixer.music.set_volume(0.03)



        self.run()

    def run(self):
        # GAMELOOP
        self.playing=True
        pg.mixer.music.play(loops=-1)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
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

        self.candy_tmp = []
        self.candyList_Compteur=-1
        if time() - self.last_time_candy > COOLDOWN_SPAWN_BONBON:
            self.rand_bonbon_X_Time = random.randrange(int(self.player.pos.x) - int(WIDTH/2),int(self.player.pos.x )+ int(WIDTH/2))
            self.rand_bonbon_Y_Time = random.randrange(int(self.player.pos.y) - int(HEIGHT/2),int(self.player.pos.y )+ int(HEIGHT/2))
            self.last_time_candy = time()
            self.candy_List.append((self.rand_bonbon_X_Time, self.rand_bonbon_Y_Time))
            Candy(self, self.rand_bonbon_X_Time, self.rand_bonbon_Y_Time)

        if time() - self.last_time_serpent > COOLDOWN_SPAWN_AI:
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
        pg.display.flip()

    def show_start_screen(self):
        # AFFICHE ECRAN DE DEBUT
        pass

    def show_end_screen(self):
        # AFFICHE ECRAN DE FIN
        pass



g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_end_screen()

pg.quit()

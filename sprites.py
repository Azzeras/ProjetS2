import pygame as pg
from settings import *
import math
import random
vecteur=pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.serpent_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vecteur(x * TAILLE_SERPENT , y * TAILLE_SERPENT)
        self.vit = vecteur(0,0)
        self.acc = vecteur(0,0)
        self.rot = 0

        self.snake_longueur = 1
        self.snakeList= []

    def get_keys(self):
        self.rot_speed=0
        self.vit=vecteur(0,0)
        self.acc=vecteur(0,0)
        keys=pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.acc = vecteur(PLAYER_SPEED,0).rotate(-self.rot)
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.rot_speed= PLAYER_ROT_SPEED
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.rot_speed = -PLAYER_ROT_SPEED

    def update(self):
        self.get_keys()
        self.rot += self.rot_speed %360
        self.image = pg.transform.rotate(self.game.serpent_img, self.rot)
        self.acc += self.vit * PLAYER_FRIC
        self.vit += self.acc
        self.pos += self.vit +0.5*self.acc
        self.rect = self.image.get_rect()
        self.rect.center=self.pos



        self.tmp=[]
        self.tmp.append(self.pos.x)
        self.tmp.append(self.pos.y)
        self.snakeList.append(self.tmp)
        for i in self.snakeList:
            Body_player(self.game ,(i[0]-5,i[1]),self.snake_longueur, self.rot)
        if len(self.snakeList) > self.snake_longueur:
            del self.snakeList[0]

        self.collide_with_player_head()

    def collide_with_player_head(self):
        hits = pg.sprite.spritecollide(self.game.player, self.game.bodies_ai, False)
        if hits :
            pg.mixer.music.pause()
            pg.mixer.pause()
            sound = random.choice(self.game.game_over_sound)
            sound.set_volume(1)
            sound.play()
            self.kill()
            self.game.show_end_screen()


class Snake_AI(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.snakeAIs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game

        self.image = game.serpent_img
        self.rect = self.image.get_rect()
        self.pos = vecteur(x ,y)
        self.vit = vecteur(0,0)
        self.acc = vecteur(0,0)
        self.rect.center = self.pos

        self.snake_longueur_AI = 1
        self.snakeList_AI= []
        if len(self.game.candy_List) !=0 :
            self.tmp=random.randint(0, len(self.game.candy_List)-1)
        else:
            self.tmp = 0
    def update(self):
        if len(self.game.candy_List) ==0 :
            self.rot = 0
        elif len(self.game.candy_List) <= self.tmp :
            self.rot = 0
        else :
            self.rot = (self.game.candy_List[self.tmp] - self.pos).angle_to(vecteur(1, 0))

        self.image = pg.transform.rotate(self.game.serpent_img, self.rot)
        self.rect = self.image.get_rect()

        self.acc = vecteur(PLAYER_ROT_SPEED,0).rotate(-self.rot)
        self.acc += self.vit * -1
        self.vit += self.acc
        self.pos += self.vit + 0.5 * self.acc
        self.rect.center = self.pos

        self.collide_with_player_body()


        self.tmp2=[]
        self.tmp2.append(self.pos.x)
        self.tmp2.append(self.pos.y)
        self.snakeList_AI.append(self.tmp2)
        for i in self.snakeList_AI:
            Body_AI(self.game ,(i[0]-5,i[1]),self.snake_longueur_AI, self.rot)
        if len(self.snakeList_AI) > self.snake_longueur_AI:
            del self.snakeList_AI[0]




    def collide_with_player_body(self):
        hitss = pg.sprite.groupcollide(self.game.bodies, self.game.snakeAIs, False, True)
        for hit in hitss:
            hit.snake_longueur += self.snake_longueur_AI
            self.game.player.snake_longueur += self.snake_longueur_AI
            random.choice(self.game.kill_ai_sound).play()


class Body_player(pg.sprite.Sprite):
    def __init__(self, game , pos, snake_Longueur, rot):
        self.groups = game.all_sprites, game.bodies
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.snake_longueur = snake_Longueur
        self.rot = rot
        self.snakeList=[]
        self.snakeList_AI=[]
        self.image=game.serpent_img_body
        self.rect = self.image.get_rect()
        self.image = pg.transform.rotate(self.game.serpent_img_body, self.rot)


        self.pos=vecteur(pos)
        self.rect.center=pos

    def update(self):
        self.snakeList.append(self.rect)
        if len(self.snakeList) > self.snake_longueur:
            self.kill()

class Body_AI(pg.sprite.Sprite):
    def __init__(self, game , pos, snake_Longueur, rot):
        self.groups = game.all_sprites, game.bodies_ai
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.snake_longueur = snake_Longueur
        self.rot = rot
        self.snakeList_AI=[]
        self.image=game.serpent_img_body
        self.rect = self.image.get_rect()
        self.image = pg.transform.rotate(self.game.serpent_img_body, self.rot)


        self.pos=vecteur(pos)
        self.rect.center=pos

    def update(self):
        self.snakeList_AI.append(self.rect)
        if len(self.snakeList_AI) > self.snake_longueur:
            self.kill()


class Candy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.candies
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game

        self.img_list=[game.candy1_img, game.candy2_img ,game.candy3_img, game.candy4_img, game.candy5_img, game.candy6_img, game.candy7_img, game.candy8_img, game.candy9_img, game.candy10_img, game.candy11_img, game.candy12_img, game.candy13_img, game.candy14_img, game.candy15_img, ]
        self.candy_img = self.img_list[random.randint(0,len(self.img_list)-1)]

        self.image = self.candy_img
        self.rect = self.image.get_rect()
        self.pos = vecteur(x, y)
        self.rect.center = self.pos
        self.rot = 0



    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vecteur(1,0))
        self.image = pg.transform.rotate(self.candy_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.collide_AI_with_candy()
        self.collide_player_with_candy()


    def recherche_indice_candylist(self, posx,posy):
        for i in range (len(self.game.candy_List)):
            r1 = range(self.game.candy_List[i][0]- TAILLE_SERPENT-10,self.game.candy_List[i][0]+ TAILLE_SERPENT+10)
            r2 = range(self.game.candy_List[i][1]- TAILLE_SERPENT-10,self.game.candy_List[i][1]+ TAILLE_SERPENT+10)
            posx=round(posx)
            posy=round(posy)
            if posx in r1 and posy in r2:
                return i

    def collide_player_with_candy(self):
        hits = pg.sprite.collide_rect(self.game.player,self)
        if hits :
            sound=random.choice(self.game.eat_candy_sound)
            sound.set_volume(.5)
            sound.play()
            self.game.player.snake_longueur += 1
            indice = self.recherche_indice_candylist(self.pos.x, self.pos.y,)
            if indice != None:
                del self.game.candy_List[indice]
            self.kill()

    def collide_AI_with_candy(self):
        hitss = pg.sprite.groupcollide(self.game.snakeAIs, self.game.candies, False, True)
        for hit in hitss:
            hit.snake_longueur_AI +=1
            indice = self.recherche_indice_candylist(hit.pos.x, hit.pos.y)
            if indice != None :
                del self.game.candy_List[indice]

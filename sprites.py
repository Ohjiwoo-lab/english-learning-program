import pygame as pg
from settings import *
vec=pg.math.Vector2

class Character(pg.sprite.Sprite):
    
    #Game클래스를 넘겨주기 위해서
    def __init__(self,game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        
        self.walking=False
        self.jumping=False
        self.load_images()
        self.image=self.standing_frames[0]
        self.rect=self.image.get_rect()
        character_size = character.get_rect().size  #캐릭터 사이즈
        self.rect.center=(character_size[0]/2,character_size[1]/2)
        self.pos=vec(0,80) #캐릭터 위치
        
    def load_images(self):
        self.standing_frames = [self.game.stand.get_image()]


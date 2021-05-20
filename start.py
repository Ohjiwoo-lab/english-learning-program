#게임시작

import pygame as pg
from settings import *
 
class Game:
    def __init__(self):
        pg.init() #파이 게임을 만들기 위해서는 꼭 초기화를 해야함.
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        #화면 크기 지정
        pg.display.set_caption(TITLE)
        self.clock=pg.time.Clock() #초당 프레임 실행을 위한 변수
        self.running=True #게임이 끝났는지 아닌지를 확인하기 위한 변수
        
    def run(self):
        
        self.playing=True #게임이 True일때 진행
        
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
    def events(self):
        
        for event in pg.event.get() :
            #window창이 닫혔는지 확인
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                    #while문을 빠져나옴
                self.running=False #게임이 끝남.
                
    def show_start_screen(self):
        self.running=True

    def draw(self):
        # 배경 이미지 불러오기
        background = pg.image.load(BACKGROUND)
        background = pg.transform.scale(background,(1000,800))
        self.screen.blit(background,(0,0))
        pg.display.flip() #pg.display.update()랑 기능이 같나? ->다름
        #flip()은 전체 update update는 한 세션만 업데이트 
        
game=Game()
game.show_start_screen()

while game.running:
    game.run()
    
pg.quit()
            
import pygame
from settings import *
from sprites import *
import random
import time
from WordManager import WordManager
from PIL import Image, ImageTk
from global_vari import wordlist,word_img
# 메인 클래스
        
class Game(WordManager):
    def __init__(self):
        WordManager.__init__(self)
        self.wordread()
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.run = True
        self.bg_img = pygame.image.load(BACKGROUND)  # 배경 이미지
        score_heart = HEART(TILE_SIZE // 2, TILE_SIZE // 2)  # 목숨 이미지 생성(화면 상단에)
        HEART_GROUP.add(score_heart)

        # 초기화
        self.score = 0
        self.game_over = 0
        self.level = 0
        self.main_menu = True
        self.heart = 0
        self.count=0
        self.world = World(self.level)  # 지형 생성
        self.player = Player(50, HEIGHT - 130)  # 캐릭터 생성
        self.card=0
        self.wrong_card=[]

        # 각종 버튼 생성
        start_img = pygame.image.load(START)
        start_img = pygame.transform.scale(start_img, (TILE_SIZE * 8, TILE_SIZE * 4))
        exit_img = pygame.image.load(EXIT_IMG)
        exit_img = pygame.transform.scale(exit_img, (TILE_SIZE * 8, TILE_SIZE * 4))

        exit_img2 = pygame.transform.scale(exit_img, (TILE_SIZE * 7, TILE_SIZE * 3))
        self.restart_img = pygame.image.load(RESTART_IMG)
        self.restart_img = pygame.transform.scale(self.restart_img, (TILE_SIZE * 7, TILE_SIZE * 3))

        self.start_button = Button(WIDTH // 2 - 360, HEIGHT // 2, start_img)
        self.exit_button = Button(WIDTH // 2 + 50, HEIGHT // 2, exit_img)
        self.restart_button = Button(WIDTH // 2 - 320, HEIGHT // 2 + 40, self.restart_img)
        self.exit_button2 = Button(WIDTH // 2 + 50, HEIGHT // 2 + 40, exit_img2)
        self.exit_button3 = Button(350, 440, exit_img2)

        running_img = pygame.image.load(RUNNING)
        self.running_img = pygame.transform.scale(running_img, (100, 160))

        self.button_img = pygame.image.load(BUTTON)

        # font
        self.font = pygame.font.SysFont('Bauhaus 93', 90)
        self.font_score = pygame.font.SysFont('Bauhaus 93', 30)
        self.font2 = pygame.font.SysFont('Consolas', 30)
        self.font3 = pygame.font.SysFont('Helvetica', 20)
        self.font4 = pygame.font.SysFont('맑은 고딕', 60)
        self.font5 = self.font = pygame.font.SysFont('Bauhaus 93', 150)
        self.font6 = pygame.font.SysFont('Consolas', 40)
    
    # 메인 함수
    def new(self):
        
        CLOCK.tick(FPS)

        SCREEN.blit(self.bg_img, (0, 0))
        SCREEN.blit(self.running_img, (170, 250))

        if self.main_menu == True:  # 메인 화면에서
            # 나가기 버튼을 눌렀을 때
            if self.exit_button.draw():
                self.run = False
            # 시작하기 버튼을 눌렀을 때
            if self.start_button.draw():
                self.main_menu = False
        else:
                 # 게임이 진행중
            SCREEN.blit(self.bg_img, (0, 0))
            self.world.draw()

            if self.game_over == 0:  # 아직 살아서 게임 진행
                PLATFORM_GROUP.draw(SCREEN)
                if pygame.sprite.spritecollide(self.player, COIN_GROUP, True):  # 캐릭터가 연필을 먹었을 때
                    COIN_FX.play()
                    self.score += 1
                    self.card = random.randint(0,len(wordlist)-1)
                    for j in range(3):
                          a=random.randint(0,len(wordlist)-1)
                          if self.card!=a:
                              self.wrong_card.append(a)
                          else :
                              j-=1
                    # 문제 풀기
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.counter, self.text = 5, '5'.rjust(3)  # 시간 제한 5초

                    background = pygame.image.load(GAME_BACKGROUND)
                    SCREEN.blit(background, (170, 160))

                    # 문제 등장
                    self.draw_text("What word is this picture?", self.font2, black, 190, 180)
                    img = pygame.image.load("photo_img/"+wordlist[self.card].get_english()+".png")
                    img_right = pygame.transform.scale(img, (300, 200))
                    SCREEN.blit(img_right, (190, 280))

                    self.xlab = 520
                    self.ylab = 250

                    # 선택지 이미지 등장
                    self.btn1 = Button(self.xlab, self.ylab, self.button_img)
                    self.btn2 = Button(self.xlab, self.ylab + 90, self.button_img)
                    self.btn3 = Button(self.xlab, self.ylab + 180, self.button_img)
                    self.btn4 = Button(self.xlab, self.ylab + 270, self.button_img)

                    self.running = True
                    while self.running:  # 반복문으로 타이머 동작
                        self.solve()  # 문제 푸는 함수 호출

                self.draw_text('X ' + str(3 - self.heart), self.font_score, blue, TILE_SIZE, 6)  # 현재 목숨 상태 표시

            # 3번의 목숨이 다 깎이면 game over
            if 3 - self.heart == 0:
                self.game_over = -1

            COIN_GROUP.draw(SCREEN)
            HEART_GROUP.draw(SCREEN)

            PLATFORM_GROUP.update()
            self.game_over = self.player.update(self.game_over, self.world)

            if self.score == self.world.score:  # Stage의 모든 연필을 획득했을 때(다음 Stage로 가는 문 생성)
                EXIT_GROUP.add(self.world.exit)
                EXIT_GROUP.draw(SCREEN)


            # 죽음
            if self.game_over == -1:
                SCREEN.blit(self.bg_img, (0, 0))
                self.draw_text("GAME OVER", self.font5, red, 120, 240)  # 게임 오버
                END_FX.play()

                if self.restart_button.draw():  # 다시하기 버튼을 눌렀을 때(첫 번째 Stage 부터 시작)
                    self.world_data = []
                    if self.level != 0:
                        self.level -= 1
                    self.reset_level()
                    self.game_over = 0
                    self.score = 0
                    self.heart = 0
                    END_FX.stop()

                if self.exit_button2.draw():  # 나가기 버튼을 눌렀을 때
                    self.run = False


            # 다음 Stage로 넘어가는 문을 통과했을 때(level이 2보다 작으면 다음 Stage로, 2이면 game 성공!)
            if self.game_over == 1:
                self.level += 1
                if self.level < MAX_LEVEL:
                    self.world_data = []
                    self.reset_level()
                    self.game_over = 0
                    self.score = 0

                # 게임 통과
                else:
                    SCREEN.blit(self.bg_img, (0, 0))
                    self.draw_text("GAME CLEAR", self.font5, blue, 120, 240)  # 게임 클리어
                    CHEERS_FX.play()

                    if self.exit_button3.draw():  # 나가기 버튼을 눌렀을 때
                        self.run = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        pygame.display.update()


    def solve(self):  
        
        
        # 타이머 이미지
        timer_background = pygame.image.load(TIMER_BACKGROUND)
        timer_background = pygame.transform.scale(timer_background, (50, 50))
        SCREEN.blit(timer_background, (730, 170))

        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                self.counter -= 1
                if self.counter > 0:
                    self.text = str(self.counter).rjust(3)
                else:
                    self.running = False
                    self.draw_text("WRONG", self.font, red, 200, 300)
                    pygame.display.flip()
                    self.heart += 1
                    WRONG_FX.play()
                    time.sleep(1)

            if self.btn1.draw():
                CORRECT_FX.play()
                self.draw_text(wordlist[self.card].get_english(), self.font4, black, self.xlab + 60, self.ylab + 10)  # 선택지를 선택하였을 때 단어가 사라지는 현상이 발생하여 추가함
                self.draw_text("CORRECT", self.font, blue, 200, 300)
                pygame.display.flip()
                self.running = False
                time.sleep(1)

            elif self.btn2.draw():
                WRONG_FX.play()
                self.draw_text(wordlist[self.card].get_english(), self.font4, black, self.xlab + 60, self.ylab + 10)
                self.draw_text(wordlist[self.wrong_card[0]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 90 + 10)
                self.draw_text("WRONG", self.font, red, 250, 300)
                pygame.display.flip()
                self.running = False
                self.heart += 1
                time.sleep(1)

            elif self.btn3.draw():
                WRONG_FX.play()
                self.draw_text(wordlist[self.card].get_english(), self.font4, black, self.xlab + 60, self.ylab + 10)
                self.draw_text(wordlist[self.wrong_card[0]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 90 + 10)
                self.draw_text(wordlist[self.wrong_card[1]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 180 + 10)
                self.draw_text("WRONG", self.font, red, 250, 300)
                pygame.display.flip()
                self.running = False
                self.heart += 1
                time.sleep(1)

            elif self.btn4.draw():
                WRONG_FX.play()
                self.draw_text(wordlist[self.card].get_english(), self.font4, black, self.xlab + 60, self.ylab + 10)
                self.draw_text(wordlist[self.wrong_card[0]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 90 + 10)
                self.draw_text(wordlist[self.wrong_card[1]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 180 + 10)
                self.draw_text(wordlist[self.wrong_card[2]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 270 + 10)
                self.draw_text("WRONG", self.font, red, 250, 300)
                pygame.display.flip()
                self.running = False
                self.heart += 1
                time.sleep(1)
        try:
            # 실제 선택지 단어 등장
            self.draw_text(wordlist[self.card].get_english(), self.font4, black, self.xlab + 60, self.ylab + 10)
            self.draw_text(wordlist[self.wrong_card[0]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 90 + 10)
            self.draw_text(wordlist[self.wrong_card[1]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 180 + 10)
            self.draw_text(wordlist[self.wrong_card[2]].get_english(), self.font4, black, self.xlab + 60, self.ylab + 270 + 10)
        except:
            pass
        
        SCREEN.blit(self.font6.render(self.text, True, black), (703, 180))  # 타이머 글씨 삽입
        pygame.display.flip()


    # 화면에 글씨 삽입
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        SCREEN.blit(img, (x, y))


    # 레벨 조절
    def reset_level(self):
        self.player.reset(50, HEIGHT - 130)
        PLATFORM_GROUP.empty()
        COIN_GROUP.empty()
        EXIT_GROUP.empty()

        self.world = World(self.level)


# 각종 버튼 생성
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        SCREEN.blit(self.image, self.rect)

        return action

g = Game()
while g.run:
    g.new()

pygame.quit()

#게임시작

import pygame
from settings import *
from sprites import *
import random
import time


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.run = True

        self.bg_img = pygame.image.load(BACKGROUND)
        score_heart = HEART(TILE_SIZE // 2, TILE_SIZE // 2)
        HEART_GROUP.add(score_heart)
        self.score = 0
        self.game_over = 0
        self.level = 0
        self.main_menu = True
        self.heart = 0

        self.world_data = WORLD_DATA

        self.world = World(self.world_data)
        self.player = Player(50, HEIGHT - 130)

        start_img = pygame.image.load(START)
        start_img = pygame.transform.scale(start_img, (TILE_SIZE * 8, TILE_SIZE * 4))
        exit_img = pygame.image.load(EXIT_IMG)
        exit_img = pygame.transform.scale(exit_img, (TILE_SIZE * 8, TILE_SIZE * 4))

        self.start_button = Button(WIDTH // 2 - 360, HEIGHT // 2, start_img)
        self.exit_button = Button(WIDTH // 2 + 50, HEIGHT // 2, exit_img)

        running_img = pygame.image.load(RUNNING)
        self.running_img = pygame.transform.scale(running_img, (100, 160))

        self.button_img = pygame.image.load(BUTTON)

        # font
        self.font = pygame.font.SysFont('Bauhaus 93', 70)
        self.font_score = pygame.font.SysFont('Bauhaus 93', 30)
        self.font2 = pygame.font.SysFont('Consolas', 30)
        self.font3 = pygame.font.SysFont('Helvetica', 20)
        self.font4 = pygame.font.SysFont('맑은 고딕', 60)

    def new(self):
        CLOCK.tick(FPS)

        SCREEN.blit(self.bg_img, (0, 0))
        SCREEN.blit(self.running_img, (170, 250))

        if self.main_menu == True:
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

            if self.game_over == 0:
                PLATFORM_GROUP.draw(SCREEN)
                if pygame.sprite.spritecollide(self.player, COIN_GROUP, True):
                    COIN_FX.play()
                    self.score += 1

                    # 문제 풀기
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.counter, self.text = 10, '10'.rjust(3)
                    self.running = True
                    while self.running:
                        self.solve()

                self.draw_text('X ' + str(3 - self.heart), self.font_score, blue, TILE_SIZE, 6)

            COIN_GROUP.draw(SCREEN)
            HEART_GROUP.draw(SCREEN)

            PLATFORM_GROUP.update()
            self.game_over = self.player.update(self.game_over, self.world)

            if self.score == self.world.score:
                EXIT_GROUP.draw(SCREEN)

            # 죽음
            if self.game_over == -1:
                self.draw_text('X ' + str(3 - self.heart), self.font_score, blue, TILE_SIZE, 6)
                self.draw_text("GAME OVER", self.font, red, 250, 300)  # 게임 오버

            # exit 문으로 빠져나감
            if self.game_over == 1:
                self.level += 1
                if self.level < MAX_LEVEL:
                    self.world_data = []
                    self.reset_level(self.level)
                    self.game_over = 0
                    self.score = 0

                # 게임 통과
                else:
                    self.draw_text("GAME CLEAR", self.font, blue, 250, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        pygame.display.update()


    def solve(self):
        background = pygame.image.load(GAME_BACKGROUND)
        SCREEN.blit(background, (170, 160))

        self.draw_text("What word is this picture?", self.font2, black, 190, 180)
        img = pygame.image.load("C:/english-learning-program/photo_img/a.png")
        img_right = pygame.transform.scale(img, (300, 200))
        SCREEN.blit(img_right, (190, 260))

        xlab = 520
        ylab = 250

        btn1 = select_Button(xlab, ylab, self.button_img)
        btn2 = select_Button(xlab, ylab + 90, self.button_img)
        btn3 = select_Button(xlab, ylab + 180, self.button_img)
        btn4 = select_Button(xlab, ylab + 270, self.button_img)

        self.draw_text("A", self.font4, black, xlab + 60, ylab + 10)
        self.draw_text("About", self.font4, black, xlab + 60, ylab + 90 + 10)
        self.draw_text("Cap", self.font4, black, xlab + 60, ylab + 180 + 10)
        self.draw_text("Software", self.font4, black, xlab + 60, ylab + 270 + 10)

        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                self.counter -= 1
                if self.counter > 0:
                    self.text = str(self.counter).rjust(3)
                else:
                    self.running = False
                    self.draw_text("FALSE", self.font, red, 220, 260)
                    self.heart += 1

            if btn1.draw():
                self.draw_text("CORRECT", self.font, blue, 220, 260)
                self.running = False

            if btn2.draw():
                self.draw_text("False", self.font, red, 220, 260)
                self.running = False
                self.heart += 1

            if btn3.draw():
                self.draw_text("False", self.font, red, 220, 260)
                self.running = False
                self.heart += 1

            if btn4.draw():
                self.draw_text("False", self.font, red, 220, 260)
                self.running = False
                self.heart += 1

            if 3 - self.heart == 0:
                self.game_over = -1

        SCREEN.blit(self.font2.render(self.text, True, red), (720, 180))
        pygame.display.flip()


    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        SCREEN.blit(img, (x, y))


    def reset_level(self, level):
        self.player.reset(50, HEIGHT - 130)
        PLATFORM_GROUP.empty()
        COIN_GROUP.empty()
        EXIT_GROUP.empty()

        if level == 1:
            self.world_data = WORLD_DATA1

        self.world = World(self.world_data)



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


class select_Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        # draw button
        SCREEN.blit(self.image, self.rect)

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

        return action


    
g = Game()
while g.run:
        g.new()

pygame.quit()



#게임시작

import pygame
from settings import *
from sprites import *

# 추후에 클래스로 변경 예정
pygame.init()

pygame.display.set_caption(TITLE)

# 배경
bg_img = pygame.image.load(BACKGROUND)

# 지형/캐릭터 생성
world = World(WORLD_DATA)
player = Player(70, HEIGHT - 130, world)

run = True

# 아직 게임이 진행중인 동안 화면 업데이트
while run:
    CLOCK.tick(FPS)

    SCREEN.blit(bg_img, (0, 0))

    world.draw()
    PLATFORM_GROUP.draw(SCREEN)
    COIN_GROUP.draw(SCREEN)

    PLATFORM_GROUP.update()
    player.update()

    if pygame.sprite.spritecollide(player, COIN_GROUP, True):
        COIN_FX.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()



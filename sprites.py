
import pygame
from settings import *

# 지형 클래스
class World():
    def __init__(self, data):

        self.tile_list = []

        # load images
        self.book_img = pygame.image.load('image/book.png')

        self.row_count = 0
        for row in data:
            self.col_count = 0
            for tile in row:
                if tile == 1:
                    self.create()
                if tile == 2:
                    platform = Platform(self.col_count * TILE_SIZE, self.row_count * TILE_SIZE, -1, 0)
                    PLATFORM_GROUP.add(platform)
                if tile == 3:
                    platform = Platform(self.col_count * TILE_SIZE, self.row_count * TILE_SIZE, 0, 1)
                    PLATFORM_GROUP.add(platform)
                if tile == 4:
                    coin = Coin(self.col_count * TILE_SIZE + (TILE_SIZE // 2), self.row_count * TILE_SIZE + TILE_SIZE)
                    COIN_GROUP.add(coin)
                self.col_count += 1
            self.row_count += 1

    def create(self):
        img = pygame.transform.scale(self.book_img, (TILE_SIZE, TILE_SIZE))
        img_rect = img.get_rect()
        img_rect.x = self.col_count * TILE_SIZE
        img_rect.y = self.row_count * TILE_SIZE
        tile = (img, img_rect)
        self.tile_list.append(tile)

    def draw(self):
        for tile in self.tile_list:
            SCREEN.blit(tile[0], tile[1])


# 캐릭터 클래스
class Player():
    def __init__(self, x, y, world):
        self.world = world

        # 시작할 때 정면 보기
        img = pygame.image.load(FRONT)
        self.image = pygame.transform.scale(img, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'C:/english-learning-program/image/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (50, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        ''' # 시작할 때 앞을 볼 것인가, 옆을 볼 것인가(이것을 하면 옆을 본다.)      
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        '''
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        # get keypresses
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            JUMP_FX.play()
            self.vel_y = -15
            self.jumped = True

        if key[pygame.K_SPACE] == False:
            self.jumped = False

        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1

        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1

        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision
        self.in_air = True
        for tile in self.world.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False

        # 화면 밖으로 안 나가도록
        if self.rect.x + dx < 0:
            dx = 0
        if self.rect.x + dx > WIDTH - 50:
            dx = 0

        # check for collision with platforms
        for platform in PLATFORM_GROUP:
            # collision in the x direction
            if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below platform
                if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                    self.vel_y = 0
                    dy = platform.rect.bottom - self.rect.top
                # check if above platform
                elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                    self.rect.bottom = platform.rect.top - 1
                    self.in_air = False
                    dy = 0
                # move sideways with the platform
                if platform.move_x != 0:
                    self.rect.x += platform.move_direction * -1

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0

        # draw player onto screen
        SCREEN.blit(self.image, self.rect)



# 움직이는 지형 생성
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('image/book.png')
        self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


# 연필(획득하면 문제 나오도록 할 것)
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('image/pencil.png')
        self.image = pygame.transform.scale(img, (TILE_SIZE // 2, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


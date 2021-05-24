#pygame2021.05.20 start - 21.06.5 end
import pygame

#settings은 변수 설정을 위한 파일

# 타이틀
TITLE="python_project game 'english learning game'"

#pygame window창 크기 설정
WIDTH=1000
HEIGHT=800

CLOCK = pygame.time.Clock()
FPS=60 #하나의 프레임당 1컷 60s
HEART=3 #목숨

PLATFORM_GROUP = pygame.sprite.Group()
COIN_GROUP = pygame.sprite.Group()

# 화면
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# 음악
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.mixer.music.load('C:/english-learning-program/sound/supermario_music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
COIN_FX = pygame.mixer.Sound('C:/english-learning-program/sound/supermario_coin.wav')
COIN_FX.set_volume(0.5)
JUMP_FX = pygame.mixer.Sound('C:/english-learning-program/sound/supermario_jump.wav')
JUMP_FX.set_volume(0.5)

# define game variables
TILE_SIZE = 40  # 한 칸의 크기(지형 생성 시)

'''
#Player_properties
#아직 왜 필요한지 모르겠지만, 일단 적고 이해한다. 
PLAYER_ACC = 1.0 #플레이어의 초기 가속도 => 속도를 위한거 같음.
PLAYER_FRICTION = -0.2 #초기 마찰 계수 => 블록과 충돌이 발생했을때 딱 붙었을땐 충돌검사가 일어나지 않음
#바닥과 -2정도는 차이가 나야지 충돌 검사를 함.
PLAYER_GRAVITY = 0.8 #플레이어가 받을 중력 크기 =>이게 왜필요할까?
PLAYER_JUMP = 20.0 #플레이어 점프 값
#Starting platforms 이동하는 블록을 제외하곤 이걸로 짜면될듯?
PLATFORM_LIST=[(50, 700, 50, 10)]
#x=0 y=800-40:760, 너비 1000,높이 40 초기값
PLAYER_SPEED = 0.5
'''

# 이미지
BACKGROUND="C:/english-learning-program/image/super_background2.png"
BOOK="C:/english-learning-program/image/book.png"
FRONT="C:/english-learning-program/image/front1.png"

# 25 x 20 지형
WORLD_DATA = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  # 16
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # 18
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 19
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 20
]


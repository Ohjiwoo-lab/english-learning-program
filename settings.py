#pygame2021.05.20 start - 21.06.5 end
import pygame

#settings은 변수 설정을 위한 파일

# 화면 타이틀
TITLE="python_project game 'english learning game'"

# pygame window 창 크기 설정
WIDTH = 1000
HEIGHT = 800

# 프레임 설정
CLOCK = pygame.time.Clock()
FPS = 100  # 하나의 프레임당 1컷 100s

# 게임 레벨
MAX_LEVEL = 2

# 그룹(장애물, 연필 등)
PLATFORM_GROUP = pygame.sprite.Group()
COIN_GROUP = pygame.sprite.Group()
HEART_GROUP = pygame.sprite.Group()
EXIT_GROUP = pygame.sprite.Group()

# 화면 생성
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# 음악, 효과음
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.mixer.music.load('sound/supermario_music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
COIN_FX = pygame.mixer.Sound('sound/supermario_coin.wav')
COIN_FX.set_volume(0.5)
JUMP_FX = pygame.mixer.Sound('sound/supermario_jump.wav')
JUMP_FX.set_volume(0.5)
WRONG_FX = pygame.mixer.Sound('sound/wrong.mp3')
WRONG_FX.set_volume(1)
CORRECT_FX = pygame.mixer.Sound('sound/correct.wav')
CORRECT_FX.set_volume(1)
CHEERS_FX = pygame.mixer.Sound('sound/cheers2.mp3')
CHEERS_FX.set_volume(1)
END_FX = pygame.mixer.Sound('sound/gameover.MP3')
END_FX.set_volume(1)

# 색
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 화면 분할 타일 크기
TILE_SIZE = 40  # 한 칸의 크기(지형 생성 시)

# 이미지
BACKGROUND="image/super_background2.png"
BOOK="image/book.png"
FRONT="image/front1.png"
HEART_IMG="image/heart.png"
EXIT="image/supermario_exit.png"
PENCIL="image/pencil.png"
RUNNING="image/Running1.png"
START="image/start.png"
EXIT_IMG="image/exit_img.png"
BUTTON="image/game_selection.png"
GAME_BACKGROUND="image/supermario_game_background.png"
RESTART_IMG="image/restart_img.png"
TIMER_BACKGROUND="image/timer_background.png"


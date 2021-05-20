#pygame2021.05.20 start - 21.06.5 end

#settings은 변수 설정을 위한 파일

TITLE="python_project game 'english learning game'"

#pygame window창 크기 설정
WIDTH=1000
HEIGHT=800
FPS=20 #하나의 프레임당 1컷 60s

#Player_properties
#아직 왜 필요한지 모르겠지만, 일단 적고 이해한다. 
PLAYER_ACC = 1.0 #플레이어의 초기 가속도 => 속도를 위한거 같음.
PLAYER_FRICTION = -0.2 #초기 마찰 계수 => 블록과 충돌이 발생했을때 딱 붙었을땐 충돌검사가 일어나지 않음
#바닥과 -2정도는 차이가 나야지 충돌 검사를 함.
PLAYER_GRAVITY = 0.8 #플레이어가 받을 중력 크기 =>이게 왜필요할까?
PLAYER_JUMP = 20.0 #플레이어 점프 값
#Starting platforms 이동하는 블록을 제외하곤 이걸로 짜면될듯?
PLATFORM_LIST=[(0, HEIGHT - 80, WIDTH, 80)]
#x=0 y=800-40:760, 너비 1000,높이 40 초기값

BACKGROUND="C:/python_game/image/background1.png"
BOTTOM="C:/python_game/image/bottom.png"

STAND="C:/python_game/image/front.png"
JUMP="C:/python_game/image/front4.png"
RIGHTJUMP="C:/python_game/image/running3.png"
RIGHT="C:/python_game/image/right.png"
LEFT="C:/python_game/image/left.png"
LEFTJUMP="C:/python_game/image/leftrunning.png"
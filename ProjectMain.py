from StartPage import StartPage
import LearningMenu
from playsound import playsound
from UserManager import UserManager
from WordManager import WordManager
from pygame import *
import threading
import TestMenu
import CardMenu
from time import sleep

try:
    import Tkinter as tk
except:
    import tkinter as tk

class ProjectMain(tk.Tk,UserManager,WordManager): #Tk를 상속받아서 생성

    def __init__(self):
        tk.Tk.__init__(self)
        UserManager.__init__(self)
        WordManager.__init__(self)
        self.init_gui()
        mixer.init()
        self.wordread()
        self.word_img()
        self.background_music=mixer.Sound("C:/english-learning-program/sound/01. The Alphabet Song.mp3")
        self.background_music.set_volume(0.2)
        self.click=mixer.Sound("C:/english-learning-program/sound/click_sound1.mp3")
        self.click.set_volume(0.5)
        self.music=True
        self._frame=None
        self.switch_frame(StartPage) #프레임 변경을 위함
        
    def init_gui(self): #Tk 이름 설정 및 꾸미기
        self.geometry("1000x800") #1000x800 크기
        self.resizable(width=False, height=False) #화면 고정
        self.title("english learning program") #타이틀 설정
        self.iconbitmap('C:/english-learning-program/image/symbol.ico') #좌측 맨끝 아이콘 설정
   
    def switch_frame(self,frame_class):
        new_frame=frame_class(self)
        
        if self._frame is not None:
            self._frame.destroy()
 
        self._frame=new_frame
        self._frame.pack()
        
    def write_notKnow(self,update): #아는것 추가,틀린것 삭제
        
        if update is not None:
            self.delete_notKnowInfo(update)
            self.insert_knowInfo(update)
            self.set_user()
            
    def insert_info(self,know,notknow):
        try:
            self.insert_knowInfo(know)
            self.insert_notknowInfo(notknow)
            self.set_user()
        except:
            pass
        
    def write_user(self):
        self.insert_user()
    
    def write_info_know(self,suc_num):
        self.insert_knowInfo(suc_num)
        self.set_user()
        
    def write_info_notKnow(self,wrong_num):
        self.insert_notknowInfo_int(wrong_num)
        self.set_user()
    
    def click_sound(self,sound): 
        if sound==True:
            self.click.play()
            sound=False
            
    # def card_back_sound(self): 
    #     mixer.music.load("C:/english-learning-program/sound/card_sound.mp3")
    #     mixer.music.play()
        
        
    def music_sound(self):
        self.background_music.play(-1)
        
    def stop_sound(self):
        self.background_music.stop()
    
    def exit_(self):
        sound=True
        self.click_sound(sound)
        print("종료됩니다")
        self.destroy()
        
        exit()

python_project=ProjectMain()

python_project.mainloop()

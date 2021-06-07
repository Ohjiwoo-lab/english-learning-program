import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import GameMenu
import CardLevelOne 
import CardLevelTwo
import CardLevelThree

class CardMenuPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master=master
        self.canvas = tk.Canvas(self, width=1000, height=800,bg="black")

        self.pack()
        self.canvas.pack()

        background=Image.open("C:/english-learning-program/image/background.png")

        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        self.gui_frame()

    def next_one_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardLevelOne.LevelOne)

    def next_two_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardLevelTwo.LevelTwo)

    def next_three_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardLevelThree.LevelThree)

    def show_manual(self):
        message = '''
 <게임 방법>
        
  1. 게임의 난이도를 선택하여 게임을 시작한다.
        
  2. 게임이 시작되면 타이머가 작동한다. 각 난이도마다 제한시간이 정해져 있고
  이를 초과하게 되면 게임에 실패한다.
           
  3. 제한 시간 내에 모든 카드를 뒤집어서 '영어 단어 - 한글 단어' 쌍을 찾으면 된다. 
  예를 들어 'apple - 사과' 쌍이 있다면 'apple'이 적혀 있는 카드와 '사과'가 적혀있는 
  카드를 뒤집어야 점수를 받을 수 있다.
           
  4. 난이도 별로 존재하는 단어의 개수만큼 점수를 받아야 게임에서 성공하게 된다.
        
  5. 카드를 뒤집는 횟수에는 제한이 없다.
        
        
  <게임의 난이도>
        
  - 3 x 4 : 총 12개의 카드에 6개의 단어가 있다. 제한시간은 3분이다.
  - 4 x 5 : 총 20개의 카드에 10개의 단어가 있다. 제한시간은 4분이다.
  - 5 x 6 : 총 30개의 카드에 15개의 단어가 있다. 제한시간은 5분이다.
  '''

        pixelVirtual = tk.PhotoImage(width=1, height=1)

        self.msg_label = tk.Label(self, image=pixelVirtual, bg='#D9D9D9', fg='black', bd=4, text="", font=("G마켓 산스 Light", 14, 'bold'), width=780, height=575, compound="c", anchor=tk.NW)
        self.msg_label.place(x=110, y=120)

        self.msg_label['text'] = message

        self.img6 = tk.PhotoImage(file="image/redo.png")
        self.btn_back = tk.Button(self, image=self.img6, relief='flat', command=self.disable_label, width=40, height=40, compound="c")
        self.btn_back.place(x=820, y=620)
   
    def back_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.stop_sound()
        self.master.switch_frame(GameMenu.GameMenuPage)
        
    
    def disable_label(self):
        self.msg_label.destroy()
        self.btn_back.destroy()

    # def back_page(self):
    #     self.canvas.delete("all")
    #     self.destroy()
    #     self.master.switch_frame(GameMenu.GameMenuPage)

    def gui_frame(self):

        fontStyle = tkFont.Font(family="맑은 고딕", size=28, weight='bold')
        fontStyle2 = tkFont.Font(family="G마켓 산스 Light", size=20, weight='bold')

        # 배경 상자
        self.title = tk.Canvas(self, width=780, height=525, bg="black")
        self.title.pack()

        wall = tk.PhotoImage(file="image/background2.png")
        self.canvas.create_image(110, 130, anchor=tk.NW, image=wall)

        # 타이틀
        img = tk.PhotoImage(file="image/title.png")
        title_label = tk.Label(self, image=img)
        title_label.place(x=110, y=25)

        label = tk.Label(self, text="난이도를 선택하세요", font=fontStyle, fg='#4472C4', bg="white")
        label.place(x=310, y=160)

        img2 = tk.PhotoImage(file="image/img1.png")
        btn1 = tk.Button(self, image=img2, width=695, height=95, command=self.next_one_page)
        btn1.place(x=140, y=240)

        img3 = tk.PhotoImage(file="image/img2.png")
        btn2 = tk.Button(self, image=img3, width=695, height=95, command=self.next_two_page)
        btn2.place(x=140, y=360)

        img4 = tk.PhotoImage(file="image/img3.png")
        btn3 = tk.Button(self, image=img4, width=695, height=95, command=self.next_three_page)
        btn3.place(x=140, y=480)

        img5 = tk.PhotoImage(file="image/question.png")
        btn4 = tk.Button(self, image=img5, bg='white', fg='white', width=30, height=30, relief='flat', command=self.show_manual)
        btn4.place(x=130, y=620)

        label = tk.Label(self, text="게임 설명", font=fontStyle2, fg="black", bg='white')
        label.place(x=175, y=622)

        btn5 = tk.Button(self, text="나가기", bg='gray', fg='white', width=10, height=2,command=self.back_page)
        btn5.place(x=875, y=722)

        self.mainloop()
    
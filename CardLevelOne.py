import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import CardMenu
import CardGameOut
from global_vari import wordlist
import random
from time import sleep
import CardSuccess

class LevelOne(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master=master
        self.canvas = tk.Canvas(self, width=1000, height=800)
        self.pack()
        self.canvas.pack()
        self.clock = 180
        self.dic_wordlist={}
        self.Nlist_ans={}
        self.key=[]
        self.count=0
        self.kor_key=None
        self.eng_key=None
        self.key1_button=None
        self.key2_button=None
        self.card_count =0

        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        self.gui_frame()
    
    def dic_word(self):
     
        for i in range(len(wordlist)):
            self.dic_wordlist[wordlist[i].get_english()]=wordlist[i].get_korean()
     
        while len(self.Nlist_ans)!=6:
            self.Nlist_ans.update({random.choice((list(self.dic_wordlist.items())))})
        print(self.Nlist_ans)
        self.kor_key=list(self.Nlist_ans.keys())
        self.eng_key=list(self.Nlist_ans.values())
        self.key=self.kor_key+self.eng_key
        random.shuffle(self.key)
        print(self.key)
        
    def gameOver_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardGameOut.GameOut(self.master, 1))

    def back_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardMenu.CardMenuPage)
        
    def click(self,index):
         global key1
         global key2
         self.master.card_sound()
         self.buttons[index]['text']=self.key[index]
         try:
            
             if self.card_count==0:
                   if self.key1_button and self.key2_button !=None:
                       self.count=self.count+1
                       print(self.count)
                       self.key1_button['state']=tk.NORMAL
                       self.key2_button['state']=tk.NORMAL
                       self.key1_button.destroy()
                       self.key2_button.destroy()
                       self.text.set(str(self.count)+' / 6')
                       if self.count == 5:
                            self.key1_button['state']=tk.NORMAL
                            self.key2_button['state']=tk.NORMAL
                       if self.count == 6 :
                           self.success()
                           print("종료")
                       
                  
                   if self.buttons[index]['text'] in self.kor_key: # 1키 한글
                       key1=self.kor_key.index(self.buttons[index]['text'])
                       self.key1_button=self.buttons[index]
                   if self.buttons[index]['text'] in self.eng_key: # 1키 영어
                       key1=self.eng_key.index(self.buttons[index]['text'])
                       self.key1_button=self.buttons[index]
                       self.buttons[index]['state']=tk.DISABLED
                   self.card_count=self.card_count+1
                   return
             if self.card_count==1:
                 if self.buttons[index]['text'] in self.eng_key: #2키 영어
                     if self.eng_key.index(self.buttons[index]['text'])==key1:
                         key2=self.eng_key.index(self.buttons[index]['text'])
                         self.key2_button=self.buttons[index]
                         self.buttons[index]['state']=tk.DISABLED
                         self.card_count=0
                     else: #영어 영어
                         self.key2_button=self.buttons[index]
                         self.buttons[index]['state']=tk.DISABLED
                         self.card_count=2
                     return
                 elif self.buttons[index]['text'] in self.kor_key: #2키 한글
                     if self.kor_key.index(self.buttons[index]['text'])==key1:
                         key2=self.kor_key.index(self.buttons[index]['text'])
                         self.key2_button=self.buttons[index]
                         self.buttons[index]['state']=tk.DISABLED
                         self.card_count=0
                     else: #한글 한글
                         self.key2_button=self.buttons[index]
                         self.buttons[index]['state']=tk.DISABLED
                         self.card_count=2

                     return
             if self.card_count==2: #틀렸을 때
                   self.key1_button['state']=tk.NORMAL
                   self.key2_button['state']=tk.NORMAL
                   self.key1_button['text']=''
                   self.key2_button['text']=''              
                   if self.buttons[index]['text'] in self.kor_key: # 1키 한글
                       key1=self.kor_key.index(self.buttons[index]['text'])
                       self.key1_button=self.buttons[index]
                   if self.buttons[index]['text'] in self.eng_key: # 1키 영어
                       key1=self.eng_key.index(self.buttons[index]['text'])
                       self.key1_button=self.buttons[index]
                       self.buttons[index]['state']=tk.DISABLED
                   self.card_count=1
               
         except:
            pass
        
    def success(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardSuccess.CardSuccess) #프레임 변경을 위함
        
    def gui_frame(self):

        self.dic_word()
        # 배경 상자
        self.bac = tk.Canvas(self, width=780, height=525, bg="black")
        self.bac.pack()

        wall = tk.PhotoImage(file="image/background3.png")
        self.canvas.create_image(110, 95, anchor=tk.NW, image=wall)

        # 타이머, 점수 있는 곳 상자
        self.title = tk.Canvas(self, width=780, height=525, bg="black")
        self.title.pack()

        wall2 = tk.PhotoImage(file="image/background4.png")
        self.canvas.create_image(130, 130, anchor=tk.NW, image=wall2)

        # 타이틀
        img = tk.PhotoImage(file="image/title.png")
        title_label = tk.Label(self, image=img)
        title_label.place(x=110, y=25)

        xvar = 140
        yvar = 260
        self.buttons = []
        cardCount = 0

          # 점수 표기 레이블

        fontStyle = tkFont.Font(family="맑은 고딕", size=30, weight='bold')
        fontStyle2 = tkFont.Font(family="G마켓 산스 Light", size=18, weight='bold')
        self.text = tk.StringVar()
        self.text.set('0 / 6')
        
        tk.Label(self, text='제한 시간(3분)', font=fontStyle2, bg='white', fg='black').place(x=140, y=160)
        self.score=tk.Label(self, textvariable=self.text, font=fontStyle, bg='white', fg='black').place(x=750, y=140)

        for i in range(3):
            for j in range(4):
                self.buttons.append(tk.Button(self, bg="#8FAADC", width=23, height=8,  command=lambda index=cardCount: self.click(index)))
                self.buttons[cardCount].place(x=xvar, y=yvar)
                xvar = xvar + 182
                cardCount += 1

            xvar = 140
            yvar = yvar + 150

        # 중간에 나가기
        finish_img = tk.PhotoImage(file="image/finish.png")
        btn = tk.Button(self, image=finish_img, bg='white', width=40, height=40, command=self.back_page, relief='flat')
        btn.place(x=905, y=705)

        # 타이머
        self.createWidgets()

        self.mainloop()

    # 타이머
    def createWidgets(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 30), bg='white', fg='black')
        self.time.place(x=340, y=150)
        self.time["textvariable"] = self.now

        self.xlab = 470
        self.ment = tk.Label(self, text="", font=('Helvetica', 20), bg='white', fg='black')
        self.ment.place(x=self.xlab, y=155)
        self.ment['text'] = '화이팅~! 화이팅~!'

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        if self.clock == 0:
            self.gameOver_page()

        if self.clock <= 10:
            self.time["fg"] = 'red'
            self.xlab = 430
            self.ment.place(x=self.xlab, y=155)
            self.ment['text'] = '시간이 얼마 안남았어요...'
            self.ment['fg'] = 'red'

        minute,second = self.convert(self.clock)
        self.now.set(str(minute) + ':' + str(second))
        self.clock -= 1
        # schedule timer to call myself after 1 second
        self.after(180, self.onUpdate)

    def convert(self, seconds):
        """
        Convert seconds to (seconds, minutes, hours, remainder_seconds)
        """
        r = seconds

        s = r % 60
        m = (r - s) % (60 * 60)

        # 시간 단위는 안 쓰므로 생략
        # h = (r - s - m) % (60*60*60)

        return int(m / 60), s  # int(h/(60*60))
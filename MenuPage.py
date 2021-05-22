import tkinter as tk
from PIL import Image, ImageTk
from global_vari import wordlist,gl_user
from tkinter.font import Font
import LearningMenu
import GameMenu

class MenuPage(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master=master
        self.canvas=tk.Canvas(self,width=1000,height=800,bg="blue")
        self.pack()
        self.canvas.pack() 
        self.gui_frame()
        
    def learning_but_event(self,e):
        self.button1["image"]=self.click_but_img
    
    def leave_but_event(self,e):
        self.button1["image"]=self.but_img
        
    def game_but_event(self,e):
        self.game_button["image"]=self.click_but_img1
        
    def leave_gamebut_event(self,e):
        self.game_button["image"]=self.but_img1
    
    def list_but_event(self,e):
        self.word_button["image"]=self.click_but_img2
    
    def leave_listbut_event(self,e):
        self.word_button["image"]=self.but_img2
   
    def but_event(self):
        sound=True
        self.master.click_sound(sound)
       
        self.word_button["state"]=tk.DISABLED
        self.list_box=tk.Frame(self)
        self.list_box.place(x=190,y=50,width=600,height=680)
        self.mylist=tk.Listbox(self.list_box,bg="white",width=300,height=500, font=("맑은 고딕",20));
       
        for i in range(len(wordlist)):
            self.mylist.insert(wordlist[i].get_wordNum(),wordlist[i].get_english()+" "+wordlist[i].get_korean())
        self.mylist.pack()
        
        self.scroll=tk.Scrollbar(self.list_box,orient="vertical")
        self.scroll.config(command=self.mylist.yview)
        self.scroll.pack(side="right",fill="y")
        self.mylist.config(yscrollcommand=self.scroll.set)
              
        self.back_img = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/back_but.png'))
        self.back_but=tk.Button(self.list_box,height=60,width=60,image=self.back_img,command=self.destory_frame)
        self.back_but.place(x=530,y=610)
    
    def destory_frame(self):
        self.word_button["state"]=tk.NORMAL
        self.mylist.destroy()
        self.list_box.destroy()
        self.back_but.destroy()

    def next_page(self):
        sound=True
        self.master.click_sound(sound)
       
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(LearningMenu.LearningMenu)
  
    def next_page_game(self):
        sound=True
        self.master.click_sound(sound)
       
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(GameMenu.GameMenuPage)
        
    def gui_frame(self):
        
        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        
        top_word=Image.open("C:/english-learning-program/image/top_word.png")
        #이미지 크기 재조정
        resized_top_word=top_word.resize((850,120),Image.ANTIALIAS)
        new_topword=ImageTk.PhotoImage(resized_top_word) #크기조정
        self.canvas.create_image(70,10,anchor=tk.NW,image=new_topword)
        
        self.top_frame=tk.Frame(self)
        self.top_frame.place(x=120,y=150,width=350,height=50)
        self.top_label=tk.Label(self.top_frame,text="안녕하세요 "+gl_user.get_name()+"님!",fg="black",bg="white",width=500,height=100,font=("맑은 고딕",25))
        self.top_label.pack()
        
        
        self.myframe=tk.Frame(self)
        self.myframe.place(x=170,y=240,width=670,height=70)
        
        font=Font(family="맑은 고딕", underline=True,size=40 )

        self.mylabel=tk.Label(self.myframe,text="오늘도 학습하러 오셨군요!",fg="orange",bg="white",width=300,height=200,font=font)
        self.mylabel.pack()
        
        word_box=Image.open("C:/english-learning-program/image/word_box.png")
        #이미지 크기 재조정
        resized_box=word_box.resize((880,300),Image.ANTIALIAS)
        new_box=ImageTk.PhotoImage(resized_box) #크기조정
        self.canvas.create_image(70,125,anchor=tk.NW,image=new_box)
        
        self.click_but_img=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/menu_learning2.png'))
        self.but_img = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/menu_learning1.png'))
        self.button1 = tk.Button(self, text="",height=160,width=260,image = self.but_img,command=self.next_page)
        self.button1.place(x=150,y=480)
        
        #이벤트 처리 마우스를 가져다 되었을때
        self.button1.bind("<Enter>",self.learning_but_event)
        self.button1.bind("<Leave>",self.leave_but_event)
       
        self.click_but_img1 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/menu_game2.png'))
        self.but_img1 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/menu_game3.png'))
           
        self.game_button = tk.Button(self, text="",height=160,width=260,image = self.but_img1,command=self.next_page_game) #,command=lambda: master.switch_frame(GameMenu)).pack() 붙이기
        self.game_button.place(x=580,y=480)

        self.game_button.bind("<Enter>",self.game_but_event)
        self.game_button.bind("<Leave>",self.leave_gamebut_event)
        
        self.click_but_img2 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/word_list2.png'))
        self.but_img2 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/word_list1.png'))
        self.word_button = tk.Button(self, text="",height=40,width=700,image = self.but_img2,command=self.but_event)
        self.word_button.place(x=145,y=700)
       
        self.word_button.bind("<Enter>",self.list_but_event)
        self.word_button.bind("<Leave>",self.leave_listbut_event)
        
        self.exit_but=tk.Button(self,height=2,width=10,text="나가기",fg="black",command=self.master.exit_)
        self.exit_but.place(x=880,y=720)
        self.mainloop()
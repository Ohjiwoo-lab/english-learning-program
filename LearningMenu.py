import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from global_vari import gl_user,wordlist,rnum,veri
import random
import ReviewMenuPage
import LearningPage
import MenuPage

class LearningMenu(tk.Frame):
    
    def __init__(self,master): 
        tk.Frame.__init__(self,master)
        self.canvas=tk.Canvas(self, width=1000,height=800)
        self.master=master
        self.pack()
        self.canvas.pack() 
        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        self.gui_frame()
    
    def click_but1(self,e):
        if self.learning_but:
            self.learning_but["image"]=self.click_learning
    
    def click_but2(self,e):
            self.review_but["image"]=self.click_review
        
    def click_but3(self,e):
            self.card_but["image"]=self.click_card
        
    def click_but4(self,e):
            self.test_but["image"]=self.click_test
            
    def click_but5(self,e):
            self.word_button["image"]=self.click_but_img2
   
    def leave_but(self,e):
        if self.learning_but :
            self.learning_but["image"]=self.but_img
        if self.review_but :
            self.review_but["image"]=self.but_img1
        if self.card_but :
            self.card_but["image"]=self.but_img2
        if self.test_but :
            self.test_but["image"]=self.but_img3
        if self.word_button :
            self.word_button["image"]=self.but_img4
   
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
    
    def go_event(self,e):
        veri=True
        print("학습하러 가기 frame 연결")
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(LearningPage.LearningPage)

    def next_review(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(ReviewMenuPage.ReviewMenu)
    def next_learning(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(LearningPage.LearningPage(self.master,0))
    def next_word(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(LearningPage.LearningPage(self.master,1))
    def back_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(MenuPage.MenuPage)
        
    def gui_frame(self) :
        
        top_word=Image.open("C:/english-learning-program/image/top_word.png")
        #이미지 크기 재조정
        resized_top_word=top_word.resize((850,120),Image.ANTIALIAS)
        new_topword=ImageTk.PhotoImage(resized_top_word) #크기조정
        self.canvas.create_image(70,10,anchor=tk.NW,image=new_topword)
        
        self.top_frame=tk.Frame(self)
        self.top_frame.place(x=120,y=150,width=350,height=50)

        self.top_label=tk.Label(self.top_frame,text="안녕하세요 "+gl_user.get_name()+"님!",fg="black",bg="white",width=500,height=100,font=("맑은 고딕",25))
        self.top_label.pack()
        
        self.rand_word_box=tk.Frame(self)
        self.rand_word_box.place(x=300,y=220,width=550,height=100)
        self.rand_word_box.config(bg="white")

        rnum = random.randint(0,len(wordlist))
        
        self.rand_label=tk.Label(self.rand_word_box,text=wordlist[rnum].get_english(),fg="red",bg="white",font=("맑은 고딕",40))
        self.rand_label.grid(row=0,column=0)
        
        self.mylabel=tk.Label(self.rand_word_box,text=", 무슨 뜻 일까요?",fg="black",bg="white",font=("맑은 고딕",30))
        self.mylabel.grid(row=0,column=2)
        
        self.go_frame=tk.Frame(self)
        self.go_frame.place(x=650,y=300,width=200,height=45)
        
        font=Font(family="맑은 고딕", size=20, underline=True)

        self.go_label=tk.Label(self.go_frame,text="학습하러 가기",fg="gray",bg="white",width=300,height=100,font=font)
        self.go_label.pack()
        
        self.go_label.bind("<Button-1>",self.go_event)
        
        word_box=Image.open("C:/english-learning-program/image/word_box.png")
        #이미지 크기 재조정
        resized_box=word_box.resize((880,300),Image.ANTIALIAS)
        new_box=ImageTk.PhotoImage(resized_box) #크기조정
        self.canvas.create_image(70,125,anchor=tk.NW,image=new_box)
        
        self.click_learning=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/learning_but1.png'))
        self.but_img = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/learning_but.png'))
        self.learning_but=tk.Button(self,height=70,width=650,image=self.but_img,command=self.next_learning)
        self.learning_but.place(x=170,y=440)
        
        self.learning_but.bind("<Enter>",self.click_but1)
        self.learning_but.bind("<Leave>",self.leave_but)
       
        self.click_review=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/review_but1.png'))
        self.but_img1=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/review_but.png'))
        self.review_but=tk.Button(self,height=70,width=650,image=self.but_img1,command=self.next_review)
        self.review_but.place(x=170,y=510)
        
        self.review_but.bind("<Enter>",self.click_but2)
        self.review_but.bind("<Leave>",self.leave_but)
        
        self.click_card=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/card_but1.png'))
        self.but_img2=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/card_but.png'))
        self.card_but=tk.Button(self,height=70,width=650,image=self.but_img2,command=self.next_word)
        self.card_but.place(x=170,y=580)
        
        self.card_but.bind("<Enter>",self.click_but3)
        self.card_but.bind("<Leave>",self.leave_but)
        
        self.click_test=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/test_but1.png'))
        self.but_img3=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/test_but.png'))
        self.test_but=tk.Button(self,height=70,width=650,image=self.but_img3)
        self.test_but.place(x=170,y=650)
        
        self.test_but.bind("<Enter>",self.click_but4)
        self.test_but.bind("<Leave>",self.leave_but)
        
        self.click_but_img2 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/word_list2.png'))
        self.but_img4 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/word_list1.png'))
        self.word_button = tk.Button(self, text="",height=30,width=650,image = self.but_img4,command=self.but_event)
        self.word_button.place(x=170,y=720)
       
        self.word_button.bind("<Enter>",self.click_but5)
        self.word_button.bind("<Leave>",self.leave_but)
        
        self.back_but=tk.Button(self,height=2,width=10,text="뒤로가기",fg="black",command=self.back_page)
        self.back_but.place(x=880,y=720)
        self.mainloop()
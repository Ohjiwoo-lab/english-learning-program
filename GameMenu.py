import tkinter as tk
from PIL import Image, ImageTk
import CardMenu
import MenuPage
#import start
class GameMenuPage(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.canvas=tk.Canvas(self, width=1000,height=800)
        self.pack()
        self.canvas.pack() 
        
        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        self.gui_frame()
    def draw_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
     #   self.master.switch_frame(start)
        
    def enter_event(self,e):
        self.anagram_but["image"]=self.click_anagram
    def enter_event1(self,e):
        self.draw_but["image"]=self.click_draw
    
    def leave_event(self,e):
        if self.draw_but:
            self.draw_but["image"]=self.but_img1
        if self.anagram_but:
            self.anagram_but["image"]=self.but_img
    
    def anag_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardMenu.CardMenuPage)
    
    def back_page(self):
        sound=True
        self.master.click_sound(sound)
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(MenuPage.MenuPage)    
    
    def gui_frame(self):
        top_word=Image.open("C:/english-learning-program/image/top_word_blue.png")
        #이미지 크기 재조정
        resized_top_word=top_word.resize((790,110),Image.ANTIALIAS)
        new_topword=ImageTk.PhotoImage(resized_top_word) #크기조정
        self.canvas.create_image(105,20,anchor=tk.NW,image=new_topword)
        
        word_box=Image.open("C:/english-learning-program/image/word_box1.png")
        #이미지 크기 재조정
        resized_box=word_box.resize((780,280),Image.ANTIALIAS)
        new_box=ImageTk.PhotoImage(resized_box) #크기조정
        self.canvas.create_image(110,140,anchor=tk.NW,image=new_box)
        
        self.click_anagram=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/anagram_but1.png'))
        self.but_img = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/anagram_but.png'))
        self.anagram_but = tk.Button(self,height=100,width=685,image = self.but_img,command=self.anag_page)
        self.anagram_but.place(x=150,y=450)
        
        self.anagram_but.bind("<Enter>",self.enter_event)
        self.anagram_but.bind("<Leave>",self.leave_event)
      
        self.click_draw=ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/draw_but1.png'))
        self.but_img1 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/draw_but.png'))
        self.draw_but = tk.Button(self,height=100,width=685,image = self.but_img1,command=self.draw_page)
        self.draw_but.place(x=150,y=600)
        
        self.draw_but.bind("<Enter>",self.enter_event1)
        self.draw_but.bind("<Leave>",self.leave_event)
        
        self.back_but=tk.Button(self,height=2,width=10,text="뒤로가기",fg="black",command=self.back_page)
        self.back_but.place(x=880,y=720)
        self.mainloop()        
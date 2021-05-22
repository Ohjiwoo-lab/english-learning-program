import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from global_vari import gl_user,wordlist
import ReviewPage

class ReviewMenu(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master=master
        self.pack()
        self.canvas=tk.Canvas(self,width=1000,height=800)
        self.canvas.pack()
        self.gui_frame()
            
    def howToUse(self,e):
        self.explain_frame=tk.Frame(self)
        self.explain_frame.place(x=255,y=200,width=500,height=260)
        
        self.explain_canvas=tk.Canvas(self.explain_frame,width=500,height=260,bg="white")
        self.explain_canvas.pack()
        
        explain=Image.open("C:/english-learning-program/image/howtouse.png")
        #이미지 크기 재조정
        ex_resized=explain.resize((500,250),Image.ANTIALIAS)
        self.new_img=ImageTk.PhotoImage(ex_resized) #크기조정
        self.explain_canvas.create_image(0,0,anchor=tk.NW,image=self.new_img)
        
        bt=tk.Button(self.explain_frame, text="뒤로가기",command=self.back_page)
        bt.place(x=220,y=210)
        
    def back_page(self):
        self.explain_canvas.delete("all")
        self.explain_frame.destroy()
  
    def next_page(self,e):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(ReviewPage.ReviewPage)
        
    def gui_frame(self):
        

        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)

        self.rptInitBg1=tk.Canvas(self,width=840,height=665,bg="#F5B296")
        self.rptInitBg1.place(x=78,y=60)
        
        self.rptInitBg2=tk.Canvas(self,width=765,height=590,bg="white")
        self.rptInitBg2.place(x=115,y=100)
        
        rptWidget1=tk.Label(self,text="복습하기",font=("맑은 고딕",45,"bold"),
                         fg="white",bg="#F5B296",justify="center")
        rptWidget1.place(x=40,y=150,width=915,height=100)
        
        rptWidget3=tk.Label(self,text="사용방법",font=("맑은 고딕",15,'bold'),width=10,height=1,fg="#262626",bg="white")
        rptWidget3.place(x=450,y=270)
        
        but=Image.open("C:/english-learning-program/image/que_but.png")
        #이미지 크기 재조정
        but_resized=but.resize((40,40),Image.ANTIALIAS)
        new_but=ImageTk.PhotoImage(but_resized) #크기조정   
        rptWidget4=tk.Label(self,image=new_but,width=40,height=40,bg="white")
        rptWidget4.place(x=425,y=265)
        
        rptWidget4.bind('<Button-1>',self.howToUse)
        
        start_but=Image.open("C:/english-learning-program/image/rptStartButton.png")
        #이미지 크기 재조정
        startbut_resized=start_but.resize((200,200),Image.ANTIALIAS)
        new_startbut=ImageTk.PhotoImage(startbut_resized) #크기조정   
        rptWidget5=tk.Label(self,image=new_startbut,width=200,height=200,bg="white")
        rptWidget5.place(x=400,y=385)
        
        rptWidget5.bind('<Button-1>',self.next_page)
        self.mainloop()
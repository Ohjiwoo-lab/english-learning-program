import tkinter as tk
from PIL import Image, ImageTk
from PyQt5.QtCore import *
from MenuPage import MenuPage
from global_vari import gl_user,userlist
import threading
class StartPage(tk.Frame):
    
    def __init__(self,master):
        
        tk.Frame.__init__(self,master)
        self.master=master
        self.canvas=tk.Canvas(self,width=1000,height=800,bg="black")
        self.pack()
        self.canvas.pack() 
          # image open <바탕화면>
        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
         
        #1초씩이미지변경
        self.loading_frame=tk.Frame(self)
        self.loading_frame.place(x=403,y=505,width=190,height=185)
        self.canvas_loading=tk.Canvas(self.loading_frame,width=190,height=185);
        self.canvas_loading.pack()
        self.master.music_sound()
        self.gui_frame()
   
    def search(self,e):
        
        print("키보드 입력",self.my_text.get().strip())
        name=self.my_text.get()
        
        user_check=False
        i=-1
        check=i;
        for i in range(len(userlist)):
            if userlist[i].get_name() == name :
               check=i;
               user_check=True
            
        if user_check == False:
            tk.messagebox.showinfo("정보 확인창","없는 정보입니다. \n Create버튼을 통해 새로 만들어주세요.")
        else:
            gl_user.set_init(userlist[check].get_userNum(),userlist[check].get_name())
            gl_user.set_list(userlist[check].get_know(),userlist[check].get_notKnow())
            self.loading_frame.destroy()
            user_check=True
            self.destroy()
            sound=False
            self.master.stop_sound()
            self.master.switch_frame(MenuPage)
                
    def create_search(self):
           
        name=self.my_text.get().strip()
        user_check=False
           
        if user_check==False:
            for i in range(len(userlist)):
                if userlist[i].get_name() == name :
                    user_check=True
        if user_check==True:
            tk.messagebox.showinfo("정보 확인창","있는 정보입니다. \n Ok버튼을 통해 학습을 시작해주세요.")
        if len(name) != 0 :
            if user_check==False:
                gl_user.set_init(userlist[len(userlist)-1].get_userNum()+1, name)
                self.master.write_user()
                tk.messagebox.showinfo("정보 확인창","생성 완료.")
      
        self.my_text.delete(0,len(name))
        
        print(gl_user.get_name(),gl_user.get_userNum())
       
        #txt.get().strip() #앞뒤 공백 제거하여 가져오기 
    def enter_event(self,e):
        self.create_button["image"]=self.click_but_img
    def enter_event1(self,e):
        self.ok_button["image"]=self.click_but_img1
    def enter_event2(self,e):
        self.back_button["image"]=self.click_but_img2
        
    def leave_event(self,e):
        if self.create_button :
            self.create_button["image"]=self.but_img
        if self.ok_button :
            self.ok_button["image"]=self.but_img1
        if self.back_button :
            self.back_button["image"]=self.but_img2

    def back(self):
        self.login.destroy()
        self.create_button.destroy()
        self.ok_button.destroy()
        self.back_button.destroy()
        self.login_frame.destroy()
        
    def click(self,e):
        sound=True
        self.master.click_sound(sound)
        self.login_frame=tk.Frame(self)
        self.login_frame.place(x=300,y=300,width=400,height=200)
        self.canvas_login=tk.Canvas(self.login_frame,width=400,height=200,bg="white")
        self.canvas_login.pack()
        
        self.login=tk.Frame(self.login_frame)
        self.login.place(x=0,y=100,width=400,height=40)
        
        self.my_text=tk.Entry(self.login,width=35,bd=4,font=("맑은 고딕",15),bg="white")
        self.my_text.pack()
        self.my_text.bind("<Return>",self.search)
        
        self.click_but_img = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/create_but1.png'))
        self.but_img = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/create_but.png'))
        self.create_button = tk.Button(self.login_frame, text="",height=39,width=65,image = self.but_img,command=self.create_search)
        self.create_button.place(x=70,y=145)
        
        self.create_button.bind("<Enter>",self.enter_event)
        self.create_button.bind("<Leave>",self.leave_event)
        print("button click")
       
        self.click_but_img1 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/ok_but1.png'))
        self.but_img1 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/ok_but.png'))
        self.ok_button = tk.Button(self.login_frame, text="",height=39,width=65,image = self.but_img1)
        self.ok_button.place(x=165,y=145)
        self.ok_button.bind("<Enter>",self.enter_event1)
        self.ok_button.bind("<Leave>",self.leave_event)
        
        self.ok_button.bind("<Button-1>",self.search)
        
        self.click_but_img2 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/smallback_img1.png'))
        self.but_img2 = ImageTk.PhotoImage(Image.open('C:/english-learning-program/image/smallback_but.png'))
        self.back_button = tk.Button(self.login_frame, text="",height=39,width=65,image = self.but_img2,command=self.back)
        self.back_button.place(x=260,y=145)
        
        self.back_button.bind("<Enter>",self.enter_event2)
        self.back_button.bind("<Leave>",self.leave_event)
        
        
    def gui_frame(self):
      
        #cbnu
        cbnu=Image.open("C:/english-learning-program/image/cbnu.png")
        resize_cbnu=cbnu.resize((720,250),Image.ANTIALIAS)
        new_cbnu=ImageTk.PhotoImage(resize_cbnu)
        self.canvas.create_image(150,70,anchor=tk.NW,image=new_cbnu)

        #제목
        title=Image.open("C:/english-learning-program/image/word.png")
        resize_title=title.resize((800,150),Image.ANTIALIAS)
        new_title=ImageTk.PhotoImage(resize_title)
        self.canvas.create_image(110,320,anchor=tk.NW,image=new_title)
        
        maker=Image.open("C:/english-learning-program/image/maker.png")
        resize_maker=maker.resize((400,125),Image.ANTIALIAS)
        new_maker=ImageTk.PhotoImage(resize_maker)
        self.canvas.create_image(300,680,anchor=tk.NW,image=new_maker)

        loading_start=Image.open("C:/english-learning-program/image/loading.jpg")
        resize_loading=loading_start.resize((190,190),Image.ANTIALIAS)
        new_loading=ImageTk.PhotoImage(resize_loading)
        self.canvas_loading.create_image(0,0,anchor=tk.NW,image=new_loading)#
        
        self.canvas_loading.bind("<Button-1>",self.click)
        
        self.tk.mainloop()
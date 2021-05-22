import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from global_vari import wordlist,gl_user
import copy

class LearningPage(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self)
        self.page_count=0
        self.master = master
        self.canvas = tk.Canvas(self, width=1000, height=800)
        self.pack()
        self.canvas.pack()
        self.arr_ch=[]
        self.enter_possible=False
        self.gui_frame()
     # 상단 학습하기 버튼
    def learn(self):
        self.enter_possible=True
        self.textbox.place(x=270, y=531)
        #top_button1.config(state='disabled')
        #top_button2.config(state='normal')
        #WordCard_Label.config(fg="white")
    
    # 상단 단어카드 버튼
    def word_card(self):
        self.enter_possible=False
        #top_button1.config(state='normal')
        #top_button2.config(state='disabled')
        self.textbox.place_forget()
        #WordCard_Label.config(fg="black")
        #Learn_Eng.place(x=90, y=140)
    
    def input_data(self,e):
        self.text_name = tk.StringVar()
        self.textbox = tk.Entry(self, width=16, textvariable=self.text_name, font=("맑은 고딕",40),fg = "gray", justify=tk.CENTER, bd = 0)  
        self.textbox.place(x=270, y=531)
        self.textbox.bind("<Return>",self.enter_db)
        
    def press_left(self):
        try:
            if self.page_count > 0 :
                self.right.place(x=932, y=410)
                self.disabled_word()
                self.page_count-=1
                self.text_learn.config(text=wordlist[self.page_count].get_english())
                self.init_text()
                self.wrong_frame.destroy()
            if self.page_count==0:
                self.left.place_forget()
        except:
            pass
        
    def disabled_word(self):
      try:
         temp=copy.deepcopy(gl_user.get_know())
         bool_op=False
         for i in temp[0] :
             if i == self.page_count:
                 bool_op=True
                 
         if bool_op :
            self.Learn_goodlabel.config(width=27, height=1)
            print("일치")
            self.Learn_goodlabel.pack()    
            self.textbox["state"]=tk.DISABLED
            self.textbox["disabledbackground"]="white"
         else: 
            self.textbox["state"]=tk.NORMAL
            self.learn_goodlabel.destroy()
            self.good_frame.destroy()
      except:
         pass
   
    def press_right(self):
        #self.page_count
       
        try:
            if self.page_count <= len(wordlist) :
                self.left.place(x=32, y=410)
                self.page_count+=1
                self.disabled_word()
                self.text_learn.config(text=wordlist[self.page_count].get_english())
                self.wrong_frame.destroy()
        except:
            pass
        
    def enter_db(self,e):
         up_text=self.textbox.get()

         if up_text.replace(" ","")==wordlist[self.page_count].get_korean().replace(" ",""): # 맞았으면
             print("Success") 
             self.arr_ch[self.page_count]="O"
             self.text_name.set("")
             self.master.write_info_know(wordlist[self.page_count].get_wordNum())
             self.press_right()
             
         #    self.wrong_frame.destroy()
         else: # 틀렸으면
             self.wrong_frame=tk.Frame(self)
             self.wrong_frame.place(x=360,y=350,width=300,height=70)
             self.wrong_frame.config(bg="white")
             self.text_name.set("")
             self.master.write_info_notKnow(wordlist[self.page_count].get_wordNum())
       
             self.Learn_wronglabel = tk.Label(self.wrong_frame, text = "틀렸습니다!",bg = "white", font=("맑은 고딕",40),fg="red");
             self.Learn_wronglabel.config(width=27, height=1)
             self.Learn_wronglabel.pack()
             
            # self.Learn_wronglabel.place(x=0,y=0)
             
    def list_word(self): 
        try:
            self.wordlist_but.destroy()
          
            self.close_but=tk.Button(self,text="단어 목록 감추기",bg = "gray",command=self.close_list)
            self.close_but.config(width=117, height=2)
            self.close_but.place(x=90, y=723)
            self.listbox = tk.Listbox(self,font=("Consolas",20),height=9,width=54)
            self.listbox.insert(0, "   번호            단어            뜻　　　　　　　상태")
            num=0
            while num < len(wordlist):
                if num<9:
                    line = "　　 %s　　　　　　%s" % (num+1, wordlist[num].get_english())
                elif num<99:
                    line = "　　%s　　　　　　%s" % (num+1, wordlist[num].get_english())
                else:
                    line = "　 %s　　　　　　%s" % (num+1, wordlist[num].get_english())
                        
                    # 영어 단어 길이 세서 띄어쓰기 해줌, 단어 -----------------
                longest_1=len(wordlist[num].get_english())
                space=18
                space=space-longest_1
                while 0 < space:
                    line = line + " "
                    space = space-1
                line = line + wordlist[num].get_korean()
                    
                    # 영어 단어 길이 세서 띄어쓰기 해줌, 뜻 -----------------
                    
                longest_2=len(wordlist[num].get_korean())
                space=9
                space=space-longest_2
                while 0 < space:
                    line = line + "　"
                    space = space-1
                    
                     # 학습 여부 입력
                line = line + self.arr_ch[num]
                self.listbox.insert(num+2, line)
                num=num+1
                    
                self.listbox.pack()
                self.listbox.place(x=90, y=410)
        except:
                pass
    def close_list(self):
                self.listbox.place_forget()
                self.close_but.destroy()
                self.wordlist_but=tk.Button(self, text="단어 목록 보기",bg = "gray",command=self.list_word)
                self.wordlist_but.config(width=117, height=2)
                self.wordlist_but.place(x=90, y=723)
           
    def gui_frame(self):
        self.good_frame=tk.Frame(self)
        self.good_frame.place(x=250,y=350,width=550,height=70)
        self.good_frame.config(bg="white")
        self.Learn_goodlabel = tk.Label(self.good_frame, text = "이미 맞춘 답입니다!",bg = "white", font=("맑은 고딕",40),fg="red");
        for i in range(len(wordlist)):
            self.arr_ch.append("X")
            
        background = Image.open("C:/english-learning-program/image/background.png")
        # 이미지 크기 재조정
        resized = background.resize((1000, 800), Image.ANTIALIAS)
        new_background = ImageTk.PhotoImage(resized)  # 크기조정
        self.canvas.create_image(0, 0, anchor=tk.NW, image=new_background)
        
        self.learn_but=tk.Button(self, text="학습하기",fg = "white",bg = "orange", font=("맑은 고딕",25), command=self.learn)
        self.learn_but.config(width=14, state='disabled')
        self.learn_but.place(x=90, y=27)
        
        self.word_but=tk.Button(self, text="단어카드", font=("맑은 고딕",25),command=self.word_card)
        self.word_but.config(width=14)
        self.word_but.place(x=366, y=27)

        self.test_but=tk.Button(self, text="테스트", font=("맑은 고딕",25))
        self.test_but.config(width=14)
        self.test_but.place(x=642, y=27)
        
        self.text_learn = tk.Label(self, text = wordlist[0].get_english(),bg = "white", font=("맑은 고딕",40));
        self.text_learn.config(width=27, height=4)
        self.text_learn.place(x=90, y=140)
        #command의 줄인말. 사용자에게 지시를 함        
        self.com_text = tk.Label(self, text = "정답을 입력하세요.",bg = "white",fg = "gray", font=("맑은 고딕",40));
        self.com_text.config(width=27, height=4)
        self.com_text.place(x=90, y=431)
        
        self.com_text.bind('<Button-1>',self.input_data)
        
        self.wordlist_but=tk.Button(self, text="단어 목록 보기",bg = "gray",command=self.list_word)
        self.wordlist_but.config(width=117, height=2)
        self.wordlist_but.place(x=90, y=723)
        
        self.left=tk.Button(self, text="  L  ",command=self.press_left)#,
        self.left.place(x=32, y=410)
        self.left.place_forget()

        self.right=tk.Button(self, text="  R  ",command=self.press_right) #,command=press_right
        self.right.place(x=932, y=410)
        
        
        self.mainloop()

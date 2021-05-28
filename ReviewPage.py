import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from global_vari import gl_user,wordlist,rnum
from RptWordAlg import RptWord
import LearningMenu
import copy

class ReviewPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master=master       
        self.writtenWord=[] 
        self.rst=[]
        self.rpt=None
        self.EngRdWord=None 
        self.count=0
        self.canvas=tk.Canvas(self,width=1000,height=800)
        self.pack()
        self.canvas.pack()
        self.gui_frame()
    #처음영어단어 설정하는 메소드    
    def setWord(self):
        while(1):
            self.text.set(self.EngRdWord[0][1]) 
            return 0
    
    def save(self,event):
         self.writtenWord.append(str(self.txtBox.get()))  #비교할때 용이하게
         self.txtBox.delete(0,"end")
         self.chgWord()
         print("enter pressed:Saved Complete!")
         print(self.writtenWord)
         
    def chgWord(self):
        if len(self.EngRdWord)==1:
                self.showRstandExt_Bt()
                self.cal()
        else:
            for i in range(len(self.EngRdWord)):
                if self.text.get()==self.EngRdWord[i][1]:
                    if len(self.EngRdWord)!=0:
                        self.text.set(self.EngRdWord[i+1][1])
                        print("nxtWord button pressed:moved to next word!")
                        return 0
                elif self.text.get().strip()==self.EngRdWord[-1][1]:
                    self.showRstandExt_Bt()
                    self.cal()
                    
                    #self.exitBt=Button(self.windowm,image=self.)
                    return 0
    def cal(self):
         #채점
        for i in range(len(self.EngRdWord)):
            if self.EngRdWord[i][2]==self.writtenWord[i]:
                self.rst.insert(i,'correct')
                self.count=self.count+1
                print('correct')
            else:
                self.rst.insert(i,'wrong')
                print('wrong')

    def destroy_resultPage(self):
        self.rstCanvas.destroy()
        self.rstBg1.destroy()
        self.rstBg2.destroy()
        self.rstExitBt.destroy()
        
    def next_page(self,e):
        self.rnwWord()
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(LearningMenu.LearningMenu)
   
    def rnwWord(self):
        
        notKnowList=[] # 틀린 단어 -know 삭제 후 notknow 추가
        #두개를 반대로
        knowList=[] # 맞은 단어 -그대로
        #tempRnw=gl_user.get_notKnow()
        #맞은 단어와 틀린단어를 문자열 형태로 변환
        for i in range(len(self.EngRdWord)):
            if self.rst[i]=='correct':
                #다틀렸을시에 아는단어들이 모두 틀린단어로 가야되고 아는단어를 1번으로 초기화 해야된다.
                #하지만 1번단어가 이미 틀린단어에 있다면 중복되므로 리스트에 추가되지 않게 한다. 
                if str(self.EngRdWord[i][0])=="1":
                    print(" ")
                else:
                    knowList.append(str(self.EngRdWord[i][0]))   
            else:
                notKnowList.append(str(self.EngRdWord[i][0]))
        #아는단어가 데이터 베이스에 하나도 없으면 불러올때 index오류가 남, 그래서 단어 데이터의 첫번째 단어로 초기화한다. 
        #if not knowList:
        #    print("맞춘단어가 없어 아는단어(know)가 더이상 없습니다.아는단어(know)를 단어 데이터의 첫번째단어로 초기화합니다.")
        #    knowList.append('1')
        #    if "1" in notKnowList:
        #       print("1 in notknowList")
        #else:
        #    print('knowList is not None')
            
        print(notKnowList)
        print(knowList)
        
        if len(knowList) !=0 :
            print("11")
            self.master.write_notKnow(knowList)
         
    def showRstandExt_Bt(self):
        #결과보기 나타남
        self.rstBtImg=Image.open("C:/english-learning-program/image/resultBtImage.png")
        resized_rstBtImg=self.rstBtImg.resize((100,50),Image.ANTIALIAS)
        self.new_rstBtImg=ImageTk.PhotoImage(resized_rstBtImg)
        self.resultBt=tk.Button(self,image=self.new_rstBtImg,bg="#FCD4B4",bd=0,command=self.result)
        self.resultBt.place(x=440,y=700,width=100,height=50)
                    
        #복습하기 종료 나타남
        self.exitBtImg=Image.open('C:/english-learning-program/image/exitRpt_bt.png')
        resized_exitBtImg=self.exitBtImg.resize((50,50),Image.ANTIALIAS)
        self.new_exitBtImg=ImageTk.PhotoImage(resized_exitBtImg)
        self.exitBt=tk.Button(self,image=self.new_exitBtImg,bg="#FCD4B4",bd=0)
        self.exitBt.place(x=830,y=700,width=70,height=50)
        self.exitBt.bind('<Button-1>',self.next_page)
        print("nxtWord button destoyed:please check the answer")
    
    def result(self):      
        self.rstCanvas=tk.Canvas(self,width=400,height=600,bg="white") #4칸 빼면 880
        self.rstCanvas.place(x=290,y=50)
        self.rstBg1=tk.Canvas(self,width=380,height=580,bg="#FCD4B4")
        self.rstBg1.place(x=300,y=55)
        self.rstBg2=tk.Canvas(self,width=360,height=560,bg="white")
        self.rstBg2.place(x=310,y=65)
        #단어가 10개가 넘으면 경고문 나오기
#단어가 1개이상일때 
        if len(self.EngRdWord)>=1:
            if len(self.EngRdWord)>8:
                    self.rstBg2.create_text(180,490,text="*단어가 많아 일부분만 출력합니다.",font=('맑은고딕',10,))
            for i in range(len(self.EngRdWord)):
                self.rstBg2.create_text(100,50*i+60,text=self.EngRdWord[i][1],font=("맑은고딕",20,"bold"))
                if self.rst[i]=='correct':
                    self.rstBg2.create_text(280,50*i+60,text=self.rst[i],font=("맑은고딕",20,"bold"),fill='green')
                else:
                    self.rstBg2.create_text(280,50*i+60,text=self.rst[i],font=("맑은고딕",20,"bold"),fill='red')
        #단어가 1개일때
        else:
            self.rstBg2.create_text(100,60,text=self.EngRdWord[0][1],font=("맑은고딕",20,"bold"))
            self.rstBg2.create_text(250,60,text=self.rst[0],font=("맑은고딕",20,"bold"))
            
        totalNumofWord=len(self.EngRdWord)
        self.rstBg2.create_text(180,530,text=str(self.count)+'/'+str(totalNumofWord),font=("HY헤드라인M",25,))
        
        self.rstExit=Image.open('C:/english-learning-program/image/exit_bt.png')
        resized_rstExit=self.rstExit.resize((30,30),Image.ANTIALIAS)
        self.new_rstexit=ImageTk.PhotoImage(resized_rstExit)
       
        self.rstExitBt=tk.Button(self,image=self.new_rstexit,bg='white',bd=0,command=self.destroy_resultPage)
        self.rstExitBt.place(x=570,y=580)
    
    def ok_click(self):
        self.destroy()
        self.master.switch_frame(LearningMenu.LearningMenu)
        
        
    def restart(self):
        self.gui_frame()
        
    def gui_frame(self):
        
        self.rpt=RptWord()
        self.EngRdWord=copy.deepcopy(self.rpt.setWordforRpt())
        self.message=None
        
        print("reviewpage set: ",self.EngRdWord)
        
        if len(self.EngRdWord) == 0 :
            self.message=tk.messagebox.showinfo("경고",gl_user.get_name()+"님은 복습할 정보가 없으십니다.")
        if self.message == 'ok':
            self.ok_click()    
        
        self.count=0
        self.writtenWord.clear() 
        #self.rst.clear()
        background=Image.open("C:/english-learning-program/image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        
        self.bg_frame=tk.Frame(self)
        self.bg_frame.place(x=76,y=25,width=844,height=737)
        
        self.bg=tk.Canvas(self.bg_frame,width=844,height=739,bg="#FCD4B4") #4칸 빼면 880
        self.bg.pack()
        
        self.rpt_widget1=tk.Label(self,text="복습하기",font=("맑은 고딕",40,),fg="#404040",bg="#F5B296",justify="center")
        self.rpt_widget1.place(x=78,y=60,width=840,height=100)
        
        #주의 사항 위젯 구현 
        self.rpt_bg2=tk.Label(self,text="주의: 한글 뜻을 입력한뒤 enter를 눌러주세요",bg="white")
        self.rpt_bg2.place(x=78,y=420,width=840,height=40)
        
         #영어 단어위젯 구현
        self.text=tk.StringVar()
        #초기 영단어 설정
        self.setWord()
        self.wordWidget=tk.Label(self.bg_frame,textvariable=self.text,font=("맑은 고딕",50,),bg="white",justify="center")
         #단어답 입력박스 구현
        self.txtBox=tk.Entry(self,font=("맑은 고딕",30,),fg="#404040",bg="#A6A6A6",justify="center")
        self.txtBox.place(x=90,y=480,width=817,height=210)
        
        #entry 엔터 이벤트 저장으로 처리
        self.txtBox.bind("<Return>",self.save)
        
        print(self.EngRdWord)
        self.wordWidget.place(x=10,y=150,width=815,height=225)
        
        
        #다시하기 버튼 구현
        RtnTo=Image.open("C:/english-learning-program/image/restart.png")
        #이미지 크기 재조정
        RtnTo_resized=RtnTo.resize((100,50),Image.ANTIALIAS)
        RtnToInit=ImageTk.PhotoImage(RtnTo_resized) #크기조정
        self.rtnToInit=tk.Button(self,image=RtnToInit,bg="#FCD4B4",justify="center",bd=0,command=self.restart)
        self.rtnToInit.place(x=95,y=697,width=100,height=50)

        self.mainloop()
        
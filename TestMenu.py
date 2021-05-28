import tkinter as tk
import os
from PIL import Image,ImageTk
import TestPage

#######만약에 이미지가 안나오고 이미지가 없다는 오류가 뜨면 이미지에 create image나 place해놓은거 주석처리해서 한번 실행하구
#######껏다가 주석풀고 실행해주세요(왜그런지는 모르겠어요)   
   
class TestInitGui(tk.Frame):

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master=master
        self.pack()
        self.set_frame()
        
    def next_page(self):
        self.destroy()
        self.master.switch_frame(TestPage.Test)
        
    #프레임 설정    
    def set_frame(self):
        
        #########모눈종이 깔기######
        self.monunPaper=tk.Canvas(self,width=1000,height=800,bg='white')
        self.monunPaper.pack()
        monunImg=Image.open('image/monun.png')
        resized_monunImg=monunImg.resize((1000,800),Image.ANTIALIAS)
        new_monunImg=ImageTk.PhotoImage(resized_monunImg)
        self.monunPaper.create_image(0,0,anchor=tk.NW,image=new_monunImg)
        
        ########배경 만들기########
        #바탕 연파랑색
        self.bg1=tk.Canvas(self,width=840,height=735,bg='#94D8F6')
        self.bg1.place(x=75,y=25)
        #중간에 있는 진파랑색선
        self.bottomLine=tk.Canvas(self,width=840,height=20,bg='#3A8FE4')
        self.bottomLine.place(x=75,y=480)
        #제목에 캔버스 쌓아놓고 'TEST'출력
        self.titleBg=tk.Canvas(self,width=800,height=200,bg='white')
        self.titleBg.place(x=95,y=100)
        self.titleBg2=tk.Canvas(self,width=780,height=180,bg='#94D8F6')
        self.titleBg2.place(x=105,y=110)
        self.titleBg2.create_text(400,90,text='TEST',font=('맑은 고딕',70,'bold'),fill='#404040')
        #사용방법버튼 만들기
        howToUseImg=Image.open('image/howToUseButton.png')
        resized_howToUseImg=howToUseImg.resize((30,29),Image.ANTIALIAS)
        new_howToUseImg=ImageTk.PhotoImage(resized_howToUseImg)
        self.howToUseBt=tk.Button(self,image=new_howToUseImg,bg='#94D8F6',bd=0,command=self.howToUse_Create)
        self.howToUseBt.place(x=490,y=350)
        #시작버튼 만들기(프레임 연결 필요)
        startBtImg=Image.open('image/startButton.png')
        resized_startImg=startBtImg.resize((200,200),Image.ANTIALIAS)
        new_startImg=ImageTk.PhotoImage(resized_startImg)
        self.startBt=tk.Button(self,image=new_startImg,bd=0,bg='#94D8F6',command=self.next_page)
        self.startBt.place(x=405,y=400)
       
        self.mainloop()
        
    #사용방법버튼눌럿을때 실행되는 메소드    
    def howToUse_Create(self):
        #사용방법 바탕 캔버스(하얀색)
        self.HTU_canvas=tk.Canvas(self,width=400,height=400,bg='white')
        self.HTU_canvas.place(x=300,y=50)
        self.HTU_canvas.create_text(210,130,text='테스트는 총 10문제로 구성되며'
                                    ,font=('맑은 고딕',10,))
        self.HTU_canvas.create_text(210,160,text='단어범위는 데이터에 있는 단어 전체입니다.'
                                    ,font=('맑은 고딕',10,))
        self.HTU_canvas.create_text(210,200,text='해당영어나 한글에 맞는'
                                    ,font=('맑은 고딕',10,)) 
        self.HTU_canvas.create_text(210,240,text='한글,영어뜻을 적어 저장버튼을 눌러주세요 '
                                    ,font=('맑은 고딕',10,))                                                       
        #사용방법 나가기 버튼
        self.HTU_exitImg=Image.open('image/exitButton.png')
        self.resized_exitImg=self.HTU_exitImg.resize((40,40),Image.ANTIALIAS)
        self.new_HTU_exitImg=ImageTk.PhotoImage(self.resized_exitImg)
        self.HTU_exitBt=tk.Button(self,image=self.new_HTU_exitImg,bd=0,bg='white',command=self.howToUse_Exit)
        self.HTU_exitBt.place(x=650,y=400)
    #사용방법나가기버튼을 눌럿을때 실행되는 메소드
    def howToUse_Exit(self):
        self.HTU_canvas.destroy()
        self.HTU_exitBt.destroy()

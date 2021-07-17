import tkinter as tk 
import os
from PIL import Image,ImageTk
import random
from global_vari import wordlist,gl_user
import LearningMenu
#######만약에 이미지가 안나오고 이미지가 없다는 오류가 뜨면 이미지에 create image나 place해놓은거 주석처리해서 한번 실행하구
#######껏다가 주석풀고 실행해주세요(왜그런지는 모르겠어요)   
class Test(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master=master
        self.pack()
        
        self.temp_for_Random=[]
        for i in range(len(wordlist)):
            self.temp_for_Random.append([wordlist[i].get_wordNum(),wordlist[i].get_english(),wordlist[i].get_korean()])
        #전체 단어에서 중복되지 않게 10개만 뽑아서 temp2에 저장
        
        self.temp2=random.sample(self.temp_for_Random,10)
        print(self.temp2)#단어잘저장됬는지 체크하는거(지워도 되여)
        self.writtenWord=[]
        self.count_forCal=0
#############################추가(수정)한 부분##########################
        self.correctWronglist=[] #correct wrong 출력하는 위젯 위해서 만들었어요
        self.knowWord_num=[]    #userinfo 갱신을 위해서 만들었어요
        self.notknowWord_num=[] #userinfo 갱신을 위해서 만들었어요
#################################################################        
        self.set_frame()

    def back_page(self):
        self.master.click_sound(True)
        
        self.destroy()
        self.master.switch_frame(LearningMenu.LearningMenu)
        #뜻을 입력할수 있는 엔트리박스 세팅(for문으로 하면 값을 저장을 못해서 이렇게 했어요)
    def set_entryBox(self):      
        
        xvar = 550
        yvar = 100
        self.entrys=[]
          # 점수 표기 레이블

        for i in range(10):
            self.entrys.append(tk.Entry(self,font=('맑은 고딕',20,),fg="#404040",bg="#A6A6A6",justify="center"))
            self.entrys[i].place(x=xvar,y=yvar,width=150,height=40)
            yvar = yvar + 60
            
    def set_frame(self):
#         ##모눈종이 깔기
         self.monunPaper=tk.Canvas(self,width=1000,height=800,bg='white')
         self.monunPaper.pack()
         monunImg=Image.open('image/monun.png')
         resized_monunImg=monunImg.resize((1000,800),Image.ANTIALIAS)
         new_monunImg=ImageTk.PhotoImage(resized_monunImg)
         self.monunPaper.create_image(0,0,anchor=tk.NW,image=new_monunImg)

        
#         ##배경만들기
#         #바탕 연파랑색
         self.bg1=tk.Canvas(self,width=840,height=735,bg='#2A8DD4')
         self.bg1.place(x=75,y=25)
         self.bg2=tk.Canvas(self,width=800,height=695,bg='white')
         self.bg2.place(x=95,y=45)
        
        
#         ##임시용 영어 단어(전체단어에서 10개 뽑아서 섞기 필요해여)
        
#         #한글영어 번갈아가면서 출력되게 구현
         for i in range(len(self.temp2)):
             if i%2==0:
                 tk.Label(self,text=self.temp2[i][1],font=('맑은 고딕',20,),bg='white').place(x=300,y=60*i+100)
             else:
                 tk.Label(self,text=self.temp2[i][2],font=('맑은 고딕',20,),bg='white').place(x=300,y=60*i+100)
         #뜻입력창 구현 
         self.set_entryBox()
                
#         ##제출버튼
         submitImg=Image.open('image/submitButton.png')
         resized_submitImg=submitImg.resize((240,85),Image.ANTIALIAS)
         new_submitImg=ImageTk.PhotoImage(resized_submitImg)
         self.submitBt=tk.Button(self,image=new_submitImg,bg='white',bd=0,command=self.submit_and_showResult) #,command=self.submit_and_showResult
         self.submitBt.place(x=375,y=710)
        
         ##종료버튼
         exitImg=Image.open('image/exitTestButton.png')
         resized_exitImg=exitImg.resize((90,90),Image.ANTIALIAS)
         new_exitImg=ImageTk.PhotoImage(resized_exitImg)
         tk.Button(self,image=new_exitImg,bg='white',bd=0,command=self.back_page).place(x=803,y=648)
        
         self. mainloop()
    def submit_and_showResult(self):
         self.master.click_sound(True)
        
#         #제출한 답 저장(입력받은 한글뜻은 뒤에 \n이 붙어야 채점을 올바르게 해서 붙임)
         
         self.writtenWord.clear()
         for i in range(10):
             self.writtenWord.insert(i,str(self.entrys[i].get()))
         print(self.writtenWord)
         self.cal() #채점
         self.destroy_entry()#한번답을 제출하면 다시 못적게 엔트리 박스를 지운다
         self.submitBt.destroy()
# #############################추가(수정)한 부분##########################
        
         for i in range(len(self.temp2)):
             tk.Label(self,text=self.correctWronglist[i],font=('맑은 고딕',20,),bg='white').place(x=600,y=60*i+100)
#         #결과창 생성
         self.result_canvas=tk.Canvas(self,width=400,height=400,bg='#2A8DD4')
         self.result_canvas.place(x=300,y=160)
         self.result_canvas2=tk.Canvas(self,width=370,height=370,bg='white')
         self.result_canvas2.place(x=315,y=175)
#         #결과값 출력
         self.result_canvas2.create_text(190,100,text='맞힌 갯수',font=('맑은 고딕',20,),fill='green')
         self.result_canvas2.create_text(190,180,text=str(self.count_forCal)+'/'+str(len(self.writtenWord))
                                        ,font=('맑은 고딕',50,),fill='green')
         self.result_canvas2.create_text(190,300,text='틀린단어를 다시공부하려면 복습하기로 이동하세요',
                                         font=('맑은 고딕',10,))
# #################################################################
        
#         #결과창나가기버튼
         self.result_exitImg=Image.open('image/exitButton.png')
         self.resized_result_exitImg=self.result_exitImg.resize((30,30),Image.ANTIALIAS)
         self.new_result_exitImg=ImageTk.PhotoImage(self.resized_result_exitImg)
         self.result_exitBt=tk.Button(self,image=self.new_result_exitImg,bg='white',bd=0,command=self.destroy_resultPage)
         self.result_exitBt.place(x=650,y=510)
        

    def cal(self):
         for i in range(len(self.writtenWord)):
             #짝수인 단어들은 한글단어로 문제를 냈으므로 영어뜻과 일치하면 점수(count_forCal)에 1점 올리고 
             if i%2!=0:
                 if self.writtenWord[i]==self.temp2[i][1]:
                     self.count_forCal=self.count_forCal+1
                     self.correctWronglist.insert(i,'correct') #wrong correct 출력을 위해 리스트에 저장
                     self.knowWord_num.append(self.temp2[i][0]) #user텍파 갱신을 위해서 맞은거 번호 리스트에 저장
                 else:
                     self.correctWronglist.insert(i,'wrong')
                     self.notknowWord_num.append(self.temp2[i][0])
             #홀수인 단어들은 영어단어로 문제를 냈으므로 한글뜻과 일치하면 점수에 1점 올리기
             else: #홀수인 단어들은 영어단어로 문제를 냈으므로 한글 뜻과 일치하면 점수에 1점 올리기(위의 if문과 비슷해요)
                 if self.writtenWord[i]==self.temp2[i][2]:
                     self.count_forCal=self.count_forCal+1
                     self.correctWronglist.insert(i,'correct')
                     self.knowWord_num.append(self.temp2[i][0])
                 else:
                     self.correctWronglist.insert(i,'wrong')
                     self.notknowWord_num.append(self.temp2[i][0])
            
         self.master.insert_info(self.knowWord_num,self.notknowWord_num)
# #################################################################        

#     #제출하면 채점해서 결과를 보여준다. 
#     #한번답을 제출하면 다시 못적게 엔트리 박스를 지운다
    def destroy_entry(self):
         for i in range(10):
             self.entrys[i].destroy()
       
# #############################추가(수정)한 부분##########################       
#     #채점
        
#     #결과출력페이지나가기버튼 누르면 페이지를 지운다                
    def destroy_resultPage(self):
        self.master.click_sound(True)
        self.result_canvas.destroy()
        self.result_canvas2.destroy()
        self.result_exitBt.destroy()
    
#     #맞은단어 틀린단어들 user텍파에 갱신하기 (구현해야되요)

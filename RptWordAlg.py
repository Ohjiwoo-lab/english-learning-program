import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from global_vari import gl_user,wordlist,userlist
import copy

class RptWord:
    def __init__(self):
        self.temp=[]
        self.temp2=[]
        self.wordnum1=[]
        self.finalRptWord=[]
        
    def setWordforRpt(self):
        #첫번째유저의 Know(번호)를 리스트에 저장
        
        if gl_user != None:
            
            self.temp=copy.deepcopy(gl_user.get_know())
            print(self.temp)
            #wordlist의 번호만 리스트에 저장
            for i in range(len(wordlist)):
                self.wordnum1.insert(i,wordlist[i].get_wordNum())    
            print(self.wordnum1)
            #wordlist 전체 2차원 리스트에 저장
            for i in range(len(wordlist)):
                self.temp2.insert(i,[wordlist[i].get_wordNum(),wordlist[i].get_english(),wordlist[i].get_korean()])
        
            #inttemp를 이용해서 wordlist의 영어와 한글을 역추적
            self.finalRptWord.clear()
            for i in self.temp[0]:
                for j in wordlist:
                    if i==j.get_wordNum():
                        self.finalRptWord.insert(i,[j.get_wordNum(),j.get_english(),j.get_korean()]) 
            print(self.finalRptWord)
            return self.finalRptWord

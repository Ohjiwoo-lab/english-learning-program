# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:47:10 2021

@author: user
"""

#word 클래스 정리

from WordInfo import Word

class WordManager:
    
    def __init__(self):
        self.wordlist=[]
        self.wordread()
        
    def wordread(self) :
    #파일읽기 간략한 코드
        with open('C:/Python_project/word.txt','r',encoding='UTF8') as f :
            lines=f.readlines() #파일전체읽기
        
            l=[] #list생성
            for line in lines : #lines에서 읽은 전체 문자열을 한줄 기준으로 line 리스트에 넣기
                l.append(line.split(',')) #line의 한줄 ','기준으로 자르기 
            
            for i in range(len(l)):
                word=Word()
                word.set_init(int(l[i][0]), l[i][1], l[i][2])
                self.wordlist.append(word)

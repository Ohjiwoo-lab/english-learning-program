# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:46:47 2021

@author: user
"""

from PIL import Image, ImageTk
from WordInfo import Word
import pymysql
from global_vari import wordlist,word_img

class WordManager:
    
    def __init__(self):
        self.python_db=None
        #self.wordread()
        #self.word_img()
    def wordread(self) :
    #파일읽기 간략한 코드
         self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
         wordlist.clear()
         try:
             with self.python_db.cursor() as cursor:
                 #usernum를 위함
                 wordSql="select *from word"
                 #username
                 cursor.execute(wordSql)
                 result =cursor.fetchall()
                 for i in range(0,len(result)):
                     word=Word()
                     word.set_init(int(result[i][0]),result[i][1],result[i][2])
                     wordlist.append(word)               
         finally:
                self.python_db.close()

    def readlist(self):
        for i in range(len(wordlist)):
            print(wordlist[i].get_wordNum()," , ",wordlist[i].get_english())
    
    def word_img(self):
        for i in range(len(wordlist)):
            print(wordlist[i])
            image = Image.open("C:/english-learning-program/photo_img/"+wordlist[i].get_english()+".png")
            resized = image.resize((300, 300), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(resized)  # 크기조정
            word_img.append(new_image)
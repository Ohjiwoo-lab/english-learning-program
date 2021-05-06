# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:21:26 2021

@author: user
"""

#사용자 리스트 가져오기
from UserInfo import User

class UserManager:
    def __init__(self):
        self.userlist=[]
        self.set_user()
        
    def set_user(self):
        #파일읽기 간략한 코드
        with open('C:/Python_project/user.txt','r',encoding='UTF8') as f :
            lines=f.readlines() #파일전체읽기
        
            l=[] #list생성
            for line in lines : #lines에서 읽은 전체 문자열을 한줄 기준으로 line 리스트에 넣기
                l.append(line.split(',')) #line의 한줄 ','기준으로 자르기 
            
            self.userlist.clear()
            for i in range(len(l)):
                user=User()
                user.set_init(int(l[i][0]), l[i][1], l[i][2],l[i][3],l[i][4])
                self.userlist.append(user)
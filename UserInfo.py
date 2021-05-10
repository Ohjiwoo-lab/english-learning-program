# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:40:27 2021

@author: user
"""

class User :
    def __init__(self) :
        #__변수이름은 외부에서 변경 불가능
        self.__name=""
        self.__gameTime=0
        self.__know=list();
        self.__notKnow=list();
        self.__UserNum=0
    
    def set_init(self,num,name,gameTime,know,notKnow):
        self.__UserNum=num
        self.__name=name
        self.__gameTime=gameTime
        self.__know=know.split('.')
        self.__notKnow=notKnow.split('.')
        
    def set_name(self,name) :
        self.__name = name
    def set_gameTime(self,gameTime):
        self.__gameTime=gameTime
    def set_know(self,know):
        self.__know=know
    def set_notKnow(self,know):
        self.__notKnow=know
    
    def get_userNum(self):
        return self.__UserNum
    def get_name(self):
        return self.__name
    def get_gameTime(self):
        return self.__gameTime
    def get_know(self):
        return self.__know
    def get_notKnow(self):
        return self.__notKnow
    
        
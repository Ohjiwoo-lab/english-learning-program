# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:52:32 2021

@author: user
"""

class Word :
    
    def __init__(self):
        self.__wordNum=0
        self.__english=""
        self.__korean=""
        self.__fileLink=""
    
    def set_init(self,wordNum,english,korean,fileLink) :
        self.__wordNum=wordNum
        self.__english=english
        self.__korean=korean
        self.__fileLink=fileLink
        
    def set_english(self,english) :
        self.__english=english
    
    def set_korean(self,korean) :
        self.__korean=korean
        
    def set_fileLink(self,fileLink) :
        self.__fileLink=fileLink
    
    def get_wordNum(self) :
        return self.__wordNum
    
    def get_english(self):
        return self.__english
    
    def get_korean(self):
        return self.__korean
    
    def get_fileLink(self):
        return self.__fileLink
    
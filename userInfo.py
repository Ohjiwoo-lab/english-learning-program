class User :
    def __init__(self) :
        #__변수이름은 외부에서 변경 불가능
        self.__UserNum=0
        self.__name=""
        self.__know=list()
        self.__notKnow=list()
    
    def set_init(self,num,name):
        self.__UserNum=int(num)
        self.__name=name
        
    def set_list(self,know=0,notKnow=0):
        self.__know.clear()
        self.__notKnow.clear()
        
        if know is not None :
            self.__know.append(know)
        else:
            self.__know="0"
        if notKnow is not None :
            self.__notKnow.append(notKnow)   
        else:
            self.__know="0"
        
    def set_name(self,name) :
        self.__name = name
    
    def set_know(self,know):
            self.__know.append(know)
        
    def set_notKnow(self,notknow):
            self.__notKnow.append(notknow)
   
    def delete_notKnow(self,i):
        print("temp[i]",self.__notKnow.remove[i])
        del self.__notKnow[self.__notKnow.index(i)]
        #self.__notKnow.remove(i)
        
    def get_userNum(self):
        return self.__UserNum
    def get_name(self):
        return self.__name
    def get_know(self):
        return self.__know
    def get_notKnow(self):
        return self.__notKnow
            
    def get_line(self):
        return str(self.__UserNum)+","+self.__name+","+self.__gameTime+","+self.join_know(),self.join_notknow()
    
    def join_know(self): #문자열로 연결된 아는 단어 연결.
        line='.'.join(self.__know)
        return line
    
    def join_notknow(self): #문자열로 연결된 모르는 단어 연결 -> 디비에선 안사용할텐데?
        line='.'.join(self.__notKnow)
        return line
    
import copy
class User :
    def __init__(self) :
        #__변수이름은 외부에서 변경 불가능
        self.__UserNum=0
        self.__name=""
        self.__know=None
        self.__notKnow=None
    
    def set_init(self,num,name):
        self.__UserNum=int(num)
        self.__name=name
    
    def set_list2(self):
        self.__know=[]
        self.__notKnow=[]
        
    def set_list(self,know,notKnow):
        self.__know=[]
        self.__notKnow=[]
        
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
        try:
            self.__know.append(copy.deepcopy(know))
        except:
            pass
    def set_notKnow(self,notknow):
        try:
            self.__notKnow.append(copy.deepcopy(notknow))
        except:
            pass
    def delete_notKnow(self,i):
        try:
            if self.__notKnow[i] in self.__notKnow: 
                print('리스트에 값이 있습니다.')
                del self.__notKnow[int(i)]
            else: 
                print('리스트에 값이 없습니다.')
        except:
            print("예외")
            pass

        #self.__notKnow.remove(i)
        
    def get_userNum(self):
        return self.__UserNum
    def get_name(self):
        return self.__name
    def get_know(self):
        return self.__know
    def get_notKnow(self):
        return self.__notKnow
  
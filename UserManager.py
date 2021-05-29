from UserInfo import User
from global_vari import gl_user,userlist
import pymysql
import copy

class UserManager:
    def __init__(self):
        self.python_db=None
        self.set_user()
        
    def set_user(self): #데이터 베이스 연결 및 userlist 초기화
         self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
         
         userlist.clear()
         try:
             with self.python_db.cursor() as cursor:
                 #usernum를 위함
                 numSql="select *from user"
                 #username
                 cursor.execute(numSql)
                 result =cursor.fetchall()
                 for i in range(0,len(result)):
                     user = User()
                     user.set_init(result[i][0],result[i][1])
                     userlist.append(user)
                
                 wordSql="select *from know_info"
                 cursor.execute(wordSql)
                 info=cursor.fetchall()
                 
                 for i in range(len(userlist)):
                     for j in range(len(info)):
                         if userlist[i].get_userNum() == info[j][0]:
                             userlist[i].set_know(info[j][1])
                
                 wordSql="select *from notknow_info"
                 cursor.execute(wordSql)
                 info=cursor.fetchall()
                 
                 for i in range(len(userlist)):
                     for j in range(len(info)):
                         if userlist[i].get_userNum() == info[j][0]:
                             userlist[i].set_notKnow(info[j][1])
                 print(gl_user.get_notKnow())
                 print(userlist[0].get_know())
         finally:
            self.python_db.close()
         
    def insert_user(self):
        if gl_user is not None :
            
         self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
         
         try:
             with self.python_db.cursor() as cursor:
                 #usernum를 위함
                 #insert과정
                 userSql="insert into user values (%s,%s)"
                 user_info=(str(gl_user.get_userNum()),gl_user.get_name())
                
                 #username
                 cursor.execute(userSql,user_info)
                 self.python_db.commit()
                 userlist.append(gl_user)
                
         finally:
            self.python_db.close()
        
        else:
            print("user가 없음")
    def insert_info(self):
        if gl_user is not None :
            
         self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
         
         try:
             with self.python_db.cursor() as cursor:
                 #usernum를 위함
                 #insert과정
                 userSql="insert into user values (%s,%s)"
                 user_info=(str(gl_user.get_userNum()),gl_user.get_name())
                
                 #username
                 cursor.execute(userSql,user_info)
                 self.python_db.commit()
                 userlist.index(gl_user)
                
         finally:
            self.python_db.close()
        
        else:
            print("user가 없음")
    
    def insert_knowInfo(self,insert):
        
        if gl_user is not None:
            
            self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
            
            try:
                with self.python_db.cursor() as cursor:
                    knowSql="insert into know_info values (%s,%s)"
                 
                    know_info=(str(gl_user.get_userNum()),str(insert))
                    cursor.execute(knowSql,know_info)
                    self.python_db.commit()
            finally:
                self.python_db.close()

    def delete_notKnowInfo(self,delete):
        if gl_user is not None:
            
            self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')     
            try:
                with self.python_db.cursor() as cursor:
                    notknowSql="delete from notknow_info where notknow=%s"
                
                    for i in range(len(delete)):
                        cursor.execute(notknowSql,str(delete[i]))
                        self.python_db.commit()
            
                    temp = copy.deepcopy(gl_user.get_notKnow())
                    print("usermanager(temp): ",temp,len(temp[0]))
                    for i in range(len(temp[0])):
                        try:
                            if temp[0][i] == delete[i]:
                                print("delete[i] ",delete[i]," **temp[i] ",temp[0][i])
                                gl_user.delete_notKnow(i)
                        except:
                           pass
                        print("usermanager(get_notknow): ",gl_user.get_notKnow())
            finally:
                self.python_db.close()

    def insert_knowInfo(self,insert):
        
        if gl_user is not None:
            
            self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
            
            try:
                with self.python_db.cursor() as cursor:
                    knowSql="insert into know_info values (%s,%s)"
                    for i in range(len(insert)):
                        know_info=(str(gl_user.get_userNum()),str(insert[i]))
                        cursor.execute(knowSql,know_info)
                        self.python_db.commit()
                        
                    gl_user.set_know(insert)
                    print("1:usermanager(get_know): ",gl_user.get_know())
            finally:
                self.python_db.close()
                
    def insert_notknowInfo(self,insert):
        
        if gl_user is not None:
            
            self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
            
            try:
                with self.python_db.cursor() as cursor:
                    knowSql="insert into notknow_info values (%s,%s)"
                    for i in range(len(insert)):
                        know_info=(str(gl_user.get_userNum()),str(insert[i]))
                        cursor.execute(knowSql,know_info)
                        self.python_db.commit()
                        
                    gl_user.set_notKnow(insert)
                    print("2:usermanager(get_notknow): ",gl_user.get_notKnow())
            finally:
                self.python_db.close()
                
    def insert_notknowInfo_int(self,wrong_num):
                
        if gl_user is not None:
            
            self.python_db=pymysql.connect(host='localhost',user='root',password='hdoo517a*',db='python_project',charset='utf8')
            
            try:
                with self.python_db.cursor() as cursor:
                    knowSql="insert into notknow_info values (%s,%s)"
                    
                    notknow_info=(str(gl_user.get_userNum()),str(wrong_num))
                    cursor.execute(knowSql,notknow_info)
                    self.python_db.commit()
                    gl_user.set_notKnow(wrong_num)
                    print(gl_user.get_notKnow())
            finally:
                self.python_db.close()

        
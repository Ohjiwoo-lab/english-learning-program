from tkinter import *
import time
arr=[]
arr_an=[]
i=0
f = open('db.txt', 'r', encoding='UTF8')
x = open('db_done.txt', 'a', encoding='UTF8')

while True:
    line = f.readline()
    if not line:        # 더 이상 읽을게 없다면
        break        # 끝내라
    strings=line
    string_a = strings.split(',')
    arr.append(string_a[1])
    string_b=string_a[2].split('\n')
    arr_an.append(string_b[0])
    i=i+1 # 단어개
    
def init():
    global pp
    textbox.focus()
    name.set("")
    label3.place_forget()
    label4.place_forget()

    
def press_left():
    global pp
    label3.place_forget()
    label4.place_forget()
    name.set("")
    if pp > 0 :
        right.place(x=932, y=410)
        pp-=1
        label1.config(text=arr[pp])
        init()
        
    if pp==0:
        left.place_forget()
    
def press_right():
    global pp

    if pp < i-1 :
        left.place(x=32, y=410)
        pp+=1
        label1.config(text=arr[pp])
        label3.place_forget()
        label4.place_forget()
        name.set("")
        init()
        
    if pp==i-1:
        right.place_forget()



def callback(event):
    a=textbox.get()
    x = open('db_done.txt', 'a', encoding='UTF8')

    if a==arr_an[pp]:
        label4.place_forget()
        label3.place(x=90, y=350)
        name.set("")
        press_right()
        data = str(pp) + "," + arr[pp] + "," + arr_an[pp] + ",O\n"
        
    else:
        label3.place_forget()
        label4.place(x=90, y=350)
        name.set("")
        data = str(pp) + "," + arr[pp] + "," + arr_an[pp] + ",X\n"
    x.write(data)
    x.close()
    
root = Tk()

root.title("학습하기")
root.geometry("1000x800")

pp = 0

wall = PhotoImage(file = "background.png") 
wall_label = Label(image = wall) 
wall_label.place(relx=.5, rely=.5, anchor="center")

b1=Button(root, text="학습하기",fg = "white",bg = "orange", font=("맑은 고딕",25))
b1.config(width=14, state='disabled')
b1.place(x=90, y=27)

b2=Button(root, text="단어카드", font=("맑은 고딕",25))
b2.config(width=14)
b2.place(x=366, y=27)

b3=Button(root, text="테스트", font=("맑은 고딕",25))
b3.config(width=14)
b3.place(x=642, y=27)

label1 = Label(root, text = "a",bg = "white", font=("맑은 고딕",40));
label1.config(width=27, height=4)
label1.place(x=90, y=140)

label2 = Label(root, text = "정답을 입력하세요.",bg = "white",fg = "gray", font=("맑은 고딕",40));
label2.config(width=27, height=4)
label2.place(x=90, y=431)

label4 = Label(root, text = "틀렸습니다!",bg = "white", font=("맑은 고딕",40),fg="red");
label4.config(width=27, height=1)
label4.place(x=90, y=350)

label3 = Label(root, text = "정답입니다!",bg = "white", font=("맑은 고딕",40),fg="blue");
label3.config(width=27, height=1)
label3.place(x=90, y=350)



b4=Button(root, text="단어 목록 보기",bg = "gray")
b4.config(width=117, height=2)
b4.place(x=90, y=723)

left=Button(root, text="  L  ",command=press_left)
left.place(x=32, y=410)
left.place_forget()

right=Button(root, text="  R  ",command=press_right)
right.place(x=932, y=410)

name = StringVar()
textbox = Entry(root, width=16, textvariable=name, font=("맑은 고딕",40),fg = "gray", justify=CENTER, bd = 0)
textbox.place(x=270, y=531)

root.bind('<Return>', callback)

init()

root.mainloop()



import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import CardMenu
import CardLevelFour
import CardSuccess

class LevelThree(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master=master
        self.clock = 300

        self.canvas = tk.Canvas(self, width=1000, height=800)
        self.canvas.pack()
        background=Image.open("image/background.png")
        #이미지 크기 재조정
        resized=background.resize((1000,800),Image.ANTIALIAS)
        new_background=ImageTk.PhotoImage(resized) #크기조정
        self.canvas.create_image(0,0,anchor=tk.NW,image=new_background)
        
        self.gui_frame()
        
    def gameOver_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardLevelFour.LevelFour(self.master, 3))

    def Success_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardSuccess.LevelFive)

    def back_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardMenu.CardMenuPage)
        
    def gui_frame(self):

        # 배경 상자
        self.bac = tk.Canvas(self, width=780, height=525, bg="black")
        self.bac.pack()

        wall = tk.PhotoImage(file="image/background3.png")
        self.canvas.create_image(110, 95, anchor=tk.NW, image=wall)

        # 타이머, 점수 있는 곳 상자
        self.title = tk.Canvas(self, width=780, height=525, bg="black")
        self.title.pack()

        wall2 = tk.PhotoImage(file="image/background4.png")
        self.canvas.create_image(130, 130, anchor=tk.NW, image=wall2)

        img = tk.PhotoImage(file="image/title.png")
        title_label = tk.Label(self, image=img)
        title_label.place(x=110, y=25)
    
        xvar = 130
        yvar = 250
        buttons = []
        cardCount = 0

        for i in range(5):
            for j in range(6):
                buttons.append(tk.Button(self, bg='#8FAADC', width=16, height=5))
                buttons[cardCount].place(x=xvar, y=yvar)
                xvar = xvar + 125
                cardCount += 1

            xvar = 130
            yvar = yvar + 90

        fontStyle = tkFont.Font(family="맑은 고딕", size=28, weight='bold')
        fontStyle2 = tkFont.Font(family="G마켓 산스 Light", size=20, weight='bold')

        # 점수 표기 레이블
        tk.Label(self, text='제한 시간(5분)', font=fontStyle2, bg='white', fg='black').place(x=140, y=160)
        tk.Label(self, text='0 / 15', font=fontStyle, bg='white', fg='black').place(x=745, y=143)

        # 중간에 나가기
        finish_img = tk.PhotoImage(file="image/finish.png")
        btn = tk.Button(self, image=finish_img, bg='white', width=40, height=40, command=self.back_page, relief='flat')
        btn.place(x=905, y=705)

        # 타이머
        self.createWidgets()
        
        self.mainloop()

    # 타이머
    def createWidgets(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 30), bg='white', fg='black')
        self.time.place(x=340, y=150)
        self.time["textvariable"] = self.now

        self.xlab = 470
        self.ment = tk.Label(self, text="", font=('Helvetica', 20), bg='white', fg='black')
        self.ment.place(x=self.xlab, y=155)
        self.ment['text'] = '화이팅~! 화이팅~!'

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        if self.clock == 0:
            self.gameOver_page()

        if self.clock <= 10:
            self.time["fg"] = 'red'
            self.xlab = 430
            self.ment.place(x=self.xlab, y=155)
            self.ment['text'] = '시간이 얼마 안남았어요...'
            self.ment['fg'] = 'red'

        minute, second = self.convert(self.clock)
        self.now.set(str(minute) + ':' + str(second))
        self.clock -= 1
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

    def convert(self, seconds):
        """
        Convert seconds to (seconds, minutes, hours, remainder_seconds)
        """
        r = seconds

        s = r % 60
        m = (r - s) % (60 * 60)

        # 시간 단위는 안 쓰므로 생략
        # h = (r - s - m) % (60*60*60)

        return int(m / 60), s  # int(h/(60*60))



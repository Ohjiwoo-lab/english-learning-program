
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import CardMenu
import CardLevelOne
import CardLevelTwo
import CardLevelThree

class LevelFour(tk.Frame):

    def __init__(self, master, num):
        tk.Frame.__init__(self, master)
        self.master = master
        self.canvas = tk.Canvas(self, width=1000, height=800)
        self.pack()
        self.canvas.pack()

        background = Image.open("image/background.png")
        # 이미지 크기 재조정
        resized = background.resize((1000, 800), Image.ANTIALIAS)
        new_background = ImageTk.PhotoImage(resized)  # 크기조정
        self.canvas.create_image(0, 0, anchor=tk.NW, image=new_background)

        self.num = num

        self.gui_frame()

    def restart_Page(self):
        if self.num == 1:
            self.canvas.delete("all")
            self.destroy()
            self.master.switch_frame(CardLevelOne.LevelOne)
        elif self.num == 2:
            self.canvas.delete("all")
            self.destroy()
            self.master.switch_frame(CardLevelTwo.LevelTwo)
        elif self.num == 3:
            self.canvas.delete("all")
            self.destroy()
            self.master.switch_frame(CardLevelThree.LevelThree)

    def back_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardMenu.CardMenuPage)

    def gui_frame(self):
        # 배경 상자
        self.bac = tk.Canvas(self, width=780, height=525, bg="black")
        self.bac.pack()

        wall = tk.PhotoImage(file="image/background5.png")
        self.canvas.create_image(110, 130, anchor=tk.NW, image=wall)

        # 타이틀
        img = tk.PhotoImage(file="image/title.png")
        title_label = tk.Label(self, image=img)
        title_label.place(x=110, y=25)

        fontStyle = tkFont.Font(family="Ink Free", size=110, weight='bold')
        fontStyle2 = tkFont.Font(family="G마켓 산스 Light", size=35, weight='bold')

        label = tk.Label(self, text="Game Over", font=fontStyle, fg='#C00000', bg="#A6A6A6")
        label.place(x=130, y=190)

        label1 = tk.Label(self, text="제한시간을 초과하였습니다!", font=fontStyle2, fg='#C00000', bg="#A6A6A6")
        label1.place(x=160, y=380)

        img2 = tk.PhotoImage(file="image/restart.png")
        img3 = tk.PhotoImage(file="image/exit.png")
        img4 = tk.PhotoImage(file="image/sad.png")

        tk.Button(self, image=img2, bg='white', width=330, height=80, command=self.restart_Page).place(x=150, y=510)
        tk.Button(self, image=img3, bg='white', width=330, height=80, command=self.back_page).place(x=510, y=510)
        label2 = tk.Label(self, image=img4, bg="#A6A6A6", relief='flat')
        label2.place(x=750, y=360)

        self.mainloop()






import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import CardMenu

class LevelFive(tk.Frame):

    def __init__(self, master):
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

        self.gui_frame()

    def back_page(self):
        self.canvas.delete("all")
        self.destroy()
        self.master.switch_frame(CardMenu.CardMenuPage)

    def gui_frame(self):
        # 배경 상자
        self.bac = tk.Canvas(self, width=780, height=525, bg="black")
        self.bac.pack()

        wall = tk.PhotoImage(file="image/background6.png")
        self.canvas.create_image(110, 130, anchor=tk.NW, image=wall)

        # 타이틀
        img = tk.PhotoImage(file="image/title.png")
        title_label = tk.Label(self, image=img)
        title_label.place(x=110, y=25)

        fontStyle = tkFont.Font(family="Ink Free", size=110, weight='bold')
        fontStyle2 = tkFont.Font(family="G마켓 산스 Light", size=36, weight='bold')

        label = tk.Label(self, text="Game Clear", font=fontStyle, fg='#7030A0', bg="#FFD966")
        label.place(x=130, y=210)

        label1 = tk.Label(self, text="게임을 통과하셨습니다~", font=fontStyle2, fg='#7030A0', bg="#FFD966")
        label1.place(x=270, y=430)

        img2 = tk.PhotoImage(file="image/back.png")
        img3 = tk.PhotoImage(file="image/success.png")

        tk.Button(self, image=img2, bg="#FFD966", width=385, height=75, command=self.back_page).place(x=300, y=520)
        label2 = tk.Label(self, image=img3, bg="#FFD966", relief='flat')
        label2.place(x=130, y=380)

        self.mainloop()

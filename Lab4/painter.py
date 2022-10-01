from tkinter import Tk, Canvas, PhotoImage, Button

class Painter(Tk):
    def __init__(self):
        super().__init__()
        self.title("RatPainter")

        self.create_buttons_palet()
        win_width = self.winfo_screenwidth()
        win_height = self.winfo_screenheight()

        canv = Canvas(self, width=win_width, height=win_height, bg="white")
        canv.grid(row=2, columnspan=5)
        self.img = PhotoImage(width=win_width, height=win_height)
        canv.create_image((win_width / 2, win_height / 2), image=self.img, state="normal")
        self.mainloop()

    def create_buttons_palet(self):
        button1=Button(self, text="button1")
        button1.grid(row=1,column=0)

        button2=Button(self, text="button2")
        button2.grid(row=1,column=1)

        button3=Button(self, text="button3")
        button3.grid(row=1,column=2)

        button4=Button(self, text="button4")
        button4.grid(row=1,column=3)

        button5=Button(self, text="button5")
        button5.grid(row=1,column=4)
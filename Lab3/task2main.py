from tkinter import Tk, Canvas, PhotoImage
from draw_line import *

class canvas_control:
    def __init__(self):
        self.root_main = Tk()
        self.root_main.title("Draw Line")

        win_width = self.root_main.winfo_screenwidth() // 2
        win_height = self.root_main.winfo_screenheight() // 2

        canv = Canvas(self.root_main, width=win_width, height=win_height, bg="white")
        self.img = PhotoImage(width=win_width, height=win_height)
        canv.create_image((win_width / 2, win_height / 2), image=self.img, state="normal")

        self.root_main.bind("<ButtonRelease-1>", self.draw_wu)
        self.root_main.bind("<ButtonRelease-3>", self.draw_breth)
        self.root_main.bind("<ButtonRelease-2>", self.save_img)

        self.p1_wu = None
        self.p1_be = None

        canv.pack()
        self.root_main.mainloop()

    def draw_wu(self, event):
        c1 = (0, 0, 255)
        if self.p1_wu is None:
            self.p1_wu = (event.x, event.y)
        else:
            line_wu(self.img, self.p1_wu[0], self.p1_wu[1], event.x, event.y, (255, 255, 255), c1)
            self.p1_wu = None
        return

    def draw_breth(self, event):
        c1 = (0, 0, 255)
        if self.p1_be is None:
            self.p1_be = (event.x, event.y)
        else:
            line_bresenchem(self.img, (self.p1_be[0], self.p1_be[1]), (event.x, event.y), c1)
            self.p1_be = None
        return
    
    def save_img(self, event):
        self.img.write("output.png", format="png")
        return

if __name__ == "__main__":
    cc = canvas_control()

    
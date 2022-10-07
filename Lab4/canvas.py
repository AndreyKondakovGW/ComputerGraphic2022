from tkinter import Canvas, PhotoImage

class MyCanvas(Canvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.content = []
        self.af_point = None # точка для аффинных преобразований

        self.create_image()
    
    def redraw_content(self):
        self.clear()
        if self.af_point is not  None:
            self.draw_circle(self.af_point[0], self.af_point[1], r=2)
        for fig in self.content:
            fig.draw(self)

    def draw_intersections_with_line(self, p0, p1):
        intersections = []
        for fig in self.content:
            intersections += fig.find_intersec(p0, p1)

        for p in intersections:
            self.draw_circle(p[0], p[1])

    def select_figs_in_rect(self, p0, p1):
        for fig in self.content:
            if fig.in_rect(p0, p1):
                fig.color = (255, 0, 0)
                fig.selected = True
        self.redraw_content()

    def deselect_figs(self):
        for fig in self.content:
            fig.selected = False
            fig.color = (0, 0, 0)
        self.redraw_content()

    def delete_content(self):
        self.content = []
        self.af_point = None
        self.clear()

    def delete_selected(self):
        self.content = [fig for fig in self.content if not fig.selected]
        self.redraw_content()
    
    def clear(self):
        self.delete('all')
        self.create_image()

    def create_image(self, state="normal"):
        self.image = PhotoImage(width=self.width, height=self.height)
        super().create_image((self.width / 2, self.height / 2), image=self.image, state=state)

    def draw_circle(self, x, y, r=10, color="red"):
        self.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)
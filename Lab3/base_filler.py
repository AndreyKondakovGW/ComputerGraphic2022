from tkinter import *
from tkinter import ttk
from draw_line import *

should_draw = False

# base class for application with filling pixel area
class BaseFiller:
    def __init__(self, root):
        self.root = root
        self.should_draw = False
        self.old_coords = None
        self.__init_ui()
        self.__init_bindings()
        self.__fill_background()

    def __init_ui(self):
        self.width = 500
        self.height = 400
        self.image = PhotoImage(width=self.width, height=self.height)
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.create_image((self.width/2, self.height/2), image=self.image)
        self.canvas.pack()

    def __fill_background(self):
        color = (255, 255, 255)
        for x in range(0, self.width):
            for y in range(0, self.height):
                draw_pix(self.image, (x, y), color)

    def __init_bindings(self):
        self.root.bind('<Motion>', self.draw_by_lines)
        self.root.bind('<ButtonPress-1>', self.start_drawing)
        self.root.bind('<ButtonRelease-1>', self.stop_drawing)
        self.root.bind('<Double-Button-1>', self.fill)


    def start_drawing(self, event):
        self.should_draw = True

    def stop_drawing(self, event):
        self.should_draw = False

    # used to draw border
    def draw_by_lines(self, event):
        new_coords = (event.x, event.y)
        if self.should_draw:
            if self.old_coords:
                line_bresenchem(self.image, new_coords, self.old_coords)
                #self.create_line(x, y, x1, y1)
        self.old_coords = new_coords

    # wrap used to save coords of initial filling point
    def fill(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.fill_with_color(self.start_x, self.start_y)

    def get_left_border(self, x, y):
        if x == 1:
            return x
        current_color = self.image.get(x, y)
        left_x = x - 1
        left_color = self.image.get(left_x, y)
        while left_color == current_color:
            if left_x == 1:
                return 1
            left_x -= 1
            left_color = self.image.get(left_x, y)
        return left_x + 1

    def get_right_border(self, x, y):
        if x == self.width - 1:
            return x
        current_color = self.image.get(x, y)
        right_x = x + 1
        right_color = self.image.get(right_x, y)
        while right_color == current_color:
            if right_x == self.width - 1:
                return right_x
            right_x += 1
            right_color = self.image.get(right_x, y)
        return right_x - 1

    def draw_gorizontal_line(self, x1, x2, y):
        for x in range(x1, x2+1):
            color = self.next_color(x, y)
            draw_pix(self.image, (x, y), color)

    # uses abstract next_color to define fill color for every pixel
    def fill_with_color(self, x, y):
        # if (y == (self.height - 1) or y == 1):
        #     return
        current_color = self.image.get(x, y)
        color = self.next_color(x, y)
        # if current_color == color:
        #     return
        left_x = self.get_left_border(x, y)
        right_x = self.get_right_border(x, y)
        
        self.draw_gorizontal_line(left_x, right_x, y)
        for new_x in range(left_x, right_x+1):
            if (y + 1) < self.height:
                high_color = self.image.get(new_x, y+1)
                if high_color == current_color:
                    self.fill_with_color(new_x, y+1)
            if (y - 1) > 0:
                low_color = self.image.get(new_x, y-1)
                if low_color == current_color:
                    self.fill_with_color(new_x, y-1)
    
    # should be implemented in child classes
    def next_color(self, x, y):
        raise NotImplementedError()

    def start(self):
        self.root.mainloop()

# root = Tk()
# app = BaseFiller(root)
# app.start()
from tkinter import *
from tkinter import ttk
from draw_line import *

class BorderFinder:
    def __init__(self, root):
        self.root = root
        self.should_draw = False
        self.old_coords = None
        self.rightest_x = -1
        self.rightest_y = None
        self.__init_ui()
        self.__init_bindings()
        self.__fill_background()

    def __init_ui(self):
        self.width = 400
        self.height = 400
        self.image = PhotoImage(width=self.width, height=self.height)
        self.mask = PhotoImage(width=self.width, height=self.height)
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.create_image((self.width/2, self.height/2), image=self.image)
        self.canvas.pack()

    def __init_bindings(self):
        self.root.bind('<Motion>', self.draw_by_lines)
        self.root.bind('<ButtonPress-1>', self.start_drawing)
        self.root.bind('<ButtonRelease-1>', self.stop_drawing)
        self.root.bind('<Double-Button-1>', self.show_border)

    def __fill_background(self):
        color = (255, 255, 255)
        for x in range(0, self.width):
            for y in range(0, self.height):
                draw_pix(self.image, (x, y), color)
                draw_pix(self.mask, (x, y), color)

    def __clear_mask(self):
        color = (255, 255, 255)
        for x in range(0, self.width):
            for y in range(0, self.height):
                draw_pix(self.mask, (x, y), color)

    def start_drawing(self, event):
        self.should_draw = True

    def stop_drawing(self, event):
        self.should_draw = False

    # used to draw border
    def draw_by_lines(self, event):
        new_coords = (event.x, event.y)
        if self.should_draw:
            if self.old_coords:
                draw_line(self.image, new_coords, self.old_coords)
                #self.create_line(x, y, x1, y1)
        self.old_coords = new_coords

    def new_point(self, x, y, direction):
        if direction == 1:
            return x+1, y-1
        elif direction == 2:
            return x, y-1
        elif direction == 3:
            return x-1, y-1
        elif direction == 4:
            return x-1, y
        elif direction == 5:
            return x-1, y+1
        elif direction == 6:
            return x, y+1
        elif direction == 7:
            return x+1, y+1
        elif direction == 0:
            return x+1, y

    def show_border(self, event):
        self.rightest_x = -1
        self.rightest_y = None
        self.__clear_mask()
        self.find_rightest_border_point(event.x, event.y)
        self.mask.write("mask.gif", format="gif")
        self.border_points = set()
        first_x, first_y = self.rightest_x, self.rightest_y
        border_color = self.image.get(first_x, first_y)
        #self.canvas.create_rectangle(first_x, first_y, first_x + 2, first_y + 2, fill='yellow')
        self.border_points.add((first_x, first_y))
        direction = 6
        x, y = first_x, first_y
        while True:
            x1, y1 = self.new_point(x, y, direction)
            if (x1 == first_x) and (y1 == first_y):
                break
            color = self.image.get(x1, y1)
            while (color != border_color):
                direction = (direction + 1) % 8
                x1, y1 = self.new_point(x, y, direction)
                if (x1 == first_x) and (y1 == first_y):
                    x, y = x1, y1
                    break
                color = self.image.get(x1, y1)
            if (x1 == first_x) and (y1 == first_y):
                break
            x, y = x1, y1
            self.border_points.add((x, y))
            print(f"add point ({x},{y})")
            #self.highlight_pixel(x, y)
            direction = (direction - 2) % 8
        self.highlight_border()
        
    def highlight_pixel(self, x, y):
        color = (255, 0, 0)
        draw_pix(self.image, (x, y), color)

    def highlight_border(self):
        self.border_image = PhotoImage(width=self.width, height=self.height)
        color = (255, 0, 0)
        for p in self.border_points:
            draw_pix(self.image, p, color)
            draw_pix(self.border_image, p, color)
        self.border_image.write("border.gif", format="gif")

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

    def check_mask(self, x, y):
        current_mask_color = self.mask.get(x, y)
        mask_color = (255, 0, 0)
        return mask_color == current_mask_color

    def find_rightest_border_point(self, x, y):
        # if (y == (self.height - 1) or y == 1):
        #     return
        if self.check_mask(x, y):
            return
        
        current_color = self.image.get(x, y)
        left_x = self.get_left_border(x, y)
        right_x = self.get_right_border(x, y)
        if right_x > self.rightest_x:
            # print(right_x, y)
            self.rightest_x = right_x + 1
            self.rightest_y = y

        self.mask_gorizontal_line(left_x, right_x, y)
        for new_x in range(left_x, right_x+1):
            if (y + 1) < self.height:
                high_color = self.image.get(new_x, y+1)
                if high_color == current_color:
                    self.find_rightest_border_point(new_x, y+1)
            if (y - 1) > 0:
                low_color = self.image.get(new_x, y-1)
                if low_color == current_color:
                    self.find_rightest_border_point(new_x, y-1)

    def mask_gorizontal_line(self, x1, x2, y):
        color = (255, 0, 0)
        for x in range(x1, x2+1):
            draw_pix(self.mask, (x, y), color)

    def start(self):
        self.root.mainloop()

root = Tk()
border_finder = BorderFinder(root)
border_finder.start()
from tkinter import Tk, Toplevel, Label, Frame, Entry, Button

class FunctionPlotterModalWindow:
    def __init__(self, root: Tk):
        self.popup = Toplevel(root)
        self.setup_popup()
        self.setup_popup_ui()

    def setup_popup(self):
        self.popup.title = "Plotter"
        self.popup.geometry("230x150")
        self.popup.config(bg="white")

    def setup_popup_ui(self):
        self.setup_function_inputs(r=0)
        self.setup_constraints_inputs(r=1)
        self.setup_apply_button(r=2)

    def setup_function_inputs(self, r=0):
        self.func_frame = Frame(self.popup)
        self.func_label = Label(self.func_frame, text="f(x, y) = ")
        self.func_input = Entry(self.func_frame)
        self.func_label.grid(row=0, column=0)
        self.func_input.grid(row=0, column=1)
        self.func_frame.grid(row=r)
    
    def setup_constraints_inputs(self, r=1):
        self.constraints_frame = Frame(self.popup)
        self.constraints_frame.grid(row=r, column=0)
        
        self.xa_label = Label(self.constraints_frame, text="xa = ")
        self.xa_input = Entry(self.constraints_frame)
        
        self.xb_label = Label(self.constraints_frame, text="xb = ")
        self.xb_input = Entry(self.constraints_frame)
        
        self.ya_label = Label(self.constraints_frame, text="ya = ")
        self.ya_input = Entry(self.constraints_frame)
        
        self.yb_label = Label(self.constraints_frame, text="yb = ")
        self.yb_input = Entry(self.constraints_frame)

        self.xa_label.grid(row=0, column=0)
        self.xa_input.grid(row=0, column=1)
        self.xb_label.grid(row=1, column=0)
        self.xb_input.grid(row=1, column=1)
        self.ya_label.grid(row=2, column=0)
        self.ya_input.grid(row=2, column=1)
        self.yb_label.grid(row=3, column=0)
        self.yb_input.grid(row=3, column=1)

    def setup_apply_button(self, r=2):
        self.apply_button = Button(self.popup, text="Apply", command=self.apply)
        self.apply_button.grid(row=r)

    def apply(self):
        print("Apply")
        self.f = self.func_input.get()
        self.xa = float(self.xa_input.get())
        self.xb = float(self.xb_input.get())
        self.ya = float(self.ya_input.get())
        self.yb = float(self.yb_input.get())
        self.popup.destroy()

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.button = Button(self.root, text="Popup", command=self.popup)
        self.button.grid(row=0)

    def popup(self):
        self.popup = FunctionPlotterModalWindow(self.root)
        self.root.wait_window(self.popup.popup)

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    mw = MainWindow(root)
    mw.mainloop()
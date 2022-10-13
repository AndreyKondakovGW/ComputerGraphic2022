

class Strage:
    def __init__(self, figs,canvas):
        self.canvas = canvas
        self.figs = figs

    def add_figure(self, fig):
        self.figs.append(fig)
        fig.draw(self.canvas)

    def draw(self, canvas):
        for fig in self.figs:
            fig.draw(canvas)

    def delete_all(self):
        self.figs = []

    def delete_selected(self):
        self.figs = [fig for fig in self.figs if not fig.selected]

    def select(self, pred):
        for fig in self.figs:
            if pred(fig):
                fig.selected = True
                fig.color = (255, 0, 0)
    
    def deselect_figs(self):
        for fig in self.figs:
            fig.selected = False
            fig.color = (0, 0, 0)

    def call(self, func):
        res = []
        for fig in self.figs:
            res += func(fig)
        return res
    
    def apply(self, func):
        for fig in self.figs:
            func(fig)
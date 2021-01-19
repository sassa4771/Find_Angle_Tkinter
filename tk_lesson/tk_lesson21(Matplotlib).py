from tkinter import *
from PIL import ImageTk , Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Creating Canvas")
        self.minsize(640, 400)

        self.matplitCanvas()

    def matplitCanvas(self):
        f = Figure(figsize =(5,5), dpi=100)
        a = f.add_subplot(111)

        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side =BOTTOM, fill = BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.pack(side =TOP, fill = BOTH, expand = True)


if __name__ == "__main__":
    root = Root()
    root.mainloop()
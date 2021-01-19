from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Creating Canvas")
        self.minsize(640, 400)

        self.matplitCanvas()

    def matplitCanvas(self):
        fig = Figure(figsize =(5,5), dpi=100)
        axis = fig.add_subplot(111)

        xValues = [1,2,3,4]
        yValues0 = [6,7,8,7.5]
        yValues1 = [5.5,6.5,8.6,8]
        yValues2 = [6.5,7,8,7]

        t0, = axis.plot(xValues, yValues0)
        t1, = axis.plot(xValues, yValues1)
        t2, = axis.plot(xValues, yValues2)

        axis.set_ylabel('Vertical Label')
        axis.set_xlabel('Horizontal Label')

        axis.grid()

        fig.legend((t0, t1, t2), ('First Line', 'Second Line', 'Third Line'), 'upper right')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()

        canvas._tkcanvas.pack(side = TOP,fill=BOTH, expand = True)


if __name__ == "__main__":
    root = Root()
    root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Creating Canvas")
        self.minsize(640, 400)

        self.createCanvas()
    
    def createCanvas(self):
        canvas = Canvas(self, bg = "blue", height = 250, width = 300)
        coord  =10, 50, 240, 210

        canvas.pack(expand = YES, fill = BOTH)

        arc = canvas.create_arc(coord, start = 0,extent = 150, fill = "red")
        canvas.pack()



if __name__ == "__main__":
    root = Root()
    root.mainloop()
from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Geometry Managment")
        self.minsize(640, 400)

        self.createWidget()

    def createWidget(self):
        label = Label(self, text = "Pack Geometry")
        label2 = Label (self, text = "Pack2 Geometry")
        label3 = Label(self, text = "Pack3 Geometry")
        
        # # use grid
        # label.grid(column = 0, row = 0)
        # label2.grid(column = 0, row = 1)
        # label3.grid(column = 0, row = 2)

        # #use place
        # label.place(x = 20, y = 30)
        # label2.place(x = 50, y = 70)
        # label3.place(x = 40, y = 50)

        # # use pack
        # label.pack()
        # label2.pack()
        # label3.pack()

root = Root()
root.mainloop()
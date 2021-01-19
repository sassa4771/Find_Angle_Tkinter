from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Labels")
        self.minsize(640, 400)

        self.createWidget()

    def createWidget(self):
        label = Label(self, text = "Hello Tkinter Application")
        label.grid(column = 0, row = 0)

        label2 = Label(self, text = "My second Label In Tkinter")
        label2.grid(column = 0, row = 1)
root = Root()
root.mainloop()
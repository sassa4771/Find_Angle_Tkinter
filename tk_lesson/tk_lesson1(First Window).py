from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter First Window")
        self.minsize(640,400)
        self.configure(background = '#4D4D4D')


root = Root()
root.mainloop()
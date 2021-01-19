from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Geometry Managment")
        self.minsize(640, 400)

        self.label = ttk.Label(self, text = "Hello Tkinter")
        self.label.grid(column = 1, row = 0)

        # # nomal button
        # button = Button(self, text = "Click Me")
        # button.grid(column = 0, row = 0)

        # nice button
        self.button = ttk.Button(self, text = "Click Me",command = self.clickMe)
        self.button.grid(column = 0, row = 0)
    
    def clickMe(self):
        self.label.configure(text = "This Is The Changed Text")
        self.label.configure(foreground = 'green')

root = Root()
root.mainloop()
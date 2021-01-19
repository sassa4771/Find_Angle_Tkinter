from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Textbox")
        self.minsize(640, 400)
        
        self.initUI()
    def clickMe(self):
        self.label.configure(text = "Hello " + self.name.get())

    def initUI(self):
        self.name = StringVar()

        self.label = ttk.Label(self, text = "Enter Your Name")
        self.label.grid(column = 0, row = 0)

        self.textbox = ttk.Entry(self, width = 20, textvariable = self.name)
        self.textbox.grid(column = 0, row = 1)

        self.button = ttk.Button(self, text = "Click Me", command = self.clickMe)
        self.button.grid(column = 0, row = 2)

root = Root()
root.mainloop()
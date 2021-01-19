from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Check Button")
        self.minsize(640, 400)

        self.checkButton()

    def checkButton(self):
        self.check1 = ttk.Checkbutton(self, text = "Disabled", state = "disabled")
        self.check1.grid(row = 0, column = 0, sticky = W)

        self.check2 = ttk.Checkbutton(self, text = "Unchecked")
        self.check2.grid(row = 0, column = 1)

        self.check3 = ttk.Checkbutton(self, text = "Enabled")
        self.check3.grid(row = 0, column = 2)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
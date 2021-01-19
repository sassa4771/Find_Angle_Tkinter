from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Spin Box")
        self.minsize(640, 400)
    
        self.spinBox()

    def spinCallBack(self):
        value = self.spin.get()
        print(value)
        self.scrollText.insert(INSERT, value)

    def spinBox(self):
        self.spin = ttk.Spinbox(self, from_ = 0, to=20, command = self.spinCallBack)
        self.spin.grid(column = 0, row = 2)

        scroll_w = 30
        scroll_h = 10

        self.scrollText = scrolledtext.ScrolledText(self, width = scroll_w, height = scroll_h, wrap=WORD)
        self.scrollText.grid(column = 1, row = 2)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
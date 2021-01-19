from tkinter import *
from tkinter import scrolledtext



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Scroll text")
        self.minsize(640, 400)

        self.scrollTextCtr()

    def scrollTextCtr(self):
        scroll_w = 30
        scroll_h = 10

        scrollText = scrolledtext.ScrolledText(self, width = scroll_w, height = scroll_h, wrap=WORD)
        scrollText.grid(column=0,row=0,columnspan =3)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
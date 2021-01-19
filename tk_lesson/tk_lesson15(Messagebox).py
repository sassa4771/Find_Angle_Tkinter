from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Messagebox")
        self.minsize(640, 400)

        self.msgButton()

    def msgButton(self):
        self.btn = ttk.Button(self, text ="Open Message Box",command=self.errorMsgBox)
        self.btn.grid(column = 0, row =0)

    def infoMsgBox(self):
        msg.showinfo("Python Message Info", "Python GUI Created By Tkinter")
        
    def wornMsgBox(self):
        msg.showinfo("Python Warning message Box", "This Is A Warning Message Box")
        
    def errorMsgBox(self):
        msg.showerror("Python Error message Box", "This Is A Error Message Box")

if __name__ == "__main__":
    root = Root()
    root.mainloop()
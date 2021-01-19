from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Browsing A File")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text ="Open A File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File" ,command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetype = (("jpeg", "*.jpg"),("All Files", "*.*")))
        
        print(self.filename)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
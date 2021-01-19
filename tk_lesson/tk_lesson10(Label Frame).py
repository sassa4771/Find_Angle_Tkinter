from tkinter import *
from tkinter import ttk



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Label Frame")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text ="My Label Frame")
        self.labelFrame.grid(column = 0, row = 7, padx = 20, pady = 40)

        self.labels()

    def labels(self):
        ttk.Label(self.labelFrame, text = "Label One").grid(column = 0, row = 0, sticky = W)
        
        ttk.Label(self.labelFrame, text = "Label Twe").grid(column = 0, row = 1, sticky = W)

        ttk.Label(self.labelFrame, text = "Label Three").grid(column = 0, row = 2, sticky = W)
        

if __name__ == "__main__":
    root = Root()
    root.mainloop()
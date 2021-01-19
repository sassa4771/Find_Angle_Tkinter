from tkinter import *
from tkinter import ttk



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Tab Controls")
        self.minsize(640, 400)

        tabControl = ttk.Notebook(self)
        tab1= ttk.Frame(tabControl)
        tabControl.add(tab1, text = "Tab 1")

        tab2= ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Tab 2")

        tab3= ttk.Frame(tabControl)
        tabControl.add(tab3, text = "Tab 3")

        tabControl.pack(expan = 1, fill = "both")

if __name__ == "__main__":
    root = Root()
    root.mainloop()
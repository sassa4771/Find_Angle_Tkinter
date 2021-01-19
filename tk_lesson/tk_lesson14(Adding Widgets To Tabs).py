from tkinter import *
from tkinter import ttk



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Adding Widgets To Tabs")
        self.minsize(640, 400)

        tabControl = ttk.Notebook(self)
        self.tab1= ttk.Frame(tabControl)
        tabControl.add(self.tab1, text = "Tab 1")

        self.tab2= ttk.Frame(tabControl)
        tabControl.add(self.tab2, text = "Tab 2")

        tabControl.pack(expan = 1, fill = "both")

        self.addingWidhets()

    def addingWidhets(self):
        labelFrame = ttk.LabelFrame(self.tab1, text = "First Tab Widgets")
        labelFrame.grid(column = 0, row = 0,padx = 8, pady = 10)

        label = ttk.Label(labelFrame, text = "Enter Your Name:")
        label.grid(column = 0, row = 0, sticky = 'W')

        textedit = Entry(labelFrame, width = 20)
        textedit.grid(column = 1,row =0)
        
        label = ttk.Label(labelFrame, text = "Enter Pasword:")
        label.grid(column = 0, row = 1, sticky = 'W')

        textedit = Entry(labelFrame, width = 20)
        textedit.grid(column = 1,row =1)

        
        labelFrame = ttk.LabelFrame(self.tab2, text = "Second Tab Widgets")
        labelFrame.grid(column = 0, row = 0,padx = 8, pady = 10)

        label = ttk.Label(labelFrame, text = "Enter Your Name:")
        label.grid(column = 0, row = 0, sticky = 'W')

        textedit = Entry(labelFrame, width = 20)
        textedit.grid(column = 1,row =0)
        
        label = ttk.Label(labelFrame, text = "Enter Pasword:")
        label.grid(column = 0, row = 1, sticky = 'W')

        textedit = Entry(labelFrame, width = 20)
        textedit.grid(column = 1,row =1)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
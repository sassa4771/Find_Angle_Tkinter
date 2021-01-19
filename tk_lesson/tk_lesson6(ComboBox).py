from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter ComboBox")
        self.minsize(640, 400)

        self.InitUI()

    def clickMe(self):
        self.label.configure(text = "You Have Selected " + self.myfruit.get())
        
    def InitUI(self):
        self.myfruit = StringVar()

        self.combo = ttk.Combobox(self, width = 15, textvariable = self.myfruit)
        self.combo['value'] = ("Apple", "Pear", "Melon", "Water Melon", "Banana")
        self.combo.grid(column = 1, row =0)

        self.label = ttk.Label(self, text = "Select Your Favarite Fruit")
        self.label.grid(column = 0, row = 0)

        self.button = ttk.Button(self, text = "Click Me", command = self.clickMe)
        self.button.grid(column = 1, row = 1)

if __name__ == "__main__":
    root = Root()
    root.mainloop()
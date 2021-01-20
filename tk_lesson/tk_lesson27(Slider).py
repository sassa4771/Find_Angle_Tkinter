# tkinter
from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Slider")
        self.minsize(640,400)
        
        # slider
        self.label = ttk.Label(self, text = "slider Test")
        self.label.grid(column=0,row=0)
  
        self.slider = Scale(self, from_=1, to=10, orient=HORIZONTAL, command = self.showslidervalue)
        self.slider.grid(column=0,row=1)

    def showslidervalue(self,_):
        print(self.slider.get())

if __name__ == "__main__":
    root = Root()
    root.mainloop()
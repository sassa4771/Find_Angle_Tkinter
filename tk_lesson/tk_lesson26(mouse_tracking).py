from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class Set_Pivot_Position(Tk):
    def __init__(self):
        super(Set_Pivot_Position, self).__init__()
        self.title("Select Area")
        self.minsize(600,400)
        
        self.imagefile = Image.open("Books.jpg")

        self.img = ImageTk.PhotoImage(file='red.png')
        bgimg = ImageTk.PhotoImage(self.imagefile)
        self.canvas = Canvas(self, width=bgimg.width(), height=bgimg.height(),
                   borderwidth=0, highlightthickness=0)
        self.bgcimg = self.canvas.create_image(0, 0, image=bgimg, anchor=NW)
        self.cimg = self.canvas.create_image(0, 0, image=self.img)
        
        self.canvas.pack(expand=True)
        self.canvas.img = bgimg
        self.canvas.bind('<B1-Motion>', self.Mousecoords) # track mouse movement

    def Mousecoords(self,event):
        self.pointxy = (event.x, event.y) # get the mouse position from event
        print("Pivot【X: " + str(self.pointxy[0]) + ", Y: " + str(self.pointxy[1]) + "】")
        self.canvas.coords(self.cimg, self.pointxy) # move the image to mouse postion

if __name__ == "__main__":
    root = Set_Pivot_Position()
    root.mainloop()
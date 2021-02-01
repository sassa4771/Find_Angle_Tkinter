from tkinter import *
from PIL import ImageTk , Image

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Creating Canvas")
        self.minsize(640, 400)
        # img = ImageTk.PhotoImage(Image.open(self.filepath))
        img = ImageTk.PhotoImage(Image.open('Books.jpg'))
        self.canvas = Canvas(self, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
        PhotoImage(master = self.canvas, width = img.width(), height = img.height())
        self.canvas.pack()
        self.canvas.img = img  # Keep reference in case this code is put into a function.
        self.canvas.create_image(0, 0, image=img, anchor = NW)



if __name__ == "__main__":
    root = Root()
    root.mainloop()
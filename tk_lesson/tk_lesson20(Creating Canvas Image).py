from tkinter import *
from PIL import ImageTk , Image

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Creating Canvas")
        self.minsize(640, 400)

        self.createCanvasImage()
    
    def createCanvasImage(self):
        canvas = Canvas(self, bg = "black", height = 250, width = 300)

        canvas.pack(expand = YES, fill = BOTH)

        img = Image.open('mount.jpg')
        canvas.image = ImageTk,PhotoImage(img)
        canvas.create_image(0,0, image = canvas.image, anchor = 'pw')



if __name__ == "__main__":
    root = Root()
    root.mainloop()
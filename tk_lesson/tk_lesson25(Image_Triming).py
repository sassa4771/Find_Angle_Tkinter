from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

WIDTH, HEIGHT = 900, 900
topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None
path = "Books.jpg"

class Create_Image_Cut_Tool(Tk):

    def __init__(self):
        super(Create_Image_Cut_Tool, self).__init__()
        self.title("Select Area")
        self.minsize(640,400)
        self.geometry('%sx%s' % (WIDTH, HEIGHT))
        self.configure(background='grey')
            
        self.topx, self.topy, self.botx, self.boty = 0, 0, 0, 0
        self.rect_id = None

        # img = ImageTk.PhotoImage(Image.open(self.filepath))
        img = ImageTk.PhotoImage(Image.open(path))
        self.canvas = Canvas(self, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
        PhotoImage(master = self.canvas, width = img.width(), height = img.height())
        self.canvas.pack()
        self.canvas.img = img  # Keep reference in case this code is put into a function.
        self.canvas.create_image(0, 0, image=img, anchor = NW)

        # Create selection rectangle (invisible since corner points are equal).
        self.rect_id = self.canvas.create_rectangle(self.topx, self.topy, self.topx, self.topy, dash=(2,2), fill='', outline='white')
                                                
        self.canvas.bind('<Button-1>', self.get_mouse_posn)
        self.canvas.bind('<B1-Motion>', self.update_sel_rect)
        
    def get_mouse_posn(self,event):
        self.topx, self.topy = event.x, event.y

    def update_sel_rect(self,event):
        self.botx, self.boty = event.x, event.y
        self.canvas.coords(self.rect_id, self.topx, self.topy, self.botx, self.boty)  # Update selection rect.

        print("topx: " + str(self.topx) + "px, topy: " + str(self.topy) + "px, botx: " + str(self.botx) + "px, boty:" + str(self.boty) + "px")


if __name__ == "__main__":
    ci = Create_Image_Cut_Tool()
    ci.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import math


class Image_Rotation_Tool(Toplevel):

    def __init__(self, ImageFile, Root):
        super(Image_Rotation_Tool, self).__init__()
        self.imagefile = ImageFile
        self.title("Select Area")
        self.minsize(640,400)
        self.geometry('%sx%s' % (ImageFile.width, ImageFile.height))
        self.configure(background='grey')
        self.root = Root
        
        self.c_x = ImageFile.width/2
        self.c_y = ImageFile.height/2

        self.topx, self.topy, self.botx, self.boty = 0, 0, 0, 0
        self.rect_id = None

        # Close Button
        self.button_close = ttk.Button(self, text = "Finsh To Select Range", command = self.close_window)
        self.button_close.pack()

        # img = ImageTk.PhotoImage(Image.open(self.filepath))
        img = ImageTk.PhotoImage(ImageFile)
        self.canvas = Canvas(self, width=img.width(), height=img.height(), borderwidth=0, highlightthickness=0)
        PhotoImage(master = self.canvas, width = img.width(), height = img.height())
        self.canvas.pack()
        self.canvas.img = img  # Keep reference in case this code is put into a function.
        self.rotate_image = self.canvas.create_image(0, 0, image=img, anchor = NW)

        # Create selection rectangle (invisible since corner points are equal).
        self.rect_id = self.canvas.create_rectangle(self.topx, self.topy, self.topx, self.topy, dash=(2,2), fill='', outline='white')
                                                
        self.canvas.bind('<Button-1>', self.get_mouse_posn)
        self.canvas.bind('<B1-Motion>', self.update_sel_rect)
        
    def get_mouse_posn(self,event):
        self.topx, self.topy = event.x, event.y

    def update_sel_rect(self,event):
        self.botx, self.boty = event.x, event.y
        self.canvas.coords(self.rect_id, self.topx, self.topy, self.botx, self.boty)  # Update selection rect.

        self.root.label_cut.configure(text = "Cut Range【X:" + str(self.topx) + "-" + str(self.botx) + ", Y:" + str(self.topy) + "-" + str(self. boty) + "】")
        self.root.label_cut.configure(foreground = 'Black')

        self.rotation_image()

        print("topx: " + str(self.topx) + "px, topy: " + str(self.topy) + "px, botx: " + str(self.botx) + "px, boty:" + str(self.boty) + "px")
    
    def rotation_image(self):
        # 元画像の中心を軸に回転する
        angle = self.get_angle(self.botx, self.boty, self.c_x, self.c_y, self.topx, self.topy)
        self.rotate_image = self.imagefile.rotate(angle)
        print("angle: " + str(angle))
        
    def close_window(self): 
        self.destroy()
        self.update()
        
        self.root.DrawLine()

    
    def get_angle(self,x1, y1, x2, y2, x3, y3):
        angle = (math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2)) / math.pi * 180

        return angle


if __name__ == "__main__":
    ci = Image_Rotation_Tool()
    ci.mainloop()
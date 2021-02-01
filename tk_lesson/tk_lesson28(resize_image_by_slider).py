from tkinter import *
from PIL import ImageTk , Image
import cv2
import cv2_pil

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Creating Canvas")
        self.minsize(640, 400)

        # Parts Position
        self.rp_x = 10   #Reference Position
        self.rp_y = 10   #Reference Position
        # y axis
        self.lp1 = 0+self.rp_y
        self.p1 = 30+self.rp_y
        self.lp2 = 60+self.rp_y
        self.p2 = 90+self.rp_y
        self.lp3 = 120+self.rp_y
        self.p3 = 140+self.rp_y
        self.lp4 = 200+self.rp_y
        # self.p4 = 210+self.rp_y
        self.lp5 = 240+self.rp_y
        self.p5 = 270+self.rp_y
        self.lp6 = 280+self.rp_y
        self.lp7 = 320+self.rp_y
        self.lp8 = 360+self.rp_y
        
        self.slider = Scale(self, from_=1, to=10, orient=HORIZONTAL, command = self.getslider)
        self.slider.place(x = self.rp_x, y = self.p1)

        self.image_path = 'Screenshot from 2021-01-21 17-26-10.png'
        self.image = Image.open(self.image_path)
        self.img = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height(), borderwidth=0, highlightthickness=0)
        PhotoImage(master = self.canvas, width = self.img.width(), height = self.img.height())
        self.canvas.place(x = self.rp_x, y = self.p2)
        self.canvas.img = self.img  # Keep reference in case this code is put into a function.
        self.canvas.create_image(0, 0, image=self.img, anchor = NW)

    def getslider(self,_):

        # convert PIL to cv2
        src = cv2.imread(self.image_path)
        resize_value = self.slider.get()

        width = int(src.shape[1]  / resize_value)
        height = int(src.shape[0] / resize_value)

        # dsize
        dsize = (width, height)
                
        # resize image
        self.resize_image = cv2.resize(src, dsize)
        
        # convert cv2 to PIL
        self.resize_img = ImageTk.PhotoImage(self.cv2pil(self.resize_image))
        self.canvas.delete("all")
        self.canvas = Canvas(self, width=self.resize_img.width(), height=self.resize_img.height(), borderwidth=0, highlightthickness=0)
        
        PhotoImage(master = self.canvas, width = self.resize_img.width(), height = self.resize_img.height())

        self.canvas.place(x = self.rp_x, y = self.p2)
        self.canvas.img = self.resize_img  
        
        self.canvas.create_image(0, 0, image=self.resize_img, anchor = NW)
        self.canvas.update
        
        print(dsize)

    def cv2pil(self,image):
        ''' OpenCV型 -> PIL型 '''
        new_image = image.copy()
        if new_image.ndim == 2:  # モノクロ
            pass
        elif new_image.shape[2] == 3:  # カラー
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
        elif new_image.shape[2] == 4:  # 透過
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
        new_image = Image.fromarray(new_image)
        return new_image

if __name__ == "__main__":
    root = Root()
    root.mainloop()
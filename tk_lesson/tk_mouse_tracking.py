from tkinter import *
from PIL import Image, ImageTk

def Mousecoords(event):
    pointxy = (event.x, event.y) # get the mouse position from event
    print(pointxy)
    canvas.coords(cimg, pointxy) # move the image to mouse postion

def update_sel_rect(event):

    botx, boty = event.x, event.y
    canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.
        
    print("topx: " + str(topx) + "px, topy: " + str(topy) + "px, botx: " + str(botx) + "px, boty:" + str(boty) + "px")

root = Tk()
img = ImageTk.PhotoImage(file='red.png')
canvas = Canvas(width=400, height=200)
cimg = canvas.create_image(200, 100, image=img)
canvas.pack()
canvas.bind('<B1-Motion>', Mousecoords) # track mouse movement
root.mainloop()
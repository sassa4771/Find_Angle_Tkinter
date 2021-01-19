from tkinter import *
from tkinter import ttk



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Menus")
        self.minsize(640, 400)

        self.createMenus()

    def createMenus(self):
        menubar = Menu(self)
        self.config(menu = menubar)

        file_menu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File",menu = file_menu)
        file_menu.add_command(label = "New")

        file_menu.add_command(label = "Exit")
        file_menu.add_separator()

        file_menu.add_command(label = "Open")

        help_menu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Help", menu = help_menu)
        help_menu.add_command(label = "About Us")
        

if __name__ == "__main__":
    root = Root()
    root.mainloop()
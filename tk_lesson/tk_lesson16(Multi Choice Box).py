from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Multi Choice Box")
        self.minsize(640, 400)

        self.button()

    def button(self):
        self.btn = ttk.Button(self, text = "Open Multi Choice Box", command=self.choiceBox)
        self.btn.grid(column = 0, row = 0)

    def choiceBox(self):
        answer = msg.askyesnocancel("Multi Choice Box", "Are Sure To Quite?")

        if answer == True:
            self.quit()

if __name__ == "__main__":
    root = Root()
    root.mainloop()
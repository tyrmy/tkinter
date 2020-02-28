from tkinter import *

class myFrame(Frame):
    def __init__(self, location):
        self.frame = LabelFrame(location, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)
        self.label = Label(self.frame, text="I am a label")
        self.label.pack()

root = Tk()
root.title("Useful App")
myFrame(root)

root.mainloop()

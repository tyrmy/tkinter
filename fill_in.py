from tkinter import *

class myFrame(Frame):
    def __init__(self, location):
        size = 9
        self.frame = LabelFrame(location, text="Fill-in form", padx=10, pady=10)
        for i in range(size):
            Label(self.frame, text="Value " + str(i)).grid(row=i, column=0)
            Entry(self.frame).grid(row=i, column=1)
        self.frame.pack(padx=10, pady=10)
        Button(self.frame, text="Submit").grid(row=size+1, column=0, columnspan=2, pady=10, padx=10)

root = Tk()
root.title("Useful App")
myFrame(root)

root.mainloop()

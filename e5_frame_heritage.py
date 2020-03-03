from tkinter import *
class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.config(pady=100, padx=100)
        self.pack()
        Label(self, text='Hello World!').pack()
        Button(self, text='Click me!').pack()

root = Tk()
app = App(root)
root.mainloop()

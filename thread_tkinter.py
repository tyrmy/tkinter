import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kello-ohjelma")
        self.root.minsize(200,50)
        self.label = tk.Label(text="")
        self.label.config(font=("Courier", 44))
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()

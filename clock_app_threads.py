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
        self.create_menu()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Uusi", command=self.notdefined)
        filemenu.add_command(label="Avaa", command=self.notdefined)
        filemenu.add_command(label="Sulje", command=self.root.destroy)
        menubar.add_cascade(label="Tiedosto", menu=filemenu)
        self.root.config(menu=menubar)

    def notdefined(self):
        pass

app=App()

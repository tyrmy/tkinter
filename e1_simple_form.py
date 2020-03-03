from tkinter import *

master = Tk() 

B = Button(master, text ="Hello", command = None)

var = StringVar()

Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
Label(master, text='Submit').grid(row=2) 

e1 = Entry(master) 
e2 = Entry(master) 

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
B.grid(row=2, column=1)

mainloop() 

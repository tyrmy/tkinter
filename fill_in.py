from tkinter import *

class myFrame(Frame):
    def __init__(self, location, input_values, frame_name):
        self.entrys = []
        self.labels = []
        self.frame = LabelFrame(location, text=frame_name, padx=10, pady=10)
        for i in range(len(input_values)):
            self.labels.append(Label(self.frame, text=input_values[i]))
            self.labels[i].grid(row=i, column=0)
            self.entrys.append(Entry(self.frame))
            self.entrys[i].grid(row=i, column=1)
        self.frame.pack(padx=10, pady=10)
        Button(self.frame, text="Submit", command=self.get_entry_values).grid(row=i+1, column=0, columnspan=2, pady=10, padx=10)

    def get_entry_values(self):
        return_values = []
        for entry in self.entrys:
            return_values.append(entry.get())
        #return return_values
        print(return_values)

root = Tk()
values = ["Banaanit","Omenat","Sitruunat","Limet"]

root.title("Useful App")
myFrame(root, values, "Hedelmät")
myFrame(root, range(5), "Arvoja")

root.mainloop()

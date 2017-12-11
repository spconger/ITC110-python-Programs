from tkinter import *
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()
    def init_window(self):
        self.master.title("Mileage Calculator")
        
        self.milesLabel=Label(self.master, text="Enter the total Miles")
        self.milesLabel.place(x=10, y=10)

        self.milesEntry=Entry(self.master)
        self.milesEntry.place(x=10, y=30)

        self.gasLabel=Label(self.master, text="Enter the total gallons")
        self.gasLabel.place(x=10, y=50)

        self.gasEntry=Entry(self.master)
        self.gasEntry.place(x=10, y=75)

        self.submit=Button(self.master, text="Submit", command=self.calculate)
        self.submit.place(x=10, y=100)

        #self.message = ""
        #self.resultLabel=Label(self.master, text=self.message)

    def calculate(self):
        miles=float(self.milesEntry.get())
        gallons=float(self.gasEntry.get())
        self.mpg=miles/gallons
        self.message="Your MPG is " + str(self.mpg)
        messagebox.showinfo("Miles Per Gallon", self.message)




root=Tk()
root.geometry=("800x800")

app=Window(root)
root.mainloop()

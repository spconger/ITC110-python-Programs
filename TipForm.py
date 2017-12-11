from tkinter import *
from Tip import Tip
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Tip Calculator")
        
        self.amountLabel=Label(self.master, text="Enter Amount")
        self.amountLabel.place(x=10, y=15)

        self.amountEntry=Entry(self.master)
        self.amountEntry.place(x=10, y=35)

        self.taxLabel=Label(self.master, text="Enter tax Percent (no % sign)")
        self.taxLabel.place(x=10,y=55)
        
        self.taxEntry=Entry(self.master)
        self.taxEntry.place(x=10, y=75)

        self.tipLabel=Label(self.master, text="Enter tip Percent (no % sign)")
        self.tipLabel.place(x=10,y=105)
        
        self.tipEntry=Entry(self.master)
        self.tipEntry.place(x=10, y=125)

        self.submit=Button(self.master, text="Submit", command=self.onClick)
        self.submit.place(x=10,y=150)

    def onClick(self):
        amount=float(self.amountEntry.get())
        taxPerc=float(self.taxEntry.get())
        tipPerc=float(self.tipEntry.get())
        t=Tip(amount, tipPerc, taxPerc)
        #message = print(t)
        messagebox.showinfo("total due", t)
            

        
        


root=Tk()
root.geometry=("800x800")

app=Window(root)
root.mainloop()

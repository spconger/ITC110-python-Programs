from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #these set the minimum and maximum size
        #for the parent frame
        master.maxsize(width=200, height=200)
        master.minsize(width=200, height=200)
        self.master=master
        self.init_window()
        
    def init_window(self):
        
        self.myLabel=Label(self.master,text="not pressed")
        self.myLabel.place(x=10,y=10)
        #in order to be able to change the label
        #you have to pack it, though packing it seems
        #to disable the placement
        self.myLabel.pack()

        self.submit=Button(self.master,text="submit", command=self.click)
        self.submit.place(x=10,y=35)
        self.submit.pack()
        

    def click(self):
        #the configure command allows the label
        #to be changed
        self.myLabel.configure(text="button pressed")


root=Tk()
root.geometry=("800x800")

app=Window(root)
root.mainloop()

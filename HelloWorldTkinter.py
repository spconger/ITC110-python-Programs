# this makes a basic window

from tkinter import *
from tkinter import messagebox


class Window(Frame):
    #we are inheriting from frame
    #and calling its init function
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()
    
    #set up the window
    def init_window(self):
        #set title of the window
        self.master.title("Hello")
        #self.pack(fill=BOTH, expand=1)
        # a label to prompt the user
        self.prompt=Label(self.master, text="Enter your name")
        #using absolute placement
        self.prompt.place(x=10,y=25)
        #creating a text box
        self.nameEntry=Entry(self.master)
        self.nameEntry.place(x=10,y=55)
        #adding a button
        self.submit=Button(self.master, text="submit", command=self.hello)
        self.submit.place(x=10,y=100)
        #self.result = Label(self.master,text="")
        #self.result.place(x=10, y=360)
        #self.result.pack()
        
    def hello(self):
        greeting = "Hello, " + self.nameEntry.get()
        messagebox.showinfo("hello", greeting)
        

     

        


root=Tk()
root.geometry=("500x400")

app=Window(root)
root.mainloop()



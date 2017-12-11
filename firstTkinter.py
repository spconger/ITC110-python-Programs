# this makes a basic window

import tkinter

top=tkinter.Tk()
greeting = tkinter.Label(top, text="Hello World")
greeting.place(x=10, y=25)
top.mainloop()

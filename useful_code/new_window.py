from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Creating new Windows")

def open():
    top = Toplevel()
    lbl = Label(top, text="Hello World").pack()
    btn2 = Button(top,text="Close Window",command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()

root.mainloop()
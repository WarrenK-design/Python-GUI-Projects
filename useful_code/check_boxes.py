# SHows how to open directory and files from within Tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Check boxes")

# Create tkinter variable
var = StringVar()

c = Checkbutton(root, text = "Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()
myLabel = Label(root, text=var.get()).pack()

def show():
    myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
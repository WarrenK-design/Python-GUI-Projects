# SHows how to open directory and files from within Tkinter
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Drop Down Menu")
root.geometry("400x400")

def show():
    myLabel = Label(root,text=clicked.get()).pack()

options = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"

]


# Drop down menu
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
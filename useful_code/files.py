# SHows how to open directory and files from within Tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root= Tk()
root.title("Files Window")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/warre/OneDrive/Desktop/My_Projects/GUI/image_viewer/images", title="Select A File",
        filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File ",command=open)
my_btn.pack()
root.mainloop()
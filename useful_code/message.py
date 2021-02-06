# THis is for pop up message boxes
# There are differnt ones we can create
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Radio Buttons')

def popup():
    response = messagebox.askyesno("This is my Popup!","Hello World")
  #  if response == 1:
  #      Label(root, text="You clicked Yes!").pack()
  #  else:
  #      Label(root, text="You clicked No!").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()
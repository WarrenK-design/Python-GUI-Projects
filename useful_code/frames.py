from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Frames')

# Create the frame
frame = LabelFrame(root, text="This is my Frame...",padx=5, pady=5)
frame.pack(padx=100,pady=100)

# Put the button inside of the frame
b = Button(frame, text="Click Me")
b.pack()
root.mainloop()
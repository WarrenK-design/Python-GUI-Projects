from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio Buttons')

# Define an thiknter in var
#r = IntVar()
#r.set(2)

modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

## clicked ##
# Updates which button is clicked
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Define our buttons
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()


myButton = Button(root, text="Click me!", command=lambda:clicked(pizza.get())).pack()
root.mainloop()
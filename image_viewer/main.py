from tkinter import *
from PIL import Image, ImageTk

# Define root
root = Tk()
root.title('Warren Image viewer')
root.iconbitmap('Google-Chrome-Google-Chrome.ico')

## Define Functionality ##
# The forward button functionality
# Inputs:
#   image_number - The current image number we are on
def forward(image_number):
    global my_label, button_f, button_b
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda:back(image_number-1))

    # Id on last image we want to disable the button
    if image_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    # Update the status bar
    status = Label(root, text="Image "+str(image_number)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)

## back ##
# Functionality for the back button
# Inputs:
#   image_number - The image which is currently on the screen number
def back(image_number):
    global my_label, button_f, button_b
    my_label.grid_forget()
    # Need to redefine features as to update them
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    # If the image is the first image, disable the back button
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    # Update the status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# Define image
my_img1 = ImageTk.PhotoImage(Image.open("images/central_park.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/liberty.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/new_york.png"))
#my_img4 = ImageTk.PhotoImage(Image.open("images/time_square.jpg"))
image_list = [my_img1,my_img2,my_img3]

# Status bar
status = Label(root, text="Image 1 of "+str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)


# Set out the layout
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

# Buttons
button_back = Button(root,text='<<', command=lambda: back(2), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root,text='>>',command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
# Sticky lets you stretch out a piece of the GUI
status.grid(row=2,column=0,columnspan=3, sticky=W+E)
root.mainloop()
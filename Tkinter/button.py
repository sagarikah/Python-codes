# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('650x400')

#adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.pack()

# function to display text when button is clicked
def clicked():
    lbl_2 = Label(root, text = "I just got clicked")
    lbl_2.pack()
    #lbl.configure(text = "I just got clicked")
 
# button widget with red color text inside
btn = Button(root, text = "Click me" , fg = "red", bg = "yellow", command=clicked)

# set Button grid
btn.pack()
 
# all widgets will be here
# Execute Tkinter
root.mainloop()

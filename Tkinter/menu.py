# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')

item.add_command(label='Open')

item.add_command(label='Exit')

menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

 
# adding a label to the root window
lbl = Label(root, text = "Welcome to GeekForGeeks")
lbl.grid()

 
# Execute Tkinter
root.mainloop()

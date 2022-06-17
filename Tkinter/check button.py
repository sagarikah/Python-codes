# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Coffee Shop")
# Set geometry(widthxheight)
root.geometry('550x400')
 
#adding a label to the root window
lbl = Label(root, text = "Welcome to our cafe", fg='grey')
lbl.grid()

lbl2 = Label(root, text = "What would you like to order?")
lbl2.grid(row=4)
             
var1 = IntVar()
Checkbutton(root, text='espresso', fg='brown', variable=var1).grid(row=6, sticky=W)

var2 = IntVar()
Checkbutton(root, text='capucchino', fg='blue', variable=var2).grid(row=7, sticky=W)

var3 = IntVar()
Checkbutton(root, text='latte', fg='purple', variable=var3).grid(row=8, sticky=W)


def clicked():
    lbl3= Label(root, text = "Thank You !")
    lbl3.grid()
    
button = Button(root, text='Place Order', fg='white', bg='green', command=clicked)
button.grid()


# Execute Tkinter
root.mainloop()

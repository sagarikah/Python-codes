# Import Module
import tkinter 
 
# create root window
root = tkinter.Tk()
 
# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding a label to the root window
lbl = tkinter.Label(root, text = "Country")
lbl.grid()


# adding drop-down list
combo = tkinter.Combobox(root)
combo['values'] = ("India", "USA", "France", "China", "Canada", "Italy")
combo.current("India")
combo.grid(column=1, row=0)

# Execute Tkinter
root.mainloop()

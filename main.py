from tkinter import *
from functions.design import *

def bin2dec(x):
    return int(x, 2)

def event(*args):
    label(root=window, text=bin2dec(var.get()), size=14, pos_x=0.3, pos_y=0.4)
    

window = Tk()
window.geometry("900x700")
window.title("Binary to Decimal")
label(root=window, text="Binary to Decimal converter", size=18, pos_x=0.35, pos_y=0.1)
label(root=window, text="Enter a binary number: ", size=14, pos_x=0.1, pos_y=0.3)
label(root=window, text="Decimal number is: ", size=14, pos_x=0.1, pos_y=0.4)
var = StringVar()
entry = Entry(window, width=35, textvariable=var)
entry.place(relx=0.4, rely=0.31)
button(root=window, text="Convert", pos_x=0.4, pos_y=0.5, event=event)
window.mainloop()
from tkinter import *
from tkinter.font import Font

def label(**kwargs):
    var = StringVar()
    font = Font(size=kwargs['size'])
    label = Label(kwargs['root'], textvariable = var, font=font)
    label.place(relx=kwargs['pos_x'], rely=kwargs['pos_y'])
    var.set(kwargs['text'])

def entry(**kwargs):
    var = StringVar()
    entry = Entry(kwargs['root'], textvariable = var)
    entry.place(relx=kwargs['pos_x'], rely=kwargs['pos_y'])
    return var

def button(**kwargs):
    button = Button(kwargs['root'], text=kwargs['text'], command=kwargs['event'])
    button.place(relx=kwargs['pos_x'], rely=kwargs['pos_y'])
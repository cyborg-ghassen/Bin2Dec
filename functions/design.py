from tkinter import *
from tkinter.font import Font

def label(**kwargs):
    var = StringVar()
    label = Label(kwargs['root'], textvariable = var)
    var.set(kwargs['text'])
    label.pack()
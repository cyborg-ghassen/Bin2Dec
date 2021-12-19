from tkinter import *
from functions.design import *
from functions.functions import *

def main():
    window = Tk()
    window.geometry("1000x700")
    window.title("Binary to Decimal")
    label(root=window, text="Binary to Decimal converter")
    window.mainloop()

if __name__ == "__main__":
    main()
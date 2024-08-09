
# Import Module
from tkinter import *
from tkinter import ttk


# create root window
root = Tk()


# window title
root.title("Welcome to Budget Tracker")
# Set geometry (widthxheight)
root.geometry('500x500')


lbl = Label(root, text="Ready to start budgeting?")
lbl.grid()


root.mainloop()

import random
import sys
import os

from tkinter import *

h = 512
w = 512
def createWindow():
    ''' creates window of a given height and width'''
    root = Tk()
    canvas = Canvas(root, width = w, height = h)
    root.title("game of life")

    top_Frame = Frame(root)
    top_Frame.pack()

    bottom_Frame = Frame(root)
    bottom_Frame.pack(side=BOTTOM)

    run_button = Button(bottom_Frame, text="Run simulation", fg = "green")
    stop_button = Button(bottom_Frame, text="Stop simulation", fg="red")
    run_button.pack(side=LEFT)
    stop_button.pack(side=LEFT)
    canvas.pack()
    canvas.mainloop()

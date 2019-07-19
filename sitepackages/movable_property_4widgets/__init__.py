#!/usr/bin/env python

import os
import tkinter as tk
from tkinter import *

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

##Demo Text widget to finilize the change.

#main = tk.Tk()
#
#frame = tk.Frame(main, bd=4, bg="grey")
#frame.place(x=10, y=10)
#make_draggable(frame)
#
#notes = tk.Text(frame)
#notes.pack()
#
#main.mainloop()

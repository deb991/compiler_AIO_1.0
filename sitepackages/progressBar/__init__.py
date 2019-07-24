#!/usr/bin/env python -i
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk

def progressBar(*args, **kwargs):
    #master = Tk()

    def progress(currentValue):
        progressbar["value"] = currentValue

    maxValue = 100

    progressbar = ttk.Progressbar((kwargs), orient="horizontal", length=150, mode="determinate", takefocus=True)
    progressbar.pack(side=tk.BOTTOM)

    currentValue = 0
    progressbar["value"] = currentValue
    progressbar["maximum"] = maxValue

    divisions = 10
    for i in range(divisions):
        currentValue = currentValue + 10
        progressbar.after(500, progress(currentValue))
        progressbar.update()  # Force an update of the GUI

    progressbar.destroy()



    #master.mainloop()

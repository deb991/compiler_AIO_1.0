#!/usr/bin/env python -i
import tkinter as tk
from tkinter import Tk, ttk
from ui.sitePackages import progressBar
from ui.sitePackages.moveable_property_4Widget import make_draggable

root = Tk()

#root.configure()
#progressBar.progressBar(root)

tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1)
tabcontrol.pack(expand=1, fill="both")

#frame = tk.Frame(root, bd=4, bg="grey")
#frame.place(x=10, y=10)
make_draggable(tab1)

notes = tk.Text(tab1)
notes.pack(ipadx=5)

L_Side_menubar = tk.Frame(root, background="blue")
L_Side_menubar.pack(fill='both', side="bottom")


progressBar.progressBar(L_Side_menubar)

#Here another switch required to close the Progree bar after loaded fully.
#Another switch required to pin down the moveable widget.
#Now working on Tabbed based notepad. Which will provide "open a new Tab on demand"



root.mainloop()

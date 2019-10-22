import os
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
import sys
import subprocess as sub
from subprocess import Popen

os.chdir("C:\\Users\\DE635273\\PycharmProjects\\Jarine_console\\J_pad\\")
sys.path.append("C:\\Users\\DE635273\\PycharmProjects\\Jarine_console\\J_pad\\editor.py")
python = sys.executable


#e = exec(open('cs1_1.py').read())

e = sub.Popen(['python', 'editor.py'], shell=True, stdout=sub.PIPE, universal_newlines=True)
out, err = e.communicate()

root = Tk()
canvas = tk.Canvas(root)
text = tk.Text(canvas)
text.pack(expand=True, fill=BOTH)
canvas.pack(expand=True, fill=BOTH)

text.insert(1.0, out)

root.mainloop()

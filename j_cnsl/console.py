#!/usr/bin/env python -i
import os
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import *

#=====Accessing Command location


ntCmdlist1 = "C:\\Windows\\System"
ntCmdlist2 = "C:\\Windows\\System32"
x11Cmd = "/usr/bin/"
sysShell = 'C:\\Windows\\System32\\cmd.exe'
curr__dir = (os.getcwd(), '/>>')

if os.path.isdir(ntCmdlist1 and ntCmdlist2):
    print(os.listdir(ntCmdlist1), '\n', os.listdir(ntCmdlist2))

elif os.path.isdir(x11Cmd):
    print(os.listdir(x11Cmd))

else:
    print('Command file not found. Please check your system.~~~~~ ::>')
    print('\n System erorr.\n commands not found.:: Error code 853')


#More loops & exceptions will be added later as per the requirement

#Building GUI as Command prompt.
#initial build will be as a native console. which will interact with system & concate the output from system shell
#to cascade on the new console window

consl = Tk()

w = 1200               # width
h = 380                # height

# get screen width and height
ws = consl.winfo_screenwidth()                  # width of the screen
hs = consl.winfo_screenheight()                 # height of the screen


# calculate x and y coordinates for the Tk desktopTaskBar window
x = (ws/1) - (w/1)
y = (hs/1) - (h/1)

consl.geometry("1200x380")
consl.resizable(1,1)
consl.configure(background='black')

#Adding canvas on Root window for other services.

cmd_OP = Canvas(consl, width=1000, height=500)
cmd_OP_viewer = Text(cmd_OP, width=700, height=350, background="black", foreground="yellow")

cmd_OP.create_window((0,0), window=cmd_OP_viewer, anchor=NW)
cmd_OP_viewer.pack(side=TOP, expand=True, fill=X)

#Font for all output & other operations.
helv9 = font.Font(family='Helvetica', size=9, weight=tkinter.font.BOLD)

# input of the console are being set.
l1 = Label(consl, text=curr__dir, background="black", foreground="yellow")
entry = Entry(consl, background="black", foreground="yellow")
entry.pack(side=BOTTOM, anchor=SW, expand=TRUE, fill=X)
entry.delete(0, END)
entry.insert(0, '>>')
l1.pack(side=BOTTOM, anchor=SW, expand=TRUE)

cmd_OP.pack()



if __name__ == '__main__':
    consl.mainloop()
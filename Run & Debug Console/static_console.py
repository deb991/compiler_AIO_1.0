#!/usr/bin/env python -i
import os
import tkinter
from tkinter import *
from tkinter import scrolledtext
import traceback

"""This program is for provoding static output window 
after gone through the EXECUTION & DEBUGING phase"""

#Few System functionality is being added to redirect into Variable window.
ntCmdlist1 = "C:\\Windows\\System"
ntCmdlist2 = "C:\\Windows\\System32"
x11Cmd = "/usr/bin/"
sysShell = 'C:\\Windows\\System32\\cmd.exe'
curr__dir = (os.getcwd(), '/>')

#Main Window is been added from here.
knsl = Tk()
knsl.title('Run & debug Console')
knsl.resizable(1, 1)
knsl.configure(background='black')


#Main canvas which will hold those editors.
maincanvas = Canvas(knsl)
maincanvas.pack(fill=BOTH, expand=True)


#Side toolbar @ left side with special details.
L_Side_menubar = Frame(maincanvas, background="grey")
L_Side_menubar.pack(fill=Y, side=LEFT)

#Special buttons on run & debug window.
project_window__button = Button(L_Side_menubar, text='R\nU\nN') #, command=f__Manager)
project_window__button.grid(column=1, row=1, columnspan=1, padx=1, sticky=NW)

project_window__button = Button(L_Side_menubar, text='D\nE\nB\nU\nG') #, command=f__Manager)
project_window__button.grid(column=1, row=4, columnspan=1, padx=1, sticky=NW)

#Editor Window
op_wndo = scrolledtext.ScrolledText(maincanvas)
op_wndo.pack(side=LEFT, fill=BOTH, expand=True)
var_wndo = scrolledtext.ScrolledText(maincanvas)
var_wndo.pack(side=RIGHT, fill=BOTH)
var_wndo.config(state=DISABLED)

def sys_CMD_OP():
    if os.path.isdir(ntCmdlist1 and ntCmdlist2):
        print(os.listdir(ntCmdlist1), '\n', os.listdir(ntCmdlist2))

    elif os.path.isdir(x11Cmd):
        print(os.listdir(x11Cmd))

    else:
        print(
            'Command file not found. Please check your system.~~~~~ ::>\n\nSystem erorr.\n commands not found.:: Error code 853')

print()
var_wndo.insert('INSERT', str(sys_CMD_OP()))
print(traceback.print_stack())

if __name__ == '__main__':
    knsl.mainloop()

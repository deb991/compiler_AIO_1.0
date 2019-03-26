#!/usr/bin/env python -i
from tkinter import *
from tkinter import scrolledtext
from commands import save__file, save_as__file, save__all, new__file, export__html, mkFleRdOnly, cut
from tkinter.messagebox import askokcancel
from tkinter import filedialog

import threading

root = Tk(className='just another code editor but with some innovative features')
edtr = scrolledtext.ScrolledText(root, width=100, height=100)

thread_list = []

#Few on demand commands
def exit():
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def open__file():
    print('Open an existing file from the system.')
    #return 'EOF'
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        edtr.insert('1.0', contents)
        file.close()

menubar = Menu(root)
fileMenu = Menu(menubar)
menubar.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label='New', command=new__file)
fileMenu.add_command(label='Open', command=open__file)
fileMenu.add_command(label='Save', command=save__file)
fileMenu.add_command(label='Save as', command=save_as__file)
fileMenu.add_command(label='Save All', command=save__all)
fileMenu.add_command(label='Export to HTML', command=export__html)
fileMenu.add_command(label='Make file read only', command=mkFleRdOnly)
fileMenu.add_command(label='Exit', command=exit)
fileMenu.add_separator()

editMenu = Menu(menubar)
menubar.add_cascade(label='Edit', menu=editMenu)

#editMenu.add_command(label='Cut', menu=cut)

root.config(menu=menubar)
edtr.pack()
if __name__ == '__main__':
    root.mainloop()

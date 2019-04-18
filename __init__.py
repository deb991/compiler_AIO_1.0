#!/usr/bin/emv python -i
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, filedialog, Frame, Canvas
from commands import *
from tkinter.messagebox import askokcancel
from idlelib.tree import FileTreeItem, ScrolledCanvas, TreeNode, _tree_widget
import threading


root = Tk('~~~~console~~~~', )
root.configure(background='grey')
edtr = Canvas(root, width=1200, height=600)

notepad = tk.Text(edtr, width=120, height=80)
ws = notepad.winfo_screenmmwidth()
hs = notepad.winfo_screenmmheight()

edtr.create_window((0, 0), window=notepad, anchor=NW)

S = Scrollbar(root)
S.pack(side=RIGHT, expand=True, fill=Y)
notepad.pack(side=LEFT, expand=True, fill=X)

S.config(command=notepad.yview)
notepad.config(yscrollcommand=S.set)
notepad.insert('end', '')

def exit():
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


t_exit = threading.Thread(target=exit)

def f__Manager():
    pass


class Struct():
    pass
#=========================================

#=========================================

#==========================================
#==========================================
class wndo(tk.Frame):
    UPDATE_PERIOD = 100  # ms
    editors = []
    updateId = None

    def __init__(self, **kw):

        super().__init__(**kw)
        print('Simple statement!!!')
        global data
        global text
        data = Struct()
        #initData(data)

        #=================By property menthods===================#


        # ================Few on demand commands=================#

    def open__file(self):
        print('Open an existing file from the system.')
        # return 'EOF'
        file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
        if file != None:
            contents = file.read()
            edtr.insert('1.0', contents)
            file.close()

    t = threading.Thread(target=open__file)

    def save__file(self):
        print('save a file')
        file = filedialog.asksaveasfile(mode='w')
        if file != None:
            # slice off the last character from get, as an extra return is added
            data = edtr.get('1.0', END + '-1c')
            file.write(data)
            file.close()
            # return 'EOF'

    t_save__file = threading.Thread(target=save__file)


    # ==============Menu Bar======================#

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

    editMenu.add_command(label='Cut', command=cut)
    editMenu.add_command(label='Copy', command=copy)
    editMenu.add_command(label='ClipBoard', command=clpBrd)
    editMenu.add_command(label='Paste', command=paste)
    editMenu.add_separator()
    editMenu.add_command(label='Delete', command=delt)

    viewMenu = Menu(menubar)
    menubar.add_cascade(label='View', menu=viewMenu)

    viewMenu.add_command(label='Full Screen mode', command=FSM)
    viewMenu.add_command(label='Presentation mode', command=PsM)
    viewMenu.add_separator()

    runMenu = Menu(menubar)
    menubar.add_cascade(label='Run', menu=runMenu)

    runMenu.add_command(label='Run', command=run)
    runMenu.add_command(label='Debug', command=dbug)
    runMenu.add_separator()
    runMenu.add_command(label='View Break points', command=VBP)

    sett = Menu(menubar)
    menubar.add_cascade(label='Settings', menu=sett)

    sett.add_command(label='Settings', command=sett)
    sett.add_separator()
    sett.add_command(label='Project Setting', command=sett__P)


    help = Menu(menubar)
    menubar.add_cascade(label='Help', menu=help)

    help.add_command(label='About', command=abt)
    help.add_command(label='File Manager', command=fleAnlzer)


    L_Side_menubar = Frame(root)
    L_Side_menubar.pack(fill=X, side=BOTTOM)

    fileManager__button = Button(L_Side_menubar, text='File Manager', command=f__Manager) #.pack(side=LEFT, padx=1, pady=1)
    fileManager__button.grid(column=0, row=1, columnspan=1, padx=1, sticky=SW)

    project_window__button = Button(L_Side_menubar, text='Project Window', command=f__Manager)
    project_window__button.grid(column=1, row=1, columnspan=1, padx=1, sticky=SW)

    debug__button = Button(L_Side_menubar, text='Debug', command=f__Manager)
    debug__button.grid(column=2, row=1, columnspan=1, padx=1, sticky=SW)

    console__button = Button(L_Side_menubar, text='Console', command=f__Manager)
    console__button.grid(column=3, row=1, columnspan=1, padx=1, sticky=SW)


        # ==========================Menu Bar==================#

        #======================Thread========================#
    thread_list = [t, t_exit, t_new__file, t_new__file, t_save_as__file, t_save__all, t_export__html,
                       t_cut, t_copy, t_clpBrd]
        #======================Thread========================#


root.config(menu=wndo.menubar)
edtr.pack()


if __name__ == '__main__':
    nPad = wndo()
    nPad.pack(side="top", fill="both", expand=True)
    root.mainloop()

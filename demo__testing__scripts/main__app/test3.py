#!/usr/bin/emv python -i
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Frame, Canvas
from J_pad.commands import *
from tkinter.messagebox import askokcancel
import threading


root = Tk('~~~~J-PAD~~~~', )
root.configure(background='grey')
notepad = tk.Text(root)
notepad.pack()

def exit():
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


t_exit = threading.Thread(target=exit)


def open__file():
    print('Open an existing file from the system.')
    # return 'EOF'
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        notepad.insert(INSERT, contents)
        file.close()

t = threading.Thread(target=open__file)

def save__file():
    print('save a file')
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = notepad.get(END, END + '-1c')
        file.write(data)
        file.close()
        # return 'EOF'


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, background="grey")
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

#class CustomText(tk.Text):
#    def __init__(self, *args, **kwargs):
#        tk.Text.__init__(self, *args, **kwargs)
#
#        # create a proxy for the underlying widget
#        self._orig = self._w + "_orig"
#        self.tk.call("rename", self._w, self._orig)
#        self.tk.createcommand(self._w, self._proxy)
#
#    def _proxy(self, *args):
#        # let the actual widget perform the requested action
#        cmd = (self._orig,) + args
#        try:
#            result = self.tk.call(cmd)
#        except Exception:
#            return None
#
#        # generate an event if something was added or deleted,
#        # or the cursor position changed
#        if (args[0] in ("insert", "replace", "delete") or
#            args[0:3] == ("mark", "set", "insert") or
#            args[0:2] == ("xview", "moveto") or
#            args[0:2] == ("xview", "scroll") or
#            args[0:2] == ("yview", "moveto") or
#            args[0:2] == ("yview", "scroll")
#        ):
#            self.event_generate("<<Change>>", when="tail")
#
#        # return what the actual widget returned
#        return result

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = notepad
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        self.text.config(background='black', foreground='grey')

    def _on_change(self, event):
        self.linenumbers.redraw()

    menubar = Menu(root, background='#000099', foreground='white',
                   activebackground='#004c99', activeforeground='white')
    fileMenu = Menu(menubar, tearoff=0, background="grey", foreground='black',
                    activebackground='#004c99', activeforeground='white')
    menubar.add_cascade(label='File', menu=fileMenu)

    fileMenu.add_command(label='New', command=t_new__file.start)
    fileMenu.add_command(label='Open', command=open__file)
    fileMenu.add_command(label='Save', command=t_save__file.start)

root.config(bg='#2A2C2B',menu=App.menubar)
#root.bind('<Button-3>',rClicker, add='')

if __name__ == '__main__':
    nPad = App()
    nPad.pack(side="top", fill="both", expand=True)
    root.mainloop()

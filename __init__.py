#!/usr/bin/env python -i
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, filedialog, Frame, Canvas
from commands import *
from tkinter.messagebox import askokcancel
import threading

root = Tk(className='just another code editor but with some innovative features')
edtr = scrolledtext.ScrolledText(root, width=100, height=100)
frame = Frame

class wndo(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        self.text.insert("end", "one\ntwo\nthree\n")
        self.text.insert("end", "four\n", ("bigfont",))
        self.text.insert("end", "five\n")

        #self.C = Canvas(root, bg="white", height=560, width=450)
        #self.C.grid(row=0, column=0, rowspan=0, columnspan=0, sticky='nsew')
        #print('Simple statement!!!')

        #self.C.pack( )

    def _on_change(self, event):
        self.linenumbers.redraw( )


        # ================Few on demand commands=================#
    def exit(self):
        if askokcancel("Quit", "Do you really want to quit?"):
            root.destroy()

    t_exit = threading.Thread(target=exit)

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

    fileMenu.add_command(label='New', command=thisCommand.new__file)
    fileMenu.add_command(label='Open', command=open__file)
    fileMenu.add_command(label='Save', command=save__file)
    fileMenu.add_command(label='Save as', command=thisCommand.save_as__file)
    fileMenu.add_command(label='Save All', command=thisCommand.save__all)
    fileMenu.add_command(label='Export to HTML', command=thisCommand.export__html)
    fileMenu.add_command(label='Make file read only', command=thisCommand.mkFleRdOnly)
    fileMenu.add_command(label='Exit', command=exit)
    fileMenu.add_separator()

    editMenu = Menu(menubar)
    menubar.add_cascade(label='Edit', menu=editMenu)

    editMenu.add_command(label='Cut', command=thisCommand.cut)
    editMenu.add_command(label='Copy', command=thisCommand.copy)
    editMenu.add_command(label='ClipBoard', command=thisCommand.clpBrd)
    editMenu.add_command(label='Paste', command=thisCommand.paste)
    editMenu.add_separator()
    editMenu.add_command(label='Delete', command=thisCommand.delt)

    viewMenu = Menu(menubar)
    menubar.add_cascade(label='View', menu=viewMenu)

    viewMenu.add_command(label='Full Screen mode', command=thisCommand.FSM)
    viewMenu.add_command(label='Presentation mode', command=thisCommand.PsM)
    viewMenu.add_separator()

    runMenu = Menu(menubar)
    menubar.add_cascade(label='Run', menu=runMenu)

    runMenu.add_command(label='Run', command=thisCommand.run)
    runMenu.add_command(label='Debug', command=thisCommand.dbug)
    runMenu.add_separator()
    runMenu.add_command(label='View Break points', command=thisCommand.VBP)

    sett = Menu(menubar)
    menubar.add_cascade(label='Settings', menu=sett)

    sett.add_command(label='Settings', command=sett)
    sett.add_separator()
    sett.add_command(label='Project Setting', command=thisCommand.sett__P)

    help = Menu(menubar)
    menubar.add_cascade(label='Help', menu=help)

    help.add_command(label='About', command=thisCommand.abt)
    help.add_command(label='File Manager', command=thisCommand.fleAnlzer)

# ==========================Menu Bar==================#

        # ======================Thread========================#
    thread_list = [t, t_exit, thisCommand.t_new__file,
                   thisCommand.t_new__file, thisCommand.t_save_as__file,
                   thisCommand.t_save__all, thisCommand.t_export__html,
                       thisCommand.t_cut, thisCommand.t_copy,
                   thisCommand.t_clpBrd]



#======================Thread========================#


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
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

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result

root.config(menu=wndo.menubar)
edtr.pack()

if __name__ == '__main__':
    root = tk.Tk( )
    wndo(root).pack(side="top", fill="both", expand=True)
    root.mainloop( )

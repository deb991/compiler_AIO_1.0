#!/usr/bin/emv python -i
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Frame, Canvas
from J_pad.commands import *
from tkinter.messagebox import askokcancel
import threading


root = Tk('~~~~J-PAD~~~~', )
root.configure(background='grey')
edtr = Canvas(root, width=1200, height=600)

notepad = tk.Text(edtr, width=900, height=400)
ws = notepad.winfo_screenmmwidth()
hs = notepad.winfo_screenmmheight()

edtr.create_window((0, 0), window=notepad, anchor=NW)

#S = Scrollbar(root)
#S.pack(side=RIGHT, expand=True, fill=Y)
notepad.pack(side=LEFT, expand=True, fill=X)

#S.config(command=notepad.yview)
#notepad.config(yscrollcommand=S.set)
notepad.insert('end', '')

#edtr.pack()

def exit():
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


t_exit = threading.Thread(target=exit)

def f__Manager():
    pass


class Struct():
    pass
#=========================================
#Text input & line count operations.
#=========================================

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
        try:
            result = self.tk.call(cmd)
        except Exception:
            return None

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

#==========================================
#==========================================


#==========================================
#Right mouse click option
#==========================================

def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        def rClick_Run(e):
            e.widget.event_generate(run())

        def rClick_Debug(e):
            e.widget.event_generate()


        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
            (' Run', lambda e=e: rClick_Run(e)),
            (' Debug', lambda e=e: rClick_Debug(e))
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")
        rmenu.config(foreground='grey', background='black')

    except TclError:
        print(' - rClick menu, something wrong')
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print(' - rClickbinder, something wrong')

#==========================================
#Right mouse click option
#==========================================



class wndo(tk.Frame):
    UPDATE_PERIOD = 100  # ms
    editors = []
    updateId = None

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

        self.text.config(background='black', foreground='grey')


    def _on_change(self, event):
        self.linenumbers.redraw()

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

    def color_text(self, edit, tag, word, fg_color='grey', bg_color='black'):
        # add a space to the end of the word
        word = word + " "
        edit.insert('end', word)

        end_index1 = edit.index('class')
        begin_index = "%s-%sc" % (end_index1, len(word) + 1)
        edit.tag_add(tag, begin_index, end_index1)
        edit.tag_config(tag, foreground='yellow', background=bg_color)

        end_index2 = edit.index('def')
        begin_index = "%s-%sc" % (end_index1, len(word) + 1)
        edit.tag_add(tag, begin_index, end_index1)
        edit.tag_config(tag, foreground='yellow', background=bg_color)

        end_index3 = edit.index('mainloop')
        begin_index = "%s-%sc" % (end_index1, len(word) + 1)
        edit.tag_add(tag, begin_index, end_index1)
        edit.tag_config(tag, foreground='yellow', background=bg_color)

        #end_index4 = edit.index('class')
        #begin_index = "%s-%sc" % (end_index1, len(word) + 1)
        #edit.tag_add(tag, begin_index, end_index1)
        #edit.tag_config(tag, foreground='yellow', background=bg_color)

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
                       t_cut, t_copy, t_clpBrd, t__f_manager]
        #======================Thread========================#

root.config(menu=wndo.menubar)
root.bind('<Button-3>',rClicker, add='')

if __name__ == '__main__':
    nPad = wndo()
    nPad.pack(side="top", fill="both", expand=True)
    #nPad.bind('<Button-3>',rClicker, add='')
    root.mainloop()

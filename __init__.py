#!/usr/bin/emv python -i
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, filedialog, Frame, Canvas
from commands import *
from tkinter.messagebox import askokcancel
from idlelib.tree import FileTreeItem, ScrolledCanvas, TreeNode, _tree_widget
import threading


root = Tk('~~~~console~~~~', )
edtr = Canvas(root, width=1200, height=600)

notepad = tk.Text(edtr, width=120, height=80)
ws = notepad.winfo_screenmmwidth()
hs = notepad.winfo_screenmmheight()

sc = ScrolledCanvas(edtr, bg="white", highlightthickness=1, takefocus=1, width=140, height=100)

edtr.create_window((0, 0), window=notepad, anchor=NW)

S = Scrollbar(root)
S.pack(side=RIGHT, expand=True, fill=Y)
notepad.pack(side=LEFT, expand=True, fill=BOTH)
sc.frame.pack(expand=True, fill=BOTH, side=RIGHT)


S.config(command=notepad.yview)
notepad.config(yscrollcommand=S.set)
notepad.insert('end', '')


item = FileTreeItem(os.path.expanduser('C://Users//'))
node = TreeNode(sc.canvas, None, item)
node.expand()


edtr.pack()

def exit():
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


t_exit = threading.Thread(target=exit)


class Struct():
    pass
#=========================================
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
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.tk.eval('''
            proc widget_proxy {widget widget_command args} 
                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]
                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} 
                    event generate  $widget <<Change>> -when tail

                # return the result from the real widget command
                return $result
            }
            ''')
        self.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(self)))

#==========================================
#==========================================
class wndo():
    UPDATE_PERIOD = 100  # ms
    editors = []
    updateId = None

    def __init__(self, *args, **kwargs):
        #self.C = Canvas(root, bg="white", height=560, width=450)
        #self.C.grid(row=0, column=0, rowspan=0, columnspan=0, sticky='nsew')
        print('Simple statement!!!')
        #self.C.pack()
        global data
        global text
        data = Struct()
        # initData(data)

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
        file = open('C:/your/file/location/myFile.xml')
        self.text.insert("end", file.read())

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

        # ==========================Menu Bar==================#

        #======================Thread========================#
    thread_list = [t, t_exit, t_new__file, t_new__file, t_save_as__file, t_save__all, t_export__html,
                       t_cut, t_copy, t_clpBrd]






        #======================Thread========================#

root.config(menu=wndo.menubar)
edtr.pack()


if __name__ == '__main__':
    #root = tk.Tk()
    nPad = wndo()
    root.mainloop()

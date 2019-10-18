import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog
#from PIL import ImageTk, Image
from custom_text import CustomText
from text_Line_Number import TextLineNumbers
#from commands import run_execute
import subprocess as sub
import pathlib
from pathlib import *



python_keywords = {'orange': 'orange', 'False': 'orange', 'None': 'orange', 'True': 'orange',
                  'and': 'orange', 'as': 'orange', 'assert': 'orange',
                  'break': 'orange', 'class': 'orange','continue': 'orange',
                  'def': 'orange', 'del': 'orange', 'elif': 'orange', 'else': 'orange',
                  'except': 'orange', 'finally': 'orange', 'for': 'orange', 'from': 'orange',
                  'global': 'orange', 'if': 'orange', 'import': 'orange', 'in': 'orange',
                  'is': 'orange', 'lambda': 'orange', 'main': 'orange','name': 'orange',
                   'nonlocal': 'orange', 'not': 'orange','or': 'orange', 'pass': 'orange',
                   'raise': 'orange', 'return': 'orange', 'try': 'orange', 'while': 'orange',
                   'with': 'orange', 'yield': 'orange', 'print': 'orange', 'tearoff': 'orange',

                    'yellow': 'yellow', '__future__': 'yellow', '__main__': 'yellow', '_dummy_thread': 'yellow',
                   '_thread': 'yellow', 'abc': 'yellow', 'aifc': 'yellow', 'argparse': 'yellow',
                   'array': 'yellow', 'ast': 'yellow', 'asynchat': 'yellow', 'asyncio': 'yellow',
                   'asyncore': 'yellow', 'atexit': 'yellow', 'audioop': 'yellow', '	base64': 'yellow',
                   'bdb': 'yellow', 'binascii': 'yellow', 'binhex': 'yellow', 'bisect': 'yellow',
                   'builtins': 'yellow', 'bz2': 'yellow',

                   'self': 'pink', 'event': 'pink',

                   'err': 'red', 'out': 'pink',
                   }


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
            e.widget.event_generate(run( ))

        def rClick_Debug(e):
            e.widget.event_generate( )

        e.widget.focus( )

        nclst = [
            (' Cut', lambda e=e: rClick_Cut(e)),
            (' Copy', lambda e=e: rClick_Copy(e)),
            (' Paste', lambda e=e: rClick_Paste(e)),
            (' Run', lambda e=e: rClick_Run(e)),
            (' Debug', lambda e=e: rClick_Debug(e))
        ]

        rmenu = tk.Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root + 40, e.y_root + 10, entry="0")
        rmenu.config(foreground='grey', background='black')

    except tk.TclError:
        print(' - rClick menu, something wrong')
        pass

    return "break"


def rClickbinder(r):
    try:
        for b in ['Text', 'Entry', 'Listbox', 'Label']:  #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except tk.TclError:
        print(' - rClickbinder, something wrong')


class NotePad():
    def __init__(self):
#Root Configuration ~~
        self.root = tk.Tk()
        try:
            self.root.attributes('-zoomed', True)

        except:
            self.root.state('zoomed')
        #self.root.resizable(False, False)
        #self.root.attributes('-fullscreen', True)
        self.root.configure(background='#253042')
        self.root.bind('<Button-3>', rClicker, add='')
        self.root.iconify()
        self.root.title('JRine Console :: '+  os.getcwd())
        self.root.bind_class("Text", "<Control-a>", self.selectall)
        self.root.bind_class("Text", "<Control-s>", self.save)

#Frame configuration ~~
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=2, column=0, columnspan=50, rowspan=49, sticky='NESW')


        self.rows = 0

#Declering Theme tkinter widget ~~
        self.style = ttk.Style()
        self.style.theme_create("body", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [7, 5, 2, 0], "background": "#253042"}},
            "TNotebook.Tab": {
                "configure": {"padding": [5, 1], "background": "#253042", "foreground": "white"},
                "map": {"background": [("selected", "black")],
                        "expand": [("selected", [2, 3, 3, 0])]}
            },
            "TProgressbar": {"configure": {"background": "orange", "troughcolor": "#253042", "borderwidth": "5"}}
        }
                                )

        self.style.theme_use("body")
        while self.rows < 50:
            self.root.rowconfigure(self.rows, weight=1)
            self.root.columnconfigure(self.rows, weight=1)
            self.rows += 1

        rows = 0


    def _on_change(self, event):
        self.linenumbers.redraw()

    def selectall(self, event):
        event.widget.tag_add("sel", "1.0", "end")

    def save(self, event):

        event.widget.tag_add("sel", "1.0", "end")
        print('File saved :: ', self.file_name)

    def highlighter(self, event):
        for k, v in python_keywords.items():
            startIndex = '1.0'
            while True:
                startIndex = self.text_expand.search(k, startIndex, tk.END)
                if startIndex:
                    endIndex = self.text_expand.index('%s+%dc' % (startIndex, (len(k))))
                    self.text_expand.tag_add(k, startIndex, endIndex)
                    self.text_expand.tag_config(k, foreground=v)
                    startIndex = endIndex
                else:
                    break

    def open(self):
        self.tab2 = ttk.Frame(self.notebook, style='My.TFrame')
        self.text_expand = CustomText(self.tab2)

        self.vsb = tk.Scrollbar(self.tab2, orient="vertical", command=self.text_expand.yview)
        self.text_expand.configure(yscrollcommand=self.vsb.set)

        self.linenumbers = TextLineNumbers(self.tab2, width=30)
        self.linenumbers.attach(self.text_expand)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text_expand.pack(expand=1, fill='both')

        self.file = open(filedialog.askopenfilename(initialdir=os.getcwd(), title='Open a Python file'))
        self.file_name = os.path.basename(self.file.name)
        self.contents = self.file.read()

        self.text_expand.insert(1.0, self.contents)
        self.notebook.add(self.tab2, text=self.file_name)

        self.text_expand.bind('<Enter>', self.highlighter)
        self.text_expand.bind("<<Change>>", self._on_change)
        self.text_expand.bind("<Configure>", self._on_change)
        self.text_expand.config(background='black', foreground='grey')
        self.file.close()

        self.notebook.focus()
        self.notebook.update()
        self.text_expand.focus()
        self.text_expand.update()


    def newFile(self):
        self.tab2 = ttk.Frame(self.notebook, style='My.TFrame')
        self.text_expand = CustomText(self.tab2)

        self.vsb = tk.Scrollbar(self.tab2, orient="vertical", command=self.text_expand.yview)
        self.text_expand.configure(yscrollcommand=self.vsb.set)

        self.linenumbers = TextLineNumbers(self.tab2, width=30)
        self.linenumbers.attach(self.text_expand)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text_expand.pack(expand=1, fill='both')

        #Creating New File::
        self.file = filedialog.asksaveasfile(initialdir=os.getcwd(), title='Create New File', )

        self.file_name = os.path.basename(self.file.name)
        #self.contents = self.file.read()

        self.text_expand.insert(1.0, '')
        self.notebook.add(self.tab2, text=self.file_name)

        self.text_expand.bind('<Key>', self.highlighter)
        self.text_expand.bind("<<Change>>", self._on_change)
        self.text_expand.bind("<Configure>", self._on_change)
        self.text_expand.config(background='black', foreground='grey')
        self.file.close()

        self.notebook.focus()
        self.notebook.update()
        self.text_expand.focus()
        self.text_expand.update()


    def Exit(self):
        self.root.destroy()


    def execute_code(self):
        result = []
        print(self.file_name)
        #Find that file & check path
        filePath = os.path.abspath(self.file_name)
        print('flag 1')
        cmd = (sys.executable + '\t' + filePath)
        #If python is defined in path::
        print('flag 2')
        p = sub.Popen(cmd, shell=True, stdout=sub.PIPE,
                      universal_newlines=True)
        print('flag 3')
        print(p)

    def console_output(self):
        console = tk.Tk()
        canvas = tk.Canvas(console)
        notepad = tk.Text(canvas)
        notepad.pack(expand=True, fill='both')
        canvas.pack(expand=True, fill='both')
        notepad.insert(tk.END, [str(self.execute_code())])
        console.mainloop()


    def menuBar(self):
        menubar = tk.Menu(self.root, background='#000099', foreground='white',
                          activebackground='#004c99', activeforeground='white')
        filemanu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                           activebackground='#004c99', activeforeground='black')
        menubar.add_cascade(label='File', menu=filemanu)
        filemanu.add_command(label='New File   [Ctrl + O]', command=self.newFile)
        filemanu.add_command(label='Open File   [Ctrl + O]', command=self.open)
        filemanu.add_command(label='Exit   [Ctrl + Q]', command=self.Exit)

        ViewMenu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                           activebackground='#004c99', activeforeground='black')

        menubar.add_cascade(label='View', menu=ViewMenu)

        ViewMenu.add_command(label='Presentation Mode', command=self.open)
        ViewMenu.add_command(label='Full-Screen Mode', command=self.open)


        RunMenu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                           activebackground='#004c99', activeforeground='black')

        menubar.add_cascade(label='Run', menu=RunMenu)

        RunMenu.add_command(label='Run   [Ctrl + Shift + F10]', command=self.console_output)
        RunMenu.add_command(label='Debug [Ctrl + Shift + F11]', command=self.open)


        HelpMenu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                           activebackground='#004c99', activeforeground='black')

        menubar.add_cascade(label='Help', menu=HelpMenu)

        HelpMenu.add_command(label='KeyMap', command=self.open)
        HelpMenu.add_command(label='Help', command=self.open)
        HelpMenu.add_command(label='Submit Feedback', command=self.open)



        HelpMenu.add_separator()
        HelpMenu.add_command(label='About', command=self.open)
        HelpMenu.add_command(label='Check For Updates', command=self.open)


        self.root.configure(menu=menubar)

    def bottom_nav(self):
        pass

    def run(self):
        self.root.mainloop()




if __name__ == '__main__':
    inst = NotePad()
    inst.menuBar()
    inst.run()

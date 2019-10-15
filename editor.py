import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from custom_text import CustomText
from text_Line_Number import TextLineNumbers
from commands import run_execute
import subprocess as sub


python_keywords = {'False': 'orange', 'None': 'orange', 'True': 'orange',
                  'and': 'orange', 'as': 'orange', 'assert': 'orange',
                  'break': 'orange', 'class': 'orange','continue': 'orange',
                  'def': 'orange', 'del': 'orange', 'elif': 'orange', 'else': 'orange',
                  'except': 'orange', 'finally': 'orange', 'for': 'orange', 'from': 'orange',
                  'global': 'orange', 'if': 'orange', 'import': 'orange', 'in': 'orange',
                  'is': 'orange', 'lambda': 'orange', 'main': 'orange','name': 'orange',
                   'nonlocal': 'orange', 'not': 'orange','or': 'orange', 'pass': 'orange',
                   'raise': 'orange', 'return': 'orange', 'self': 'orange', 'try': 'orange', 'while': 'orange',
                   'with': 'orange', 'yield': 'orange', 'print': 'orange',

                    '__future__': 'yellow', '__main__': 'yellow', '_dummy_thread': 'yellow',
                   '_thread': 'yellow', 'abc': 'yellow', 'aifc': 'yellow', 'argparse': 'yellow',
                   'array': 'yellow', 'ast': 'yellow', 'asynchat': 'yellow', 'asyncio': 'yellow',
                   'asyncore': 'yellow', 'atexit': 'yellow', 'audioop': 'yellow', '	base64': 'yellow',
                   'bdb': 'yellow', 'binascii': 'yellow', 'binhex': 'yellow', 'bisect': 'yellow',
                   'builtins': 'yellow', 'bz2': 'yellow',
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
        #self.root.resizable(False, False)
        #self.root.attributes('-fullscreen', True)
        self.root.configure(background='#253042')
        self.root.bind('<Button-3>', rClicker, add='')

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

        self.text_expand.bind("<<Change>>", self._on_change)
        self.text_expand.bind("<Configure>", self._on_change)
        self.text_expand.bind('<Key>', self.highlighter)
        self.text_expand.config(background='black', foreground='grey')
        self.file.close()

    def Exit(self):
        self.root.destroy()


    def execute_code(self):
        print(self.file_name)
        #Find that file & check path
        filePath = os.path.abspath(self.file_name)
        python_interpret = sys.executable
        print(python_interpret)
        #If python is defined in path::
        p = sub.call('python self.file_name', shell=True)
        console = tk.Tk()
        canvas = tk.Canvas(console)
        canvas.pack(expand=True, fill='both')
        notepad = tk.Text(canvas)
        notepad.pack(expand=True, fill='both')

        notepad.insert(1.0, p)

        console.mainloop()




    def menuBar(self):
        menubar = tk.Menu(self.root, background='#000099', foreground='white',
                          activebackground='#004c99', activeforeground='white')
        filemanu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                           activebackground='#004c99', activeforeground='black')
        menubar.add_cascade(label='File', menu=filemanu)
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

        RunMenu.add_command(label='Run   [Ctrl + Shift + F10]', command=self.execute_code)
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


    def bars(self):
        button_bar = tk.Frame(self.root, background='grey')

        runButton = tk.Button(button_bar, command=run_execute)
        runButton.grid(column=0, row=1, columnspan=1, padx=1, sticky=tk.SW)

        button_bar.pack(fill=tk.Y, side=tk.BOTTOM)

        self.root.configure(menu=button_bar)



    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    inst = NotePad()
    inst.menuBar()
    inst.run()

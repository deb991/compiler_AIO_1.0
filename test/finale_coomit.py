import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from custom_text import CustomText
from text_Line_Number import TextLineNumbers


class NotePad():
    def __init__(self):
#Root Configuration ~~
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='#253042')

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
        #while rows < 50:
        #    self.tab1.rowconfigure(rows, weight=1)
        #    self.tab1.columnconfigure(rows, weight=1)
        #    rows += 1

    def _on_change(self, event):
        self.linenumbers.redraw()

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
        self.file.close()

    def Exit(self):
        self.root.destroy()

    def menuBar(self):
        menubar = tk.Menu(self.root, background='#000099', foreground='white',
                          activebackground='#004c99', activeforeground='white')
        filemanu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                           activebackground='#004c99', activeforeground='white')
        menubar.add_cascade(label='File', menu=filemanu)
        filemanu.add_command(label='Open File', command=self.open)
        filemanu.add_command(label='Exit', command=self.Exit)

        self.root.configure(menu=menubar)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    inst = NotePad()
    inst.menuBar()
    inst.run()

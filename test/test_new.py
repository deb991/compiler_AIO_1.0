import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from custom_text import CustomText
from text_Line_Number import TextLineNumbers

class NotePad():
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='#253042')
        self.rows = 0
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
        ttk.Style().configure('My.TFrame', background="#253042")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=2, column=0, columnspan=50, rowspan=49, sticky='NESW')
        self.tab1 = ttk.Frame(self.notebook, style='My.TFrame')
        self.notebook.add(self.tab1, text='Tab1')

        self.text = CustomText(self.tab1)

        self.nb = ttk.Notebook(self.tab1)
        tk.Button(self.root, text="New", background='black', foreground='white',
                  command=self.new).grid(row=0, column=46, padx=2, pady=0, sticky='NESW')
        tk.Button(self.root, text="Load", background='black', foreground='white').grid \
            (row=0, column=47, padx=(1, 10), pady=0, sticky='NESW')
        tk.Button(self.root, text="-", command=self.root.iconify, background='black', foreground='white').grid \
            (row=0, column=48, padx=0, pady=0, sticky='NESW')
        tk.Button(self.root, text="X", command=self.root.destroy, background='black', foreground='white').grid \
            (row=0, column=49, padx=0, pady=0, sticky='NESW')
        self.nb.grid(row=0, column=0, columnspan=50, rowspan=49, sticky='NESW')

        self.page1 = ttk.Frame(self.nb, style='My.TFrame')
        #self.nb.add(self.page1, text='')

        rows = 0
        while rows < 50:
            self.tab1.rowconfigure(rows, weight=1)
            self.tab1.columnconfigure(rows, weight=1)
            rows += 1

        self.menuBar()

    def open(self):
        print('Opening File from Explorer :: ')
        self.file = open(filedialog.askopenfilename(initialdir=os.getcwd(), title='Open a Python file'))
        self.file_name = os.path.basename(self.file.name)
        self.contents = self.file.read()
        self.nb.add(self.page1, text=self.file_name)
        self.text.insert(1.0, self.contents)
        #self.text.pack(expand=1, fill='both')
        # self.noteBook.grid(row=1,column=0,columnspan=4,padx=5)
        self.file.close()

    def new(self):
        self.tab2 = ttk.Frame(self.notebook, style='My.TFrame')
        self.notebook.add(self.tab2, text='New Tab')

    def run(self):
        self.root.mainloop()

    def menuBar(self):
        menubar = tk.Menu(self.root, background='#000099', foreground='white',
                       activebackground='#004c99', activeforeground='white')
        filemanu = tk.Menu(menubar, tearoff=0, background="grey", foreground='black',
                        activebackground='#004c99', activeforeground='white')
        menubar.add_cascade(label='File', menu=filemanu)
        filemanu.add_command(label='open', command=self.open)
        #filemanu.add_command(label='New File', command=self.newFile)

        self.root.configure(menu=menubar)

if __name__ == '__main__':
    inst = NotePad()
    inst.run()



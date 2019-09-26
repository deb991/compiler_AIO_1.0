import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
import traceback
import pdb
import subprocess
import test

mypatterns = [('Python', '*.py'), ('Python', '*.pyw')]
keywords = ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
        'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with',
        'yield']

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

class Tab(Frame):

    def __init__(self, root, name):
        Frame.__init__(self, root)

        self.root = root
        self.name = name

        self.textWidget = CustomText(self)
        self.textWidget.pack(expand=True, fill='both')

        self.vsb = tk.Scrollbar(orient="vertical", command=self.textWidget.yview)
        self.textWidget.configure(yscrollcommand=self.vsb.set)
        self.textWidget.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.textWidget)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")

        #self.textWidget.bind("<<Change>>", self._on_change)
        #self.textWidget.bind("<Configure>", self._on_change)

    def save_tab(self):
        print(self.textWidget.get("1.0", 'end-1c'))
        file = open(filedialog.asksaveasfilename() + '.txt', 'w+')
        file.write(self.textWidget.get("1.0", 'end-1c'))
        print(os.path.basename(file.name))
        #title = os.path.basename(file.name)
        file.close()

class App():
    def __init__(self):
        title = 'New document'
        self.root = Tk()
        self.root.geometry('300x200')
        # self.root.iconbitmap('icon.ico')
        self.root.title(title)

        self.tabs = {'ky': 0}
        # Keep a record of the open tabs in a list.
        self.tab_list = []
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')


        menubar = Menu(self.root, background='#000099', foreground='white',
                       activebackground='#004c99', activeforeground='white')
        filemanu = Menu(menubar, tearoff=0, background="grey", foreground='black',
                        activebackground='#004c99', activeforeground='white')
        menubar.add_cascade(label='File', menu=filemanu)
        filemanu.add_command(label='open', command=self.open_file)
        filemanu.add_command(label='Run', command=self.run)
        filemanu.add_command(label='New__file', command=self.generate_tab)
        self.root.configure(menu=menubar)

    def open_file(self):
        file = open(filedialog.askopenfilename(), 'r+')
        text_value = file.read()
        self.textWidget.delete(1.0, "end-1c")
        self.textWidget.insert("end-1c", text_value)
        title = os.path.basename(file.name)
        self.root.title(title)
        file.close()

    def add_tab(self, name):
        tab = Tab(self.notebook, name)
        print(name)
        self.notebook.add(tab, text=name)
        self.tab_list.append(tab)

    def save_file(self):
        tab_to_save = self.get_tab()
        print(tab_to_save)
        tab_to_save.save_tab()

    def get_tab(self):
        print(self.notebook.index('current'))
        #Get the tab object from the tab_list based on the index of the currently selected tab
        tab = self.tab_list[self.notebook.index('current')]
        return tab

    def generate_tab(self):
        if self.tabs['ky'] < 20:
            self.tabs['ky'] += 1
            self.add_tab('Document ' + str(self.tabs['ky']))

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app1 = App()
    app1.run()

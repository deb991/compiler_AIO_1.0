#!/usr/bin/env python -i
from tkinter import *
from tkinter import scrolledtext, filedialog, Frame
from commands import *
from tkinter.messagebox import askokcancel
from apply.apply import apply

import threading

root = Tk(className='just another code editor but with some innovative features')
edtr = scrolledtext.ScrolledText(root, width=100, height=100)

def yscrollset(*stuff):
    ## print 'yscrollset called', stuff
    apply(textarea._vertScrollbar.set, stuff)
    lineCounter.yview_moveto(stuff[0])

def yscroll(*stuff):
    ## print 'yscroll called', stuff
    apply(textarea._textbox.yview, stuff)
    apply(lineCounter.yview, stuff)


def setLineCounter(*event):
    # should be called check_line_count
    # if the length of the main textarea (textarea) changes
    # then wake up and update the line counter
    new_length = int(textarea.index('end').split('.')[0])
    if new_length != textarea.length:
        textarea.length = new_length
        updateLineCounter( )

def updateLineCounter(self, *event):
    lineCounter.config(state='normal')
    lineCounter.delete('0.0', 'end')
    for line in range(1, textarea.length-1):
        lineCounter.insert('end', '%i\n' %line)
    lineCounter.insert('end', '%i' %(textarea.length-1))
    line, col = map(int, textarea.index("insert").split("."))
    lineCounter.mark_set("insert", "%d.0" %(line))
    lineCounter.config(state='disabled')

f = Frame
textarea=edtr(f, text_wrap='none')
lineCounter=Text(textarea.interior(), width=5, bg='grey', state='disabled')
textarea.length=int(textarea.index('end').split('.')[0])
lineCounter=Text(textarea.interior(), width=5, bg='grey',
    state='disabled')
textarea.length=int(textarea.index('end').split('.')[0])
textarea.component('text').config(yscrollcommand=yscrollset)
textarea._vertScrollbar['command'] = yscroll

#Few on demand commands
def exit():
    if askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
t_exit = threading.Thread(target=exit)

def open__file():
    print('Open an existing file from the system.')
    #return 'EOF'
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        edtr.insert('1.0', contents)
        file.close()
t = threading.Thread(target=open__file)


def save__file():
    print('save a file')
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = edtr.get('1.0', END + '-1c')
        file.write(data)
        file.close( )
    #return 'EOF'
t_save__file = threading.Thread(target=save__file)

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

#editMenu.add_command(label='Cut', menu=cut)

thread_list = [t, t_exit, t_new__file, t_new__file, t_save_as__file, t_save__all, t_export__html, t_export__html, t_cut]
root.config(menu=menubar)
edtr.pack()
if __name__ == '__main__':
    root.mainloop()

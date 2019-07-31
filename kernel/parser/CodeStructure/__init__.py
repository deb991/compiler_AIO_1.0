#!/usr/bin/env python -i
import os
import tkinter as tk
from tkinter import *
import fnmatch

keyWords = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
        'with', 'yield', 'async', 'await']

fileList = []
module_list = []

statements = input('Enter the file path details to review : ')
with open (statements, 'r') as d:
    data = d.read()
    lines = data.splitlines()
    words = data.split()
    print('Total line number of the code :: ', len(lines))
    #print(words)
    for i in words:
        # print(i)
        fileList.append(i)

for item in keyWords:
    if item in fileList:
        print('Found Match :: ', item, '\t >> Line Number:: ', enumerate(data))
    else:
        print('Not Found!!!')

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
        return result

##Root window defined:
#root = tk.Tk()
#root.title('Debug Window :: ')
#
##canvas defined:
#frame = Frame(root, width=1200, height=600)
#
#np1 = tk.Text(frame)
#np1.pack(side="right", fill="both", expand=True)
#vScBar1 = tk.Scrollbar(orient="vertical", command=frame)
#np1.configure(yscrollcommand=vScBar1)
#vScBar1.config(command=np1.yview)
#np1.config(yscrollcommand=vScBar1.set, background='black', foreground='yellow')
#vScBar1.pack(side="right", fill="y")
#
#np1.insert(END, data)
#
##np2.insert(END, data)
#
#if __name__ == '__main__':
#    root.mainloop()

#!/usr/bin/env python -i
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import *
import subprocess
import threading
from threading import Thread

#=====Accessing Command location

ntCmdlist1 = "C:\\Windows\\System"
ntCmdlist2 = "C:\\Windows\\System32"
x11Cmd = "/usr/bin/"
sysShell = 'C:\\Windows\\System32\\cmd.exe'
curr__dir = (os.getcwd(), '/>')


if os.path.isdir(ntCmdlist1 and ntCmdlist2):
    print(os.listdir(ntCmdlist1), '\n', os.listdir(ntCmdlist2))

elif os.path.isdir(x11Cmd):
    print(os.listdir(x11Cmd))

else:
    print('Command file not found. Please check your system.~~~~~ ::>')
    print('\n System erorr.\n commands not found.:: Error code 853')


#More loops & exceptions will be added later as per the requirement
#Building GUI as Command prompt.
#initial build will be as a native console. which will interact with system & concate the output from system shell
#to cascade on the new console window

consl = Tk()


w = 1200                                        # width
h = 380                                         # height

# get screen width and height
ws = consl.winfo_screenwidth()                  # width of the screen
hs = consl.winfo_screenheight()                 # height of the screen


#calculate x and y coordinates for the Tk desktopTaskBar window
x = (ws/1) - (w/1)
y = (hs/1) - (h/1)

consl.geometry("1200x380")
consl.resizable(1, 1)
consl.configure(background='black')

#Adding canvas on Root window for other services.
cmd_OP = Canvas(consl, width=1000, height=500, background="black")
cmd_OP_viewer = Text(cmd_OP, width=700, height=350, background="black", foreground="green")

cmd_OP.create_window((0,0), window=cmd_OP_viewer, anchor=NW)
ScBar = tk.Scrollbar(orient="vertical", command=cmd_OP_viewer.yview, background="grey")
cmd_OP_viewer.configure(yscrollcommand=ScBar.set)
cmd_OP_viewer.pack(side=TOP, expand=True, fill=X)

#Font for all output & other operations.
helv9 = font.Font(family='Helvetica', size=9, weight=tkinter.font.BOLD)

#input of the console are being set.
l1 = Label(consl, text=curr__dir, background="black", foreground="white")

entry = Entry(consl, background="black", foreground="white")
entry.pack(side=BOTTOM, anchor=SW, expand=TRUE, fill=X)
entry.insert(0, '')
#entry.delete(0, END)
entry.pack()

l1.pack(side=BOTTOM, anchor=SW, expand=TRUE)
cmdOP = subprocess.check_call(entry.get(), shell=True)
entry.bind("<Return>", (lambda event: (get_entry())))


def run_win_cmd():
    result = []
    try:
        process = subprocess.Popen(entry.get(),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, universal_newlines=False)
    except:
        process = os.system(entry.get())
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        data = "".join(map(bytes.decode, result))
        return data
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details for :: \n', entry.get(), process)

    # Redirecting a text file for log purpose.
t_run_win_cmd = threading.Thread(target=run_win_cmd)


def get_entry():
    while TRUE:
        if entry.get() != "exit":
            cmd_OP_viewer.insert(END, str(run_win_cmd()))
            cmd_OP_viewer.config(state=DISABLED)
            entry.delete(0, END)
            break
        else:
            os.system(exit())
        break


cmd_OP.pack( )

#t_run_win_cmd.setDaemon(True)

if __name__ == '__main__':
    consl.mainloop()
